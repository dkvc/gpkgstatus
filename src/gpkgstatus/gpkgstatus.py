from argparse import ArgumentParser

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