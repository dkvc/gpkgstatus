# pylint:disable=missing-module-docstring
import os

from termcolor import colored
from gpkgstatus.gpkgstatus import cli

if os.name == "nt":
    os.system("color")
    cli()
    input(colored("Press Enter to continue...", "green"))
else:
    cli()
