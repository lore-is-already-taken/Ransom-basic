import os
from typing import List


class Finder:
    def __init__(self, route) -> None:
        self.route = route

    def find_files_with_extension(self, extensions: List[str]) -> List[str]:
        files = os.listdir(self.route)
        filtered_files = [
            f"{self.route}/{file}"
            for file in files
            if any(file.endswith(ext) for ext in extensions)
        ]
        return filtered_files
