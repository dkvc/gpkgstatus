from argparse import ArgumentParser
from termcolor import colored

def print_update_info(update: dict, status_color: str):
    print(colored(f"Update ID: {update['updateid']}", status_color))
    print(colored(f"Package Name: {update['title']}", status_color))
    print(colored(f"Status: {update['status']}", status_color))
    print("------------------------------")


if __name__ == "__main__":
    parser = ArgumentParser(
        prog = "gpkgstatus",
        description= "Get Current Package Status from Fedora Updates System",
        usage = "gpkgstatus [-dv DISTRO_VERSION] NAME"
    )

    parser.add_argument('name', help='Name of the package')
    parser.add_argument('-dv', '--distro-version', help='Checks package status for corresponding Fedora version')
    parser.add_argument('-f', '--force', help="Sync cached info with Fedora Updates System", action='store_true')
    parser.add_argument('-v', '--version', help='Returns gpkgstatus version', action='version', version='0.4 (beta)')
    args = parser.parse_args()
    
    #main(args)