<!-- omit in toc -->
# Contributing to **gpgkstatus**

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

<!-- omit in toc -->
## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Setting Up your Development Environment](#development-setup)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)
  - [Formatting](#formatting)

## Code of Conduct

This project and everyone participating in it is governed by the
[Code of Conduct](https://github.com/dkvc/gpgkstatus/blob/main/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. If you find any behavior that disregards [Code of Conduct](https://github.com/dkvc/gpgkstatus/blob/main/CODE_OF_CONDUCT.md), please report it to project mantainers.

## I Have a Question

Before you ask a question, it is best to search for existing [Issues](https://github.com/dkvc/gpgkstatus/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/dkvc/gpgkstatus/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (python, os, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.

## I Want To Contribute

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](https://dkvc.github.io/gpkgstatus/). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [issues](https://github.com/dkvc/gpgkstatus/issues).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the dependencies and python.s
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/dkvc/gpgkstatus/issues/new).
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be implemented by someone.

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for gpgkstatus, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://dkvc.github.io/gpkgstatus/) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/dkvc/gpgkstatus/issues) in issues to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your enhancement fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature.

### Setting Up your Development Environment

1. Most of the development is done on `docker` or `podman`. You can install [Docker](https://docs.docker.com/get-docker/) or [Podman](https://podman.io/getting-started/installation) from corresponding websites.

2. Using [Dockerfile](https://github.com/dkvc/gpkgstatus/blob/main/.devcontainer/Dockerfile) on repository, you can create a development environment on container.

3. Get started by looking through issues or making an [enhancement](#suggesting-enhancements)! 🎉

### Improving The Documentation

Most of the documentation is generated using [pdoc](https://pdoc.dev/). You can update the docstrings and [pdoc](https://pdoc.dev/) will automatically generate new documentation. You can also make improvements to this file and [README.md](https://github.com/dkvc/gpgkstatus/blob/main/README.md) to make project more welcoming to new users.

## Styleguides

### Commit Messages

Commit messages are made in the format of [Conventional Commits](https://www.conventionalcommits.org/).

Format: `<type>(<scope>): <subject>`

`<scope>` is optional

- `feat`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `refactor`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)

### Formatting

The project code is formatted using linters [pylint](https://github.com/PyCQA/pylint) and [black](https://github.com/psf/black). You are required to format your code in accordance with mentioned linters. You can ignore some warnings if necessary using syntax provided by corresponding linters.

## Attribution

Most of guide was generated using [contributing-gen](https://github.com/bttger/contributing-gen). The list of conventional commit syntax was taken from [semantic-commit-messages.md](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716#file-semantic-commit-messages-md).
