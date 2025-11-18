#!/bin/bash
set -e

# This script generates a report from test artifacts and pushes it to the repository
# Usage: generate_and_push_report.sh <report_dir> <report_file> <report_timestamp> <test_name> [artifacts_dir] [max_attempts]

REPORT_DIR="$1"
REPORT_FILE="$2"
REPORT_TIMESTAMP="$3"
TEST_NAME="$4"
ARTIFACTS_DIR="${5:-artifacts}"
MAX_ATTEMPTS="${6:-10}"

echo "Report directory: $REPORT_DIR"
echo "Report file: $REPORT_FILE"
echo "Report timestamp: $REPORT_TIMESTAMP"
echo "Artifacts directory: $ARTIFACTS_DIR"
echo "Max attempts: $MAX_ATTEMPTS"

git config user.name "github-actions[bot]"
git config user.email "github-actions[bot]@users.noreply.github.com"

# Function to copy file only if MD5 differs
copy_if_changed() {
  local src="$1"
  local dst="$2"
  
  if [ ! -f "$src" ]; then
    return
  fi
  
  # Create destination directory
  mkdir -p "$(dirname "$dst")"
  
  # If destination doesn't exist, copy it
  if [ ! -f "$dst" ]; then
    cp "$src" "$dst"
    return
  fi
  
  # Compare MD5 checksums
  src_md5=$(md5sum "$src" 2>/dev/null | cut -d' ' -f1)
  dst_md5=$(md5sum "$dst" 2>/dev/null | cut -d' ' -f1)
  
  if [ "$src_md5" != "$dst_md5" ]; then
    cp "$src" "$dst"
  fi
}

# Function to generate report
generate_report() {
  echo "Generating report..."
  
  # Create report directory
  mkdir -p "$REPORT_DIR"
  
  # Copy artifacts to report directory (only if changed)
  for dir in ${ARTIFACTS_DIR}/test-results-*/; do
    if [ -f "$dir/result-summary.json" ]; then
      PACKAGE=$(jq -r '.package' "$dir/result-summary.json")
      if [ -n "$PACKAGE" ] && [ "$PACKAGE" != "null" ]; then
        mkdir -p "${REPORT_DIR}/packages/$PACKAGE"
        
        # Copy each file individually, checking MD5
        for file in "$dir"*; do
          if [ -f "$file" ]; then
            filename=$(basename "$file")
            copy_if_changed "$file" "${REPORT_DIR}/packages/$PACKAGE/$filename"
          fi
        done
      fi
    fi
  done
  
  # Collect warnings
  python3 scripts/collect_warnings.py "${ARTIFACTS_DIR}" "${REPORT_DIR}/collected-warnings.md"
  
  # Generate summary report
  python3 scripts/generate_report.py "${ARTIFACTS_DIR}" "${REPORT_DIR}" "${REPORT_FILE}"
  echo "Generated report:"
  cat "${REPORT_FILE}"
  
  # Calculate totals for summary
  TOTAL_PASSED=0
  TOTAL_FAILED=0
  TOTAL_WARNINGS=0
  
  for dir in ${ARTIFACTS_DIR}/test-results-*/; do
    if [ -f "$dir/result-summary.json" ]; then
      # Count passed/failed tests
      ORIGINAL=$(jq -r '.original_tests_outcome' "$dir/result-summary.json")
      PATCHED=$(jq -r '.patched_tests_outcome' "$dir/result-summary.json")
      
      # Use patched result if available, otherwise original
      if [ "$PATCHED" != "null" ] && [ "$PATCHED" != "skipped" ]; then
        [ "$PATCHED" = "success" ] && TOTAL_PASSED=$((TOTAL_PASSED + 1))
        [ "$PATCHED" = "failed" ] && TOTAL_FAILED=$((TOTAL_FAILED + 1))
      elif [ "$ORIGINAL" != "null" ] && [ "$ORIGINAL" != "skipped" ]; then
        [ "$ORIGINAL" = "success" ] && TOTAL_PASSED=$((TOTAL_PASSED + 1))
        [ "$ORIGINAL" = "failed" ] && TOTAL_FAILED=$((TOTAL_FAILED + 1))
      fi
      
      # Count warnings
      ORIGINAL_WARNINGS=$(jq -r '.warnings_count.original // 0' "$dir/result-summary.json")
      PATCHED_WARNINGS=$(jq -r '.warnings_count.patched // 0' "$dir/result-summary.json")
      TOTAL_WARNINGS=$((TOTAL_WARNINGS + ORIGINAL_WARNINGS + PATCHED_WARNINGS))
    fi
  done
  
  # Create status string
  STATUS="${TOTAL_PASSED} ✅ passed, ${TOTAL_FAILED} ❌ failed, ${TOTAL_WARNINGS} warnings"
  
  # Update reports index
  python3 scripts/add_summary_line.py reports/reports.md patches.json "$TEST_NAME" "$REPORT_TIMESTAMP" "$STATUS"
  echo "Updated reports index:"
  cat reports/reports.md
}

# Optimistic locking loop
ATTEMPT=0
SUCCESS=false

while [ $ATTEMPT -lt $MAX_ATTEMPTS ]; do
  ATTEMPT=$((ATTEMPT + 1))
  echo "Attempt $ATTEMPT of $MAX_ATTEMPTS"
  
  # 1. Remove all changes in the cloned project
  echo "Resetting repository to clean state..."
  git reset --hard HEAD
  git clean -fd
  
  # 2. Make the project up to date by pulling/rebasing
  echo "Updating repository..."
  git pull --rebase origin || {
    echo "⚠️  Failed to pull/rebase, retrying..."
    continue
  }
  
  # 3. Generate the report
  generate_report
  
  # 4. Try to commit and push it
  echo "Committing changes..."
  git add reports/
  
  # Check if there are changes to commit
  if git diff --cached --quiet; then
    echo "✓ No changes to commit, report is up to date"
    SUCCESS=true
    break
  fi
  
  git commit -m "[skip ci] Add report for $REPORT_TIMESTAMP"
  
  echo "Pushing changes..."
  if git push origin; then
    echo "✓ Successfully pushed report!"
    SUCCESS=true
    break
  else
    echo "⚠️  Push failed, another process updated the repository"
    echo "Retrying in 2 seconds..."
    sleep $((10 + ( RANDOM % 20 )))  # Randomized backoff between 10-30 seconds
  fi
done

if [ "$SUCCESS" = "false" ]; then
  echo "❌ Failed to push report after $MAX_ATTEMPTS attempts"
  exit 1
fi

echo "✓ Report generation completed successfully"
