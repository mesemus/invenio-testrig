# invenio-testrig

This repository provides tools for verifying patches for invenio libraries.

It does not run a repository itself at this point, pytests are run for all influenced invenio packages.

## Usage

0. Fork this repository to your own GitHub account.

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-github-account>/invenio-testrig.git
   ```

2. Switch to a new branch for your changes. The verification workflow creates a lots of commits, so it's best to keep your changes isolated.

   ```bash
   git switch -c my-bugfix-verification
   ```

3. Edit the `config.json5` file to specify your patches:

    ```json
    {
         "repositories": [
            {
                "base_url": "https://github.com/inveniosoftware",
                "branch": "",
                "package-regexes": ["invenio-.*"],
                "exclude-package-regexes": ["invenio-xrootd", "invenio-swh"]
            }
         ],
         "patches": {
             "invenio-db": {  // <-- do not forget to change this to the name of the package
                "git": "https://github.com/oarepo/invenio-db.git",
                "branch": "fix-uow"
             }
         }
    }
    ```

    The `patches` section contains the patches to apply. The `repositories` section specifies where to find the original packages.

4. Commit and push your changes to your fork.

5. Go to the Actions tab and start the workflow manually:

   - Click on the "Verify Invenio Patches" workflow.
   - Click "Run workflow".
   - **Select the correct branch.**
   - Optionally, configure the following inputs:
     - **Config file**: Path to the configuration file (default: `config.json5`)
     - **Continue from previous run**: If enabled, the workflow will continue from the most recent run, skipping packages that were already successfully tested.
     - **Verbose pytest**: If enabled, pytest will run with verbose output (-vv -s) and caching will be disabled. Use this if tests deadlock to see output in real-time.

   ![Workflow Configuration](docs/run_workflow.png)
   
   **Note:** Test name, packages to test, test timeout, and whether to run original tests are configured in the config file.

6. Wait for the workflow to finish.

7. Navigate to the [generated report](./reports/reports.md).

## How it works

The CI pipeline performs the following steps:

1. **Extract packages**: Clone the `github.com/zenodo/zenodo-rdm` repository and extract all `invenio-*` packages from `uv.lock`. The package list is stored as an output for use in the subsequent matrix build steps.

2. **Test each package** (runs in parallel as a matrix build):
   a. **Clone the package**:
      - If the package is listed in the `patches` section of `config.json5`, clone the specified repository and branch.
      - Otherwise, clone the package from the repository specified in the `repositories` section.
   b. **Set up environment**: Create a virtual environment using `uv --seed`.
   c. **Apply patches**: For each module listed in the `patches` section of `config.json5` that is installed in the virtual environment, install the patched version. If no patches apply, skip to step e.
   d. **Run tests with patches**: Execute the test suite using the `run-tests.sh` script.
   e. **Run original tests (if needed)**: If the patched tests fail and "Run original tests" is enabled, clone the original package from the configured repository and run its tests.
   f. **Compare results**: Compare test results before and after applying patches. Store test outputs and diffs as artifacts.

3. **Generate report**: Create a summary report of all tested packages, indicating which patches fixed issues, which introduced regressions, and which had no effect.
