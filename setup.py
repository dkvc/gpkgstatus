from setuptools import setup

with open('README.md') as readme_file:
    README = readme_file.read()
    
with open('requirements.txt') as req_file:
    REQUIREMENTS = req_file.read().splitlines()

setup(
        name="gpkgstatus",
        version="0.5-beta",
        license="GPL-2.0",
        python_requires=">=3.8",
        author="Dhanush Kovi",
        description="Get Current Package Status from Fedora Updates System",
        long_description=README,
        long_description_content_type="text/markdown",
        url="https://github.com/dkvc/gpkgstatus",
        install_requires=REQUIREMENTS,
)
