# Invenio-Testrig

Invenio-testrig is designed to make your fear of breaking InvenioRDM repositories with your contributions a thing of the past.

It allows you to test your changes on your contribution, affected packages and a running repository[*] in a safe and automated way, either locally or on GitHub.

[*] Work in progress - end-to-end testing will be integrated in the upcoming weeks.

## Use cases

### Contributor to Invenio

- Adding a contribution to `invenio-records-resources`
- I'll test that tests pass in this module
- I should test that tests pass at least in `invenio-rdm-records`
- I should test that a newly created repository works with my contribution

But: other packages that depend on `invenio-records-resources` may not be tested, and my contribution may break them.

### Repository maintainer

- I want to release a new version of my repository (not a major release, but a minor one)
- I have frozen all dependencies and want to be sure that all of these work together correctly and no tests are broken

### Third-party extensions (CESNET use case)

- I have my own extensions (patches) to Invenio core packages and I am keeping them in a local repository/local PyPI index
- I want to test that my extensions work with the latest Invenio core packages (that patches can be applied and that tests pass after applying them)

## Testrig principles

Invenio-testrig is a tool to automate the actions described in the use cases above. It is based on the following principles:

1. It can be run either on GitHub or locally on a developer's machine
2. It is based on a configuration file (YAML) that describes the test scenarios

### Config file

[The config file consists](./invenio_testrig/default_config.yaml) of several parts:

1. List of **patches** to apply (optional)
2. **github url of a seed InvenioRDM repository** - a reference to a GitHub repository with an InvenioRDM-compatible repository. This repository is used to get a list of packages to test (from the dependencies of the seed repository) and this repository is optionally tested with end-to-end tests. At the moment, this is Zenodo, but we might want to change it so that we can run e2e tests.
3. **github url of a git repository with end-to-end test framework** (optional)
4. **Patch mode** - a mode that describes how the patches are applied on top of the package versions in the seed repository.
5. **Test mode** - a mode that describes how the tests are executed (whether both patched and unpatched versions are tested, or only patched, etc.)

When testrig is run, it will read the config file, overwrite some parts with optional user input (e.g. from GitHub workflow inputs) and then execute the test scenarios according to the config file.

### What happens when testrig is run

1. Clone the seed repository
2. Get the list of packages to test from the dependencies of the seed repository (uv.lock or install & freeze)
3. Map package versions to Git repositories and their tags
4. Apply patches to these packages according to the patch mode and the provided list of patches
5. Run tests according to the test mode
6. Optionally, run end-to-end tests on the seed repository (**Work in progress**)
7. Create an HTML report

## How to run it

### Local workflow

At first, prepare the testrig with the following command:

```bash
uvx invenio-testrig setup --patch-mode <patch-mode> --patch <p1> --patch <p2> ...
```

This will create a `workdir` folder in the current directory. To test a package, run:

```bash
uvx invenio-testrig test [--apply-patches] workdir <package-name>
```

If you specify the `--apply-patches` flag, the patches will be applied to the package and all libraries on which the package depends before running tests. If you don't specify it, the tests will be run without applying patches (this is useful to compare results of patched and unpatched versions).

### GitHub workflow - contributor

To run your changes on a GitHub workflow-based testrig

#### You **can** run workflows in inveniosoftware/invenio-testrig repository

Go to the Actions tab in the invenio-testrig repository and run the workflow from there. Enter your patches and additional info and start the workflow. Take a walk and after 30 minutes or so, check the results.

#### You **can not** run workflows in inveniosoftware/invenio-testrig repository

Fork the invenio-testrig repository, and then do the same as above. Do not forget to take a walk.

### GitHub workflow - repository maintainer

Create your own `.github/workflows` workflow file and add the following content:

```yaml
name: Testing

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

Then you can run this workflow from the Actions tab in GitHub and optionally the report will be published to GitHub Pages in the selected repository and branch.

### Building third-party extensions (CESNET use case)

Use a similar setup as for the repository maintainer. Specify your set of patches using the `patches: <p1> <p2> ...` input in the workflow and run the invenio-testrig workflow.

It will create a `workdir` artifact. Inside this artifact (.tar.gz) you will find a `cloned_repos/patched` subdirectory where the patched versions of the repositories are located and these are exactly what was tested. You can then package these repositories and upload them to your local PyPI index.

## Patch modes

The following patch modes are supported:

- `pinned-overwrite` - a single patch/branch replaces any reference to this library
- `pinned-rebase` - the seed repository provides the version of the package. All patches are applied on top of this version (using cherry-pick).

- `upstream-overwrite` - use upstream versions of all packages (patched and unpatched). When patching, replace the library with the single patch/branch
- `upstream-rebase` - use upstream versions of all packages (patched and unpatched). When patching, apply all patches on top of the upstream version (using cherry-pick).

The first two modes are useful when you want to test your patches on top of your own repository.

The second two modes are useful when you want to test your patches on top of the latest upstream versions of the packages.

## How to reference patches

The following formats are supported for patches and reference to git repositories:

Repositories:

- org/package
- org/package@branch
- https://github.com/org/repo
- https://github.com/org/repo/tree/branch-name

Pull requests:

- org/package#pr_number
- org/package@branch[base]
- https://github.com/org/repo/pull/123

Also pip-installed github references for repositories (not pull requests) are supported:

- https://github.com/inveniosoftware/invenio-records-resources?branch=fix-read-many#c6b973a14802e2a7f73100ab4e32cb0c36bd4672
- https://github.com/inveniosoftware/invenio-swh?rev=v0.13.4#828a3a415cf8e725c369939832b61281c44aec40
