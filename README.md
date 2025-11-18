# invenio-bug-verification

This repository provides tools for verifying bugfixes in Invenio-based applications.

## Usage

0. Fork this repository to your own GitHub account.

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-github-account>/invenio-bug-verification.git
   ```

2. Switch to a new branch for your changes. The verification workflow creates a lots of commits, so it's best to keep your changes isolated.

   ```bash
   git switch -c my-bugfix-verification
   ```

3. Edit the `patches.json` file to specify your patches:

    ```json
    {
         "invenio-db": {
            "url": "https://github.com/oarepo/invenio-db.git",
            "branch": "fix-uow"
         }
    }
    ```

4. Optionally, adjust the `config.json` file to change global parameters.

5. Commit and push your changes to your fork.

6. Go to the Actions tab and start the workflow manually:

   - Click on the "Verify Invenio Patches" workflow.
   - Click "Run workflow".
   - Select the correct branch.
   - Optionally, configure the following inputs:
     - **Name of the verification run**: A descriptive name for this run (used in the report directory name).
     - **Continue from previous run**: If enabled, the workflow will continue from the most recent run, skipping packages that were already successfully tested.
     - **Packages**: Space or comma-separated list of specific packages to test (leave empty to test all packages).
     - **Run original tests**: If enabled, when patched tests fail, the original tests will be run to confirm the failure is due to the patch.
     - **Timeout in minutes**: Maximum time allowed for each test run (0 = GitHub default).
     - **Verbose pytest**: If enabled, pytest will run with verbose output (-vv -s) and caching will be disabled. Use this if tests deadlock to see output in real-time.

7. Wait for the workflow to finish.

8. Navigate to the [generated report](./reports/reports.md).

## How it works

The CI pipeline performs the following steps:

1. **Extract packages**: Clone the `github.com/zenodo/zenodo-rdm` repository and extract all `invenio-*` packages from `uv.lock`. The package list is stored as an output for use in the subsequent matrix build steps.

2. **Test each package** (runs in parallel as a matrix build):
   a. **Clone the package**:
      - If the package is listed in `patches.json`, clone the specified repository and branch.
      - Otherwise, clone the package from `github.com/inveniosoftware`.
   b. **Set up environment**: Create a virtual environment using `uv --seed`.
   c. **Apply patches**: For each module listed in `patches.json` that is installed in the virtual environment, install the patched version. If no patches apply, skip to step e.
   d. **Run tests with patches**: Execute the test suite using the `run-tests.sh` script.
   e. **Run original tests (if needed)**: If the patched tests fail and "Run original tests" is enabled, clone the original package from `inveniosoftware` and run its tests.
   f. **Compare results**: Compare test results before and after applying patches. Store test outputs and diffs as artifacts.

3. **Generate report**: Create a summary report of all tested packages, indicating which patches fixed issues, which introduced regressions, and which had no effect.
