#!/usr/bin/env bash

################################################################################
# run-locally.sh - Orchestrate invenio-testrig workflow locally
#
# This script automates the complete test workflow for invenio packages,
# running all commands in the correct order with sensible defaults.
#
# Usage:
#   ./run-locally.sh [config.yaml] [options]
#
# Options:
#   --workdir <path>          Working directory (default: ./workdir)
#                             Must be non-existing or empty. All output goes here.
#   --python <version>        Python version (default: python3)
#   --uv <path>               Path to uv executable (default: uv)
#   --package <name>          Test only specific package (default: all)
#   --debug                   Enable debug output for all commands
#   --keep-cache              Skip clearing git cache before initialization
#   --scope <scope>           Test scope (default: affected)
#                             Options: affected (only packages with patches), all (all packages)
#   --mode <mode>             Test execution mode (default: stop-on-success)
#                             Options: patched-only, stop-on-success, run-all
#   --disable-codestyle-checks Disable codestyle checks in tests
#   --skip-patches            Skip applying patches during testing
#   --prepare                 Only prepare (skip tests and report)
#   --help                    Show this help message
#
# Note: The config JSON is always named config.json inside the workdir.
#       All files are organized under the workdir:
#         workdir/
#         ├── config.json           (resolved config)
#         ├── cloned_repos/         (cloned repositories)
#         ├── artifacts/            (test artifacts)
#         └── report/               (HTML report)
#
#       The script runs these steps:
#       1. Setup (init, collect, filter, select-patches, clone)
#       2. Run tests
#       3. Generate report
#
# Environment Variables:
#   INVENIO_TESTRIG_COMMAND     Path to invenio-testrig command (default: invenio-testrig)
#
################################################################################

set -e  # Exit on error
set -u  # Exit on undefined variable
set -o pipefail  # Exit on pipe failure

# Default configuration constants
DEFAULT_WORKDIR="./workdir"

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Function to print colored output
print_header() {
    echo -e "${BLUE}${BOLD}===================================================${NC}"
    echo -e "${BLUE}${BOLD}$1${NC}"
    echo -e "${BLUE}${BOLD}===================================================${NC}"
}

print_step() {
    echo -e "${CYAN}${BOLD}▶ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Function to show usage
usage() {
    sed -n '2,/^$/p' "$0" | sed 's/^# \?//'
    exit 0
}

# Parse command line arguments
CONFIG_YAML=""
WORKDIR="$DEFAULT_WORKDIR"
PACKAGE_NAME=""
KEEP_CACHE=false
TEST_SCOPE="affected"
TEST_MODE="stop-on-success"
SKIP_TESTS=false
SKIP_REPORT=false
SKIP_PATCHES=false
INIT_OPTIONS=(--verbose)

while [[ $# -gt 0 ]]; do
    case $1 in
        --help|-h)
            usage
            ;;
        --workdir)
            WORKDIR="$2"
            shift 2
            ;;
        --python)
            INIT_OPTIONS+=(--python "$2")
            shift 2
            ;;
        --uv)
            INIT_OPTIONS+=(--uv "$2")
            shift 2
            ;;
        --package)
            PACKAGE_NAME="$2"
            shift 2
            ;;
        --debug)
            INIT_OPTIONS+=(--debug)
            shift
            ;;
        --keep-cache)
            KEEP_CACHE=true
            shift
            ;;
        --scope)
            TEST_SCOPE="$2"
            # Validate test scope
            if [[ ! "$TEST_SCOPE" =~ ^(affected|all)$ ]]; then
                print_error "Invalid test scope: $TEST_SCOPE"
                echo "Valid options: affected, all"
                exit 1
            fi
            INIT_OPTIONS+=(--test-scope "$TEST_SCOPE")
            shift 2
            ;;
        --mode)
            TEST_MODE="$2"
            # Validate test mode
            if [[ ! "$TEST_MODE" =~ ^(patched-only|stop-on-success|run-all)$ ]]; then
                print_error "Invalid test mode: $TEST_MODE"
                echo "Valid options: patched-only, stop-on-success, run-all"
                exit 1
            fi
            INIT_OPTIONS+=(--test-mode "$TEST_MODE")
            shift 2
            ;;
        --disable-codestyle-checks)
            INIT_OPTIONS+=(--disable-codestyle-checks)
            shift
            ;;
        --skip-patches)
            SKIP_PATCHES=true
            shift
            ;;
        --prepare)
            SKIP_TESTS=true
            SKIP_REPORT=true
            shift
            ;;
        -*)
            print_error "Unknown option: $1"
            usage
            ;;
        *)
            if [ -z "$CONFIG_YAML" ]; then
                CONFIG_YAML="$1"
            else
                print_error "Too many arguments"
                usage
            fi
            shift
            ;;
    esac
done

# Validate config if provided
if [ -n "$CONFIG_YAML" ] && [ ! -f "$CONFIG_YAML" ]; then
    print_error "Config file not found: $CONFIG_YAML"
    exit 1
fi

# Config JSON is always named config.json inside the workdir
CONFIG_JSON="$WORKDIR/config.json"

# Set up paths relative to workdir (for display and validation only - not passed to commands)
CLONE_PATH="$WORKDIR/cloned_repos"
ARTIFACTS_PATH="$WORKDIR/artifacts"
REPORT_PATH="$WORKDIR/report"

# Validate workdir
REUSE_WORKDIR=false
if [ -e "$WORKDIR" ]; then
    if [ ! -d "$WORKDIR" ]; then
        print_error "Working directory path exists but is not a directory: $WORKDIR"
        exit 1
    fi
    
    # Check if directory is empty
    if [ -n "$(ls -A "$WORKDIR" 2>/dev/null)" ]; then
        # Directory is not empty - check if it's a valid workdir to reuse
        if [ -f "$CONFIG_JSON" ]; then
            print_warning "Reusing existing working directory: $WORKDIR"
            print_warning "Will skip initialization, collection, filtering, and cloning steps."
            REUSE_WORKDIR=true
        else
            print_error "Working directory is not empty and doesn't contain a valid config: $WORKDIR"
            echo "Please use an empty directory or remove the existing one."
            exit 1
        fi
    fi
else
    # Create the workdir
    mkdir -p "$WORKDIR"
fi


INVENIO_TESTRIG_COMMAND=${INVENIO_TESTRIG_COMMAND:-invenio-testrig}

# Check if invenio-testrig is available
if ! command -v "$INVENIO_TESTRIG_COMMAND" &> /dev/null; then
    print_error "invenio-testrig command not found. Please install the package first or pass the INVENIO_TESTRIG_COMMAND environment variable with the correct path."
    exit 1
fi

# Print configuration summary
print_header "Configuration Summary"
if [ -n "$CONFIG_YAML" ]; then
    echo "Config YAML:      $CONFIG_YAML"
else
    echo "Config YAML:      (not provided)"
fi
echo "Working Dir:      $WORKDIR"
echo "Config JSON:      $CONFIG_JSON"
echo "Clone Path:       $CLONE_PATH"
echo "Artifacts Path:   $ARTIFACTS_PATH"
echo "Report Path:      $REPORT_PATH"
if [ -n "$PACKAGE_NAME" ]; then
    echo "Package Filter:   $PACKAGE_NAME"
else
    echo "Package Filter:   all packages"
fi
echo ""

# Start workflow
START_TIME=$(date +%s)

################################################################################
# STEP 1-4: Setup (init, collect, filter, select-patches, clone)
################################################################################
if [ "$REUSE_WORKDIR" = false ]; then
    print_header "STEP 1-4: Setup"
    print_step "Running complete setup: init, collect, filter, select-patches, clone..."
    
    # Clear cache if requested (must be before setup)
    if [ "$KEEP_CACHE" = false ]; then
        # Only clear if workdir exists and has git_cache
        if [ -d "$WORKDIR/git_cache" ]; then
            print_step "Clearing git cache..."
            rm -rf "$WORKDIR/git_cache"
            print_success "Git cache cleared"
        fi
    else
        print_success "Keeping existing git cache (--keep-cache)"
    fi
    
    # Build setup command with optional config
    if [ -n "$CONFIG_YAML" ]; then
        "${INVENIO_TESTRIG_COMMAND}" setup "$CONFIG_YAML" --workdir "$WORKDIR" "${INIT_OPTIONS[@]}"
    else
        "${INVENIO_TESTRIG_COMMAND}" setup --workdir "$WORKDIR" "${INIT_OPTIONS[@]}"
    fi

    print_success "Setup complete: $CLONE_PATH"
    echo ""
else
    print_warning "Skipping setup (reusing existing workdir with repositories at $CLONE_PATH)"
    if [ ! -d "$CLONE_PATH" ]; then
        print_error "Clone path does not exist: $CLONE_PATH"
        exit 1
    fi
    echo ""
fi

################################################################################
# STEP 2: Run tests
################################################################################
if [ "$SKIP_TESTS" = false ]; then
    print_header "STEP 2: Run Tests"

    # Extract package list from config
    print_step "Extracting package list..."
    
    # Use jq to extract the package list from the JSON config
    if [ -n "$PACKAGE_NAME" ]; then
        PACKAGES="$PACKAGE_NAME"
    else
        # Get all packages
        PACKAGES=$(jq -r '.tested_packages | keys[]' "$CONFIG_JSON")
        if [ $? -ne 0 ]; then
            print_error "Failed to extract package list from config"
            exit 1
        fi
    fi

    PACKAGE_COUNT=$(echo "$PACKAGES" | wc -l | tr -d ' ')
    print_step "Found $PACKAGE_COUNT package(s) to test"
    echo ""

    # Create artifacts directory
    mkdir -p "$ARTIFACTS_PATH"

    # Test each package
    PACKAGE_INDEX=0
    TOTAL_TESTED=0
    TOTAL_PASSED=0
    TOTAL_FAILED=0
    TOTAL_SKIPPED=0

    for PACKAGE in $PACKAGES; do
        PACKAGE_INDEX=$((PACKAGE_INDEX + 1))
        print_header "Testing Package $PACKAGE_INDEX/$PACKAGE_COUNT: $PACKAGE"

        PACKAGE_ARTIFACTS="$ARTIFACTS_PATH/$PACKAGE"
        mkdir -p "$PACKAGE_ARTIFACTS"

        # Test with patched dependencies first
        print_step "[$PACKAGE_INDEX/$PACKAGE_COUNT] Testing PATCHED (with patches)..."
        
        # Run the test and capture result (don't exit on failure)
        if [ "$SKIP_PATCHES" = false ]; then
            "${INVENIO_TESTRIG_COMMAND}" test "$WORKDIR" "$PACKAGE" \
                --apply-patches || true
        else
            "${INVENIO_TESTRIG_COMMAND}" test "$WORKDIR" "$PACKAGE" || true
        fi
        
        # Check the status from the status file
        PATCHED_STATUS_FILE="$PACKAGE_ARTIFACTS/patched_status.json"
        if [ -f "$PATCHED_STATUS_FILE" ]; then
            PATCHED_STATUS=$(jq -r '.status' "$PATCHED_STATUS_FILE")
        else
            PATCHED_STATUS="unknown"
        fi
        
        # Determine if original tests should run based on patched status and test mode
        TEST_ORIGINAL=false
        case "$TEST_MODE" in
            patched-only)
                # Never test original
                TEST_ORIGINAL=false
                ;;
            stop-on-success)
                # Test only if patched failed
                if [ "$PATCHED_STATUS" = "failed" ]; then
                    TEST_ORIGINAL=true
                fi
                ;;
            run-all)
                # Always test original
                TEST_ORIGINAL=true
                ;;
        esac
        
        # Display patched test results
        if [ "$PATCHED_STATUS" = "success" ]; then
            print_success "[$PACKAGE] Patched tests PASSED"
            TOTAL_PASSED=$((TOTAL_PASSED + 1))
        elif [ "$PATCHED_STATUS" = "skipped" ]; then
            print_warning "[$PACKAGE] Patched tests SKIPPED - no patches to apply"
        else
            print_warning "[$PACKAGE] Patched tests FAILED"
        fi
        echo ""
        
        # Run original tests if needed
        if [ "$TEST_ORIGINAL" = true ]; then
            print_step "[$PACKAGE_INDEX/$PACKAGE_COUNT] Testing ORIGINAL (without patches)..."
            
            "${INVENIO_TESTRIG_COMMAND}" test "$WORKDIR" "$PACKAGE" || true
            
            # Check the status from the status file
            ORIGINAL_STATUS_FILE="$PACKAGE_ARTIFACTS/original_status.json"
            if [ -f "$ORIGINAL_STATUS_FILE" ]; then
                ORIGINAL_STATUS=$(jq -r '.status' "$ORIGINAL_STATUS_FILE")
            else
                ORIGINAL_STATUS="unknown"
            fi
            
            if [ "$ORIGINAL_STATUS" = "success" ]; then
                print_success "[$PACKAGE] Original tests PASSED"
            else
                if [ "$PATCHED_STATUS" != "success" ]; then
                    print_warning "[$PACKAGE] Original tests also FAILED"
                    TOTAL_FAILED=$((TOTAL_FAILED + 1))
                else
                    print_warning "[$PACKAGE] Original tests FAILED"
                fi
            fi
            echo ""
        fi
        
        TOTAL_TESTED=$((TOTAL_TESTED + 1))
    done

    print_header "Test Summary"
    echo "Total packages tested: $TOTAL_TESTED"
    echo "Passed (patched):      $TOTAL_PASSED"
    echo "Failed (patched):      $TOTAL_FAILED"
    echo ""

else
    print_warning "Skipping test step"
    # Only check for artifacts if we're generating a report
    if [ "$SKIP_REPORT" = false ]; then
        if [ ! -d "$ARTIFACTS_PATH" ]; then
            print_error "Artifacts path does not exist: $ARTIFACTS_PATH"
            echo "Cannot generate report without test artifacts. Either run tests first or use --skip-report."
            exit 1
        fi
    fi
    echo ""
fi

################################################################################
# STEP 3: Generate report
################################################################################
if [ "$SKIP_REPORT" = false ]; then
    print_header "STEP 3: Generate Report"
    print_step "Generating test report from artifacts..."

    # Remove report directory if it exists
    if [ -d "$REPORT_PATH" ]; then
        print_warning "Report path already exists, removing: $REPORT_PATH"
        rm -rf "$REPORT_PATH"
    fi

    "${INVENIO_TESTRIG_COMMAND}" report "$WORKDIR" "$REPORT_PATH" --completed

    print_success "Report generated: $REPORT_PATH/index.html"
    
    # Copy artifacts to report directory
    print_step "Copying artifacts to report directory..."
    mkdir -p "$REPORT_PATH/artifacts"
    if [ -d "$ARTIFACTS_PATH" ]; then
        # Copy all package directories from artifacts to report
        for package_dir in "$ARTIFACTS_PATH"/*; do
            if [ -d "$package_dir" ] && [[ "$(basename "$package_dir")" != .working* ]]; then
                package_name=$(basename "$package_dir")
                cp -r "$package_dir" "$REPORT_PATH/artifacts/$package_name"
            fi
        done
        print_success "Artifacts copied to: $REPORT_PATH"
    fi
    echo ""
    
    # Try to open the report in browser (works on macOS, Linux with xdg-open)
    if command -v open &> /dev/null; then
        echo "Opening report in browser..."
        open "$REPORT_PATH/index.html"
    elif command -v xdg-open &> /dev/null; then
        echo "Opening report in browser..."
        xdg-open "$REPORT_PATH/index.html"
    else
        echo "Open the report manually: file://$(pwd)/$REPORT_PATH/index.html"
    fi
else
    print_warning "Skipping report generation"
    echo ""
fi

################################################################################
# Completion
################################################################################
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))
MINUTES=$((DURATION / 60))
SECONDS=$((DURATION % 60))

print_header "Workflow Complete! 🎉"
echo "Total time: ${MINUTES}m ${SECONDS}s"
echo ""
echo "Results in: $WORKDIR"
echo "  Config:     $CONFIG_JSON"
echo "  Repos:      $CLONE_PATH"
echo "  Artifacts:  $ARTIFACTS_PATH"
echo "  Report:     $REPORT_PATH/index.html"
echo ""

print_success "All done!"
