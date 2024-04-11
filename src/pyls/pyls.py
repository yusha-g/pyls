#!/usr/bin/env python3

import argparse
import json
from pathlib import Path
from typing import Optional

from custom_exceptions import InvalidPath
from item import Item
from pyls_arguments import add_args


def get_current_file_content_old(
    item: Item, file_path: Optional[str] = None
) -> Item | None:
    """
    Args:
        item (Item): Structure containing file.
        file_path (str): Name of file to be accessed.
    Return:
        Contents of item specified in file path.
        If no item matches, None is returned.
    """
    if item.name == file_path or file_path is None:
        return item
    for sub_item in item.contents:
        current_item = get_current_file_content_old(sub_item, file_path)
        if current_item is not None:
            return current_item
    return None

# TODO: simplify the below code
def get_current_file_content(
    item: Item, file_path: Optional[list] = None
):
    if file_path is None:
        return item
    if file_path[0] == "." and len(file_path) == 1:
        return item
    if file_path[0] == "." and len(file_path)>1:
        file_path[0] = "interpreter"

    if file_path[0] == item.name:
        if len(file_path) == 1:
            return item
        else:
            for sub_item in item.contents:
                current_item = get_current_file_content(sub_item, file_path[1:])
                if current_item is not None:
                    return current_item
    for sub_item in item.contents:
            current_item = get_current_file_content(sub_item, file_path)
            if current_item is not None:
                    return current_item
    return None
    

if __name__ == "__main__":
    structure_path = Path(__file__).parent / "json" / "structure.json"
    with open(structure_path) as fh:
        file_structure = json.load(fh)
    item = Item(**file_structure)

    parser = argparse.ArgumentParser()
    pyls_parser = parser.add_argument_group("pyls flags")
    add_args(pyls_parser)

    args = parser.parse_args()

    # TODO: this is ugly. make it prettier.
    # extract file name if file_path is specified, else just assign it None
    file_name = None
    if args.file_path:
        file_name = args.file_path.split("/")
    
    # breakpoint()
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

    if args.time:
        item_list = item.sort_by_time(item_list)
    if args.reverse:
        item_list = item.reverse_items(item_list)
    if args.long:
        item.long_list_items(item_list)
    else:
        item.display(item_list)
