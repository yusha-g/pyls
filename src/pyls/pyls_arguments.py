def add_args(parser):

    parser.add_argument(
        "--all", "-A", help="List all directories and files.", action="store_true"
    )
    parser.add_argument(
        "--long", "-l", help="List additional information", action="store_true"
    )
    parser.add_argument("--reverse", "-r", help="Reverse listing", action="store_true")
    parser.add_argument(
        "--time", "-t", help="Sort by time-modified", action="store_true"
    )

    parser.add_argument(
        "--filter",
        help="Filter by type of item. Either file or dir",
        choices=["dir", "file"],
        action="store",
    )

    # if no arguments are given, use None
    parser.add_argument(
        "file_path",
        help="The path to the directory or file to list",
        type=str,
        nargs="?",
        default=None,
    )

    parser.add_argument(
        "-h",
        action="store_true"
    )
