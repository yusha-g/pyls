#!/usr/bin/env python3

import argparse
from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Optional

def add_args(parser):
    parser.add_argument(
        "--all", "-A", 
        help="List all directories", 
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
class Item:
    """
    Each Item corresponds to directory/file in the structure.
    If an Item has contents, it is a directory. Otherwise, it's a file.
    """
    def __init__(
        self, 
        name: str, 
        size: int, 
        time_modified: int, 
        permissions: str, 
        contents: Optional[list["Item"]] = None
    ):

        self.name = name
        self.size = size
        self.time_modified = datetime.fromtimestamp(time_modified).strftime("%b %d %H:%M")
        self.permissions = permissions
        self.contents = []
        if contents:
            for sub_items in contents:
                self.contents.append(Item(**sub_items))
    
    def list_items(self, list_all: bool) -> list:
        """
        Args:
            list_all (bool): True if -A is set
        Returns: 
            List of all items in the immediate subdirectory.
            If list_all is True, will include files starting with ".".
        """
        item_list = []
        if list_all:
            for sub_items in self.contents:
                item_list.append(sub_items)
            return item_list

        for sub_items in self.contents:
            if sub_items.name[0] != ".":
                item_list.append(sub_items)
        return item_list
    
    def sort_by_time(self, item_list: list) -> list:
        return sorted(item_list, key=lambda item_time: item.time_modified)
    
    def reverse_items(self, item_list: list) -> list:
        return item_list[::-1]
    
    def long_list_items(self, item_list) -> None:
        self.long_display(item_list)

    def display(self, item_list):
        for item in item_list:
            print(item.name, end=" ")
        print()
    
    def long_display(self, item_list):
        for item in item_list:
            print(
                item.permissions,
                item.size,
                item.time_modified,
                item.name
            )

if __name__ == "__main__":
    structure_path = Path(__file__).parent / "structure.json"
    with open(structure_path) as fh:
        file_structure = json.load(fh)
    item = Item(**file_structure)

    parser = argparse.ArgumentParser()
    
    add_args(parser)

    args = parser.parse_args()

    item_list = item.list_items(args.all)


    """Note: 
    Order of checking the args is important here.
    Example:
        In case reverse is checked before time, 
        sorting by 'time_modified' will nullify the reveseral of items.
    """

    if args.time:
        item_list=item.sort_by_time(item_list)
    if args.reverse:
        item_list=item.reverse_items(item_list)
    if args.long:
        item.long_list_items(item_list)
    else:
        item.display(item_list)
    

