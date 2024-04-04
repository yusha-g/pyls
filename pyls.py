#!/usr/bin/env python3

import json
from pathlib import Path
from re import I
from typing import Optional
from pydantic import BaseModel
    
class Items(BaseModel):
    name: str
    size: int
    time_modified: int
    permissions: str
    contents: Optional[list["Items"]] = None

    def list_items(self):
        if self.contents is not None:
            for items in self.contents:
                print(items.name, end=" ")
            print()

if __name__ == "__main__":
    structure_path = Path(__file__).parent / "structure.json"
    with open(structure_path) as fh:
        file_structure = json.load(fh)

    file = Items(**file_structure)
    file.list_items()