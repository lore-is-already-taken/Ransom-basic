import os
from typing import List


def find_files_with_extension(work_dir, extensions: List[str]) -> List[str]:
    absolute_path = os.path.abspath(work_dir)
    files = os.listdir(absolute_path)

    filtered_files = []

    for item in files:
        if os.path.isdir(f"{work_dir}/{item}"):
            filtered_files += find_files_with_extension(
                f"{absolute_path}/{item}", extensions
            )

        elif any(item.endswith(ext) for ext in extensions):
            filtered_files.append(f"{absolute_path}/{item}")

    return filtered_files
