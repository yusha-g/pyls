# from argparse import ArgumentError

# class ArgumentParser:
#     def _check_value(self, action, value):
#         # converted value must be one of the choices (if specified)
#         if action.choices is not None and value not in action.choices:
#             args = {'value': value,
#                     'choices': ', '.join(map(repr, action.choices))}
#             msg = _('invalid choice: %(value)r (choose from %(choices)s)')
#             raise ArgumentError(action, msg % args)

def add_args(parser):

    parser.add_argument(
        "--all", "-A", 
        help="List all directories and files.", 
        action="store_true"
    )
    parser.add_argument(
        "--long", "-l",
        help="List additional information",
        action="store_true"
    )
    parser.add_argument(
        "--reverse", "-r",
        help="Reverse listing",
        action="store_true"
    )
    parser.add_argument(
        "--time","-t",
        help="Sort by time-modified",
        action="store_true"
    )

    parser.add_argument(
        "--filter",
        help="Filter by type of item. Either file or dir",
        choices=['dir','file'],
        action="store"
    )

    # if no arguments are given, use None
    parser.add_argument(
        "file_path",
        help="The path to the directory or file to list",
        type=str,
        nargs="?",
        default=None
    )