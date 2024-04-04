#!/usr/bin/env python3

from dataclasses import dataclass
from importlib.resources import contents
import json
from pathlib import Path
from typing import Optional


class Items:

    def __init__(
        self, 
        name: str, 
        size: int, 
        time_modified: int, 
        permissions: str, 
        contents: Optional[list["Items"]] = None
    ):

        self.name = name
        self.size = size
        self.time_modified = time_modified
        self.permissions = permissions
        self.contents = []
        if contents:
            for sub_items in contents:
                self.contents.append(Items(**sub_items))

if __name__ == "__main__":
    structure_path = Path(__file__).parent / "structure.json"
    with open(structure_path) as fh:
        file_structure = json.load(fh)
    item = Items(**file_structure)