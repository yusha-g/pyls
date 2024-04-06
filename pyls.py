#!/usr/bin/env python3

import argparse
from datetime import datetime
import json
from pathlib import Path
import sys
from typing import Optional



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
        self.time_modified = datetime.fromtimestamp(time_modified).strftime("%b %d %H %M")
        self.permissions = permissions
        self.contents = []
        if contents:
            for sub_items in contents:
                self.contents.append(Item(**sub_items))
    
    def list_items(self) -> None:
        """
        Lists all items in the immediate subdirectory (excluding the once starting with ".").
        """
        for sub_items in self.contents:
            if sub_items.name[0] != ".":
                print(sub_items.name, end=" ")
        print()

    def list_all_items(self) -> None:
        """
        Corresponds to "-A".
        List all items in the immediate subdirectory (including the once starting with ".").
        """
        for sub_itmes in self.contents:
            print(sub_itmes.name, end=" ")
        print()
    
    def long_list_items(self) -> None:
        for sub_items in self.contents:
            print(
                sub_items.permissions,
                sub_items.size,
                sub_items.time_modified,
                sub_items.name
            )

if __name__ == "__main__":
    structure_path = Path(__file__).parent / "structure.json"
    with open(structure_path) as fh:
        file_structure = json.load(fh)
    item = Item(**file_structure)

    parser = argparse.ArgumentParser()
    
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
    args = parser.parse_args()

    if len(sys.argv) == 1:
        """default behavior if no arguments are passed"""
        item.list_items()
    if args.all:
        item.list_all_items()
    if args.long:
        item.long_list_items()
    

