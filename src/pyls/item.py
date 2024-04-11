from datetime import datetime
import math
from typing import Optional

def convert_size(byte_size):
    if byte_size < 1024: # remain in bytes
        return byte_size
    return str(round(byte_size/1024, 1))+"K"
    
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
        contents: Optional[list["Item"]] = None,
    ):

        self.name = name
        self.size = size
        self.time_modified = datetime.fromtimestamp(time_modified).strftime(
            "%b %d %H:%M"
        )
        self.permissions = permissions
        self.contents = []
        if contents:
            for sub_items in contents:
                self.contents.append(Item(**sub_items))

    def __repr__(self) -> str:
        # 'cause I actually want to understand what I'm looking
        return f"{self.name}"

    def list_items(self, list_all: bool, filter: Optional[str] = None) -> list:
        """
        Args:
            list_all (bool): True if -A is set
            filter (str): Specifies type of item to list with options dir or file.
        Returns:
            List of all items in the immediate subdirectory.
            If list_all is True, will include files starting with ".".
        """
        if not self.contents:
            return [self]

        item_list = [
            sub_item
            for sub_item in self.contents
            if list_all or sub_item.name[0] != "."
        ]
        filtered_list = item_list
        if filter == "dir":
            filtered_list = [
                filtered_item for filtered_item in item_list if filtered_item.contents
            ]
            return filtered_list

        filtered_list = [
            filtered_item for filtered_item in item_list if not filtered_item.contents
        ]
        return filtered_list

    def make_human_readable(self, item_list: list):
        for sub_item in item_list:
            sub_item.size = convert_size(sub_item.size)

    def sort_by_time(self, item_list: list) -> list:
        """Sorts item list by time_modified"""
        return sorted(item_list, key=lambda item_time: item_time.time_modified)

    def reverse_items(self, item_list: list) -> list:
        """Reverses listing of items"""
        return item_list[::-1]

    def display(self, item_list: list) -> None:
        """Display function for single line listing"""
        for item in item_list:
            print(item.name, end=" ")
        print()

    def long_list_items(self, item_list: list) -> None:
        """Display function for long listing"""
        for item in item_list:
            print(item.permissions, item.size, item.time_modified, item.name)
