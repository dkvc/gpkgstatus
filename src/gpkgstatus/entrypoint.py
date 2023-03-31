# pylint:disable=all
import os

from termcolor import colored
from gpkgstatus.gpkgstatus import cli


def main():
    if os.name == "nt":
        os.system("color")
        cli()
        input(colored("Press Enter to continue...", "green"))
    else:
        cli()


if __name__ == "__main__":
    main()
