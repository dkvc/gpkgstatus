# gpkgstatus

## Get Current Package Status from Fedora Updates System

This program is a command-line tool for checking the status of packages on bodhi.fedoraproject.org.
It allows you to search for a specific package and get information about its current status, including the update ID, package name, and status.

## Current Build Status

[![Python Tests](https://github.com/dkvc/gpkgstatus/actions/workflows/python-test.yml/badge.svg?branch=main)](https://github.com/dkvc/gpkgstatus/actions/workflows/python-test.yml)
[![CodeQL](https://github.com/dkvc/gpkgstatus/actions/workflows/codeql.yml/badge.svg?branch=main)](https://github.com/dkvc/gpkgstatus/actions/workflows/codeql.yml)

## Current Release Status

[![Last Pre-Release Date](https://img.shields.io/github/release-date-pre/dkvc/gpkgstatus?label=Preview%20Release&)](https://github.com/dkvc/gpkgstatus/releases)
[![Last Release Date](https://img.shields.io/github/release-date/dkvc/gpkgstatus?label=Stable%20Release&)](https://github.com/dkvc/gpkgstatus/releases)

## Features

- Search for a specific package and get its status information.
- Option to specify a distro version to check for a specific version of the package.
- Caches the previous search results for 60 minutes (1 hour) to avoid DDoS.
- Allows you to force a new search, bypassing the cache.
- Displays the information in a user-friendly format.

## Installation

1. Download the executable file for your operating system from the ![Releases](https://github.com/dkvc/gpkgstatus/releases) section of this repository.
2. Make sure the file is executable (e.g. chmod +x gpkgstatus on Linux).

**Note:** If you want to run the file anywhere, move the file to a directory in your system's PATH (usually /usr/local/bin)

## Usage

The program can be used by running the executable file with the following command:

```bash
$ gpkgstatus -h

usage: gpkgstatus [-dv DISTRO_VERSION] [-f] name

Get Current Package Status from Fedora Updates System

positional arguments:
  name                  Name of the package

options:
  -h, --help            show this help message and exit
  -d DISTRO_VERSION, --distro-version DISTRO_VERSION
                        Checks package status for corresponding Fedora version
  -f, --force           Sync cached info with Fedora Updates System
  -v, --version         Returns gpkgstatus version
```

## Contributing

You are welcome to contribute to this project.
