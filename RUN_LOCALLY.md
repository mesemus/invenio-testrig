# Running Tests Locally with run-locally.sh

The `run-locally.sh` script orchestrates the complete invenio-testrig workflow, running all commands in the correct order with sensible defaults. All output files and directories are organized inside a single working directory.

## Quick Start

```bash
# Run with default settings (creates ./workdir/)
./run-locally.sh config_test.yaml

# Run with custom working directory
./run-locally.sh config_test.yaml --workdir ./my-test-run

# Test only a specific package
./run-locally.sh config_test.yaml --package invenio-records-resources

# Use different Python version
./run-locally.sh config_test.yaml --python python3.11
```

## What It Does

The script automatically runs the following workflow:

1. **Initialize** - Converts YAML config to JSON (named after the YAML file) and resolves git references
2. **Collect** - Clones the main repository and collects dependencies
3. **Filter** - Filters packages based on GitHub patterns
4. **Clone** - Clones all package repositories with patches
5. **Test** - Tests each package (with patches and if that fails, without patches)
6. **Report** - Generates an HTML report with results

All output is isolated in a single working directory for easy cleanup and organization.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `--workdir <path>` | Working directory (must be non-existing or empty) | `./workdir` |
| `--python <version>` | Python version to use | `python3.12` |
| `--uv <path>` | Path to uv executable | `uv` |
| `--package <name>` | Test only specific package | (all packages) |
| `--clear-cache` | Clear git cache before cloning | (not set) |
| `--skip-clone` | Skip cloning (use existing repos) | (not set) |
| `--skip-tests` | Skip running tests | (not set) |
| `--skip-report` | Skip report generation | (not set) |
| `--help` | Show help message | - |

**Note:** The config JSON is automatically named after the input YAML file. For example, `config_test.yaml` becomes `config_test.json` in the working directory.

## Skip Options for Development

When developing or debugging, you can skip certain steps:

```bash
# Skip cloning if you already have repos cloned
./run-locally.sh config_test.yaml --skip-clone

# Skip tests and just generate a report from existing artifacts
./run-locally.sh config_test.yaml --skip-clone --skip-tests

# Skip report generation
./run-locally.sh config_test.yaml --skip-report
```

## Examples

### Full workflow with custom settings

```bash
./run-locally.sh config_test.yaml \
  --workdir /tmp/test-run \
  --python python3.11 \
  --clear-cache
```

### Test a single package

```bash
./run-locally.sh config_test.yaml \
  --workdir ./preview-test \
  --package invenio-previewer
```

### Multiple test runs with different configs

```bash
# Each run isolated in its own directory
./run-locally.sh config_test.yaml --workdir ./run1
./run-locally.sh config_prod.yaml --workdir ./run2
./run-locally.sh config_dev.yaml --workdir ./run3
```

## Output

The script creates the following directory structure:

```plaintext
workdir/                         # Working directory (configurable)
├── config_test.json             # Resolved JSON configuration (named after YAML)
├── repos/                       # Cloned repositories
│   ├── repo/                    # Main repository
│   ├── invenio-e2e/            # E2E test repository (if configured)
│   ├── packages/               # Unpatched dependencies
│   │   └── package-name/
│   └── patched/                # Patched dependencies
│       └── package-name/
├── artifacts/                   # Test artifacts
│   └── package-name/
│       ├── original_log.log
│       ├── original_status.json
│       ├── original_freeze.txt
│       ├── patched_log.log
│       ├── patched_status.json
│       └── patched_freeze.txt
└── report/                      # HTML report
    └── index.html
```

All files are self-contained in the working directory for easy cleanup:

```bash
# Remove all test artifacts
rm -rf ./workdir
```

## Prerequisites

- `invenio-testrig` must be installed (`pip install -e .`)
- `uv` must be available in PATH (or specify with `--uv`)
- `python3` (or your specified version) must be available
- `gh` CLI must be configured for GitHub API access

## Troubleshooting

### Working directory already exists and is not empty

```bash
# Remove the old working directory
rm -rf ./workdir

# Or use a different directory
./run-locally.sh config_test.yaml --workdir ./my-new-workdir
```

### Git cache issues

```bash
./run-locally.sh config_test.yaml --clear-cache
```
