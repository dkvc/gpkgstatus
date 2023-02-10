from setuptools import setup, find_packages

with open("README.md") as readme_file:
    README = readme_file.read()

with open("requirements.txt") as req_file:
    REQUIREMENTS = req_file.read().splitlines()

with open("dev-reqs.txt") as req_file:
    DEV_REQS = req_file.read().splitlines()

setup(
    name="gpkgstatus",
    version="1.4.1",
    license="GPL-2.0",
    python_requires=">=3.8",
    author="Dhanush Kovi",
    description="Get Current Package Status from Fedora Updates System",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dkvc/gpkgstatus",
    install_requires=REQUIREMENTS,
    extras_require={
        "dev": DEV_REQS,
    },
    scripts=["bin/gpkgstatus"],
    keywords=[
        "fedora",
        "updates",
        "package",
        "status",
        "fedora-updates",
        "gpkgstatus",
        "bodhi",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
