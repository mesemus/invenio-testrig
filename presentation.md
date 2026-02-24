# Invenio-Testrig

## Use cases

### Contributor to Invenio

- Adding contribution to `invenio-records-resources`
- I'll test that tests pass in this module
- I should test that tests pass at least in `invenio-rdm-records`
- I should test that a newly created repository works with my contribution

But: other packages that depend on `invenio-records-resources` may not be tested, and my contribution may break them.

### Repository maintainer

- I want to release a new version of my repository (not a major release, but a minor one)
- I have frozen all dependencies and want to be sure that these exactly work together

### 3-rd party extensions (CESNET use case)

- I have my own extensions (patches) to Invenio core packages and I am keeping them in a local repository/local pypi index
- I want to test that my extensions work with the latest Invenio core packages (patches can be applied and tests work after application of those patches)

## Testrig principles

Invenio-testrig is a tool to automate the actions described in the use cases above. It is based on the following principles:

1. It can be run either on github or locally on developer's machine
2. It is based on configuration file (YAML) that describes the test scenarios

### Config file

The config file consists of a several parts:

1. List of **patches** to apply (optional)
2. **seed InvenioRDM repository** - a reference to github with an InvenioRDM-compatible repository. This repository is used to get a list of packages to test (from the dependencies of the seed repository) and this repository is optionally tested with e2e tests.
3. **repository with e2e test framework** (optional)
4. **patch mode** - a mode that describes how exactly are the patches applied on top of the package versions in the seed repository.
5. **test mode** - a mode that describes how the tests are executed (if both patched and unpatched versions are tested, or only patched, etc.)

### What happens when testrig is run

1. Clone the seed repository
2. Get list of packages to test from the dependencies of the seed repository (uv.lock or install & freeze)
3. Map package versions to git repositories and their tags
4. Apply patches to these packages according to the patch mode and the list of patches in the config file
5. Run tests according to the test mode
6. Optionally, run e2e tests on the seed repository
7. Create an HTML report

## How to run it

### Local workflow

At first, prepare the testrig with the following command:

```bash
uvx invenio-testrig setup --patch <p1> --patch <p2> ...
```

This will create a `workdir` folder in the current directory. To test a package,
run:

```bash
uvx invenio-testrig test [--apply-patches] <package-name>
```

If you specify the `--apply-patches` flag, the patches will be applied to the package
and all libraries on which the package depends before running tests. If you don't specify
it, the tests will be run without applying patches (this is useful to compare results of
patched and unpatched versions).

### Github workflow - contributor

To be able to run the github workflow, you need to have an access to the invenio-testrig
repository (or a clone). Create a new branch and update a config file in the config.yaml.
Then, run the workflow from the Actions tab in github.

Note: we want to provide a more streamlined solution, but we need to agree who should
have the rights to run the testrig.

### Github workflow - repository maintainer

Create your own .git/workflows workflow and put the following content there:

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
            ignore-lock: true
```

Then you can run this workflow from the Actions tab in github.

### Building 3-rd party extensions (CESNET use case)

Use a similar setup as for the repository maintainer. Specify your set of patches
using the `patches: <p1> <p2> ...` input in the workflow and run the invenio-testrig workflow.
It will create a `workdir` artifact. Inside this artifact (.tar.gz) you will find
`cloned_repos/patched` subdirectory where the patched versions of the repositories are
located and exactly these were tested. You can that package these repositories and
upload them to your local pypi index.

## Patch modes

The following patch modes are supported:

- `pinned-overwrite` - a single patch/branch is used in place of any reference to this library
- `pinned-rebase` - the seed repository provides the version of the package. Apply all patches
on top of this version (using cherry-pick).

- `upstream-overwrite` - Use upstream versions of all packages (patched and unpatched). When patching, replace the library with the single patch/branch
- `upstream-rebase` - Use upstream versions of all packages (patched and unpatched). When patching, apply all patches on top of the upstream version (using cherry-pick).

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
