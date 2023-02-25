# gpkgstatus

## Get Current Package Status from Fedora Updates System

This program is a command-line tool for checking the status of packages on bodhi.fedoraproject.org.
It allows you to search for a specific package and get information about its current status, including the update ID, package name, and status.

[![Code Style](https://img.shields.io/badge/code%20style-black-000000)](https://github.com/psf/black)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/PyCQA/pylint)

## Current Build Status

[![Python Tests](https://github.com/dkvc/gpkgstatus/actions/workflows/python-test.yml/badge.svg?branch=main)](https://github.com/dkvc/gpkgstatus/actions/workflows/python-test.yml)
[![CodeQL](https://github.com/dkvc/gpkgstatus/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/dkvc/gpkgstatus/actions/workflows/codeql.yml)

## Current PyPI Status

[![PyPI version](https://img.shields.io/pypi/v/gpkgstatus)](https://pypi.org/project/gpkgstatus/)
[![Dep Status](https://img.shields.io/librariesio/release/pypi/gpkgstatus)](https://pypi.org/project/gpkgstatus/)
[![Python support](https://img.shields.io/pypi/pyversions/gpkgstatus)](https://pypi.org/project/gpkgstatus/)

## Current Release Status

[![Last Pre-Release Date](https://img.shields.io/github/release-date-pre/dkvc/gpkgstatus?label=Github%20Release%20(Preview)&)](https://github.com/dkvc/gpkgstatus/releases)
[![Last Release Date](https://img.shields.io/github/release-date/dkvc/gpkgstatus?label=Github%20Release&)](https://github.com/dkvc/gpkgstatus/releases)

## Features

- Search for a specific package and get its status information.
- Option to specify a distro version to check for a specific version of the package.
- Caches the previous search results for 60 minutes (1 hour) to avoid DDoS.
- Allows you to force a new search, bypassing the cache.
- Displays the information in a user-friendly format.

## Installation

There are two ways of installing gpgkstatus:

1. **Using pip:** You can use `pip install gpkgstatus` and restart your terminal. Now you can use it!
2. **(Unsupported) Using executables from Github:** You can download executable from [Releases](https://github.com/dkvc/gpkgstatus) and use it directly. Make sure to set it as executable on Linux.

**Note:** If you want to run the file anywhere when using executable from Github, move the file to a directory in your system's PATH (usually /usr/local/bin)

### Why Way 2 is unsupported?

You have to update executable manually!

## Usage

The program can be used by running the executable file with the following command:

```console
$ gpkgstatus -h

usage: gpkgstatus [-h] [-f] [-l LIMIT] [--moreinfo] [-n NAME] [--noconfig] [-r RELEASE] [-v] [--version]

Get Current Package Status from Fedora Updates System

options:
  -h, --help            show this help message and exit
  -f, --force           Sync cached info with Fedora Updates System
  -l LIMIT, --limit LIMIT
                        Maximum limit on number of packages shown for package search
  --moreinfo            Verbose (More Info) in Update Info
  -n NAME, --name NAME  Name of the package
  --noconfig            Do not check for config file
  -r RELEASE, --release RELEASE
                        Checks package status for corresponding Fedora release
  -v, --verbose         Enable verbose output
  --version             gpkgstatus version
```

## Contributing

You are welcome to contribute to this project. Make sure to read [Contributing Guidelines](https://github.com/dkvc/gpkgstatus/blob/main/CONTRIBUTING.md). If you have any questions regarding contributing to this project, you can open an issue about it.
