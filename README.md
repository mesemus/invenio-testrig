# Invenio-Testrig

Invenio-testrig eliminates the fear of breaking InvenioRDM repositories with your contributions.

It allows you to test your changes across your contribution, affected packages, and inside a running repository[*] in a safe and automated way, either on GitHub or locally.

[*] Work in progress - end-to-end testing will be integrated in the upcoming weeks.

## Warning

The repository has not yet been moved to the inveniosoftware organization. Until the migration is complete, please modify the commands below:

- Replace `inveniosoftware/invenio-testrig` with `oarepo/invenio-testrig`
- Replace `uvx invenio-testrig` with `uvx --from git+https://github.com/oarepo/invenio-testrig invenio-testrig`

These modifications will no longer be necessary after the migration to the inveniosoftware organization.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Task: Contributing to Invenio Packages](#task-contributing-to-invenio-packages)
  - [Task: Testing RDM Repository](#task-testing-rdm-repository)
- [What Happens When Testrig is Run](#what-happens-when-testrig-is-run)
- [How to Reference Patches](#how-to-reference-patches)
- [Advanced](#advanced)
  - [Config File](#config-file)
  - [Running the Testrig Locally](#running-the-testrig-locally)

## Prerequisites

The `invenio-testrig` tool requires the `gh` and `uv` commands to be available on your system. You can install them from:
- GitHub CLI: https://cli.github.com/
- uv: https://docs.astral.sh/uv/getting-started/installation/

## Usage

### Task: Contributing to Invenio Packages

When contributing to an Invenio package (e.g., `invenio-records-resources`), you need to ensure that:

- Tests pass in your modified module
- Tests pass in dependent packages (e.g., `invenio-rdm-records`)
- Your contribution doesn't break the running repository

#### Running the tests on GitHub

To set things up, create a fork of the `inveniosoftware/invenio-testrig` repository and add an empty `gh-pages` branch. You can do this manually or use the invenio-testrig CLI:

```bash
uvx invenio-testrig github [--target org/repository] [org/package#pr_number]...
```

If you skip the `--target` argument, the repository will be forked into your GitHub account under the name `invenio-testrig`. 

If you specify a list of patches in the command, it will automatically start a workflow run with these patches. Otherwise, you can start the workflow manually from the Actions tab in GitHub and specify the patches there.

The command will attempt to open a browser window with the workflow run.

If the repository already exists, the command will update it to match the original `inveniosoftware/invenio-testrig` repository.

#### Advanced Configuration

In some cases, you may want a more customized configuration for your tests—for example, testing your patch not only on Invenio packages but also on your own extensions. In this case, copy the `invenio_testrig/default_config.yaml` file to `config.yaml` (in the root of the cloned repository) and customize it. See the [Config File](#config-file) section below for more details.

### Task: Testing RDM Repository

When preparing to release a new version of your repository, you need to ensure that all frozen dependencies work together correctly and that no tests are broken.

#### How to Set Up

Create a `.github/workflows/test_repository.yml` workflow file in the source code of your InvenioRDM repository:

```yaml
name: Repository test

on:
    workflow_dispatch:

permissions:
    contents: write # Required for pushing reports to the repository
    id-token: write # Required for publishing to GitHub Pages using actions/upload-pages-artifact
    pages: write # Required for publishing to GitHub Pages using actions/upload-pages-artifact

env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

jobs:
    verify-patches:
        uses: oarepo/invenio-testrig/.github/workflows/verify-patches.yml@master
        with:
            name: Repository with ZIP support
            repository: ${{ github.repository }}@${{ github.ref_name }}
            disable-codestyle-checks: true
            python-version: 3.14.2
            # optional stuff
            skip-report: false
            report-repository: ${{ github.repository }}
            report-branch: gh-pages
            report-repository-token: ${{ github.token }}
            ignore-uv-lock: true
```

Also, unless you specify the `skip-report` input, make sure to have a `gh-pages` branch in your repository where the report will be published. You can create it manually:

```bash
cd /tmp
gh repo clone your-org/your-repository
cd your-repository
git checkout --orphan gh-pages
git rm -rf .
git commit --allow-empty -m "Initialize gh-pages branch"
git push origin gh-pages
```

#### How to Run

To run the workflow from the command line, use the `gh` command:

```bash
gh workflow run test_repository.yml [--ref your-branch]
```

Alternatively, go to the GitHub website and run the workflow from the Actions tab.

#### Advanced Configuration

In some cases, you may want a more customized configuration for your tests—for example, testing your patch not only on Invenio packages but also on your own extensions. In this case, copy the `invenio_testrig/default_config.yaml` file into your repository (for example, as `customized_testrig_config.yaml`) and specify the config file name in the workflow inputs.

```yaml
verify-patches:
    uses: oarepo/invenio-testrig/.github/workflows/verify-patches.yml@master
    with:
        name: Repository with ZIP support
        config: customized_testrig_config.yaml
```

See below for more details on the configuration file.

## What Happens When Testrig is Run

When you run invenio-testrig, it performs the following steps:

### 1. Cloning the Seed Repository

The testrig starts by cloning a seed repository that serves as the foundation for testing. The seed repository differs depending on your use case:
- When testing patches (contributions), it uses a plain InvenioRDM repository (by default, Zenodo)
- When testing a repository with frozen dependencies, it uses your own repository with its locked dependencies

### 2. Extracting the List of Packages to Test

From the seed repository, the testrig extracts a list of all Invenio packages that need to be tested. It does this by analyzing the repository's dependencies, either from the `uv.lock` file or by installing and freezing dependencies. You can specify a flag to ignore the `uv.lock` file and always use the latest applicable versions of the packages. This is useful when testing whether your repository is still compatible with the latest dependency versions, even if the `uv.lock` file hasn't been updated yet.

### 3. Mapping Packages to Git Repositories

Each package version is mapped back to its corresponding Git repository and tag. This allows the testrig to clone the exact version of each package's source code that's being used.

### 4. Applying Patches

If you've specified patches (e.g., pull requests or branches), the testrig applies them to the relevant packages. How patches are applied depends on the patch mode:
- In `pinned` mode: patches are applied on top of the versions specified in the seed repository
- In `upstream` mode: patches are applied on top of the latest upstream versions

### 5. Running Tests

The testrig runs the test suite for each affected package. The test mode determines whether it runs tests for both patched and unpatched versions (for comparison) or only for patched versions.

### 6. End-to-End Testing *(Work in Progress)*

Optionally, the testrig can run end-to-end tests on the complete seed repository to verify that everything works together in a real application scenario.

### 7. Generating the Report

Finally, the testrig creates an HTML report summarizing all test results, showing which packages passed or failed, and highlighting any differences between patched and unpatched versions.

## How to Reference Patches

The following formats are supported for patches and references to Git repositories:

**Repositories:**

- org/package
- org/package@branch
- https://github.com/org/repo
- https://github.com/org/repo/tree/branch-name

**Pull Requests:**

- org/package#pr_number
- org/package@branch[base]
- https://github.com/org/repo/pull/123

**Pip-installed GitHub references** (for repositories, not pull requests) are also supported:

- https://github.com/inveniosoftware/invenio-records-resources?branch=fix-read-many#c6b973a14802e2a7f73100ab4e32cb0c36bd4672
- https://github.com/inveniosoftware/invenio-swh?rev=v0.13.4#828a3a415cf8e725c369939832b61281c44aec40

## Advanced

### Config File

The [config file](./invenio_testrig/default_config.yaml) consists of several parts:

#### 1. seed_repository

Configuration for the seed InvenioRDM repository used as the foundation for testing. This repository is cloned and installed (using `uv sync`) to extract dependencies and optionally run end-to-end tests.

**Properties:**

- **git** (required) - Git reference to the seed repository in the format `org/repo@branch`. This repository is used to:
  1. Extract dependencies matching the GitHub filters—these packages will be tested
  2. Run end-to-end tests (if E2E configuration is provided)
  
  Default: `zenodo/zenodo-rdm@master`

- **e2e** (optional) - Git reference to a repository containing an end-to-end test library/configuration. If the seed repository doesn't have an `e2e` directory, it will be copied from this package. If not provided, only unit tests will run (no end-to-end tests).
  
  Example: `oarepo/invenio-e2e@log-xhr`

**Example:**
```yaml
seed_repository:
  git: zenodo/zenodo-rdm@master
  e2e: oarepo/invenio-e2e@log-xhr
```

#### 2. github

List of GitHub organization configurations that define how to map tested Python packages to their GitHub repository, which packages to test, and how to test them. Each organization configuration acts as a filter and test specification for packages found in the seed repository's dependencies.

**Note:** The same organization can appear multiple times with different configurations (e.g., different branch configurations or regex patterns).

**Properties for each organization entry:**

- **org** (required) - GitHub organization name. Package names that match the include/exclude patterns will be mapped to repositories in this organization. For example, if `org` is `inveniosoftware`, the package `invenio-records-resources` will be mapped to the repository `inveniosoftware/invenio-records-resources`.

- **include** (optional) - List of regular expression patterns to filter packages for testing. Only packages matching at least one pattern will be tested.
  
  Example: `["invenio-.*"]` matches all packages starting with `invenio-`

- **exclude** (optional) - List of package names to exclude from testing, even if they match the include patterns. Useful for packages that are known to be incompatible or don't need testing.
  
  Example: `["invenio-xrootd", "invenio-swh"]`

- **test** (required) - A command with arguments to run for packages matching this configuration. Typically this is `["./run-tests.sh"]` for Invenio libraries.

- **extras** (optional) - List of extras to install for tested packages matching this configuration. This is a union of extras across all packages - if an extra doesn't exist for a specific package, it will be silently ignored.
  
  Example: `["tests", "opensearch2", "postgresql"]`

- **freeze** (optional) - List of version constraints (in pip format) to apply when resolving dependencies for tested packages. If specified, these packages will be reinstalled with the specified version constraints before running the tests.
  
  Example: `["setuptools<82.0.0"]` ensures setuptools version stays below 82.0.0

**Example:**

```yaml
github:
  - org: "inveniosoftware"
    include: 
      - "invenio-.*"
    exclude:
      - "invenio-xrootd"
      - "invenio-swh"
    test: 
      - ./run-tests.sh
    extras:
      - tests
      - opensearch2
      - postgresql
      - admin
    freeze:
      - setuptools<82.0.0
  
  - org: "oarepo"
    include:
      - "oarepo-.*"
    test:
      - ./run.sh
      - test
    extras:
      - tests
```

##### Same Prefix for Multiple Organizations

Sometimes the same prefix is used for multiple organizations. For example, the `invenio-` prefix is used for packages in both `inveniosoftware` and `CERNDocumentServer` (which has a package called `invenio-cern-sync`). In this case, specify multiple GitHub organizations and adjust the include/exclude patterns accordingly. The first matching organization will be used for each package.

```yaml
github:
  - org: "CERNDocumentServer"
    include: 
      - "invenio-cern-sync"
    test: 
      - ./run-tests.sh
    extras:
      - tests
      - opensearch2
      - postgresql
      - admin
    freeze:
      - setuptools<82.0.0

  - org: "inveniosoftware"
    ... original configuration here
```

This is an example; `invenio-cern-sync` and `invenio-curations` are already present in the default configuration.

### Running the Testrig Locally

If you prefer to run tests on your local machine instead of using GitHub workflows:

First, prepare the testrig with your patch(es):

```bash
uvx invenio-testrig setup --patch-mode upstream --patch org/package#pr_number
```

This creates a `workdir` folder in the current directory. To test a package, run:

```bash
uvx invenio-testrig test --apply-patches workdir <package-name>
```

To compare with unpatched results, run without the `--apply-patches` flag:

```bash
uvx invenio-testrig test workdir <package-name>
```

If you need to update the setup, please remove the workdir manually and run the setup command again:

```bash
rm -rf workdir
uvx invenio-testrig setup ...
```