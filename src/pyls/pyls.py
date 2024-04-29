#!/usr/bin/env python3

import argparse
import json
from pathlib import Path
from typing import Optional

from . import InvalidPath, Item, add_args


# TODO: simplify the below code
def get_current_file_content(item: Item, file_path: Optional[list] = None):

    if file_path is None:
        # no file path provided
        return item

    if file_path[0] == ".":
        if len(file_path) == 1:
            # refers to current directory
            return item
        # relative path - "." means outermost
        file_path = file_path[1:]
    # search for item recursively inside the subdirs
    for sub_item in item.contents:
        if sub_item.name == file_path[0]:
            # current sub_item is the left-most directory in the path
            if len(file_path) == 1:
                # file_path only contains name of dir / file
                return sub_item
            current_item = get_current_file_content(sub_item, file_path[1:])
            if current_item:
                # gotcha
                return current_item
    return None


def main():
    structure_path = Path(__file__).parent / "json" / "structure.json"
    with open(structure_path) as fh:
        file_structure = json.load(fh)
    item = Item(**file_structure)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--help", action="help")
    pyls_parser = parser.add_argument_group("pyls flags")
    add_args(pyls_parser)

    args = parser.parse_args()

    # extract file name if file_path is specified, else just assign it None
    # strip trailing slashes if present
    file_name = args.file_path.rstrip("/").split("/") if args.file_path else None

    current_item = get_current_file_content(item, file_name)
    if current_item:
        item_list = current_item.list_items(args.all, filter=args.filter)
    else:
        assert file_name is not None
        raise InvalidPath(file_name)

    """Note: 
    Order of checking the args is important here.
    Example:
        In case 'reverse' is checked before 'time', 
        sorting by 'time_modified' will nullify the reveseral of items.
    """
    if args.h:
        item.make_human_readable(item_list)
    if args.time:
        item_list = item.sort_by_time(item_list)
    if args.reverse:
        item_list = item.reverse_items(item_list)
    if args.long:
        dsp_str = item.long_list_items(item_list)
    else:
        dsp_str = item.display(item_list)
    print(dsp_str)
