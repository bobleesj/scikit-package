import os
from scikit_package.utils import io, file
from scikit_package.utils.shell import run


def main(args):
    dev_path = io.get_config_value("dev_path")
    folder_names = file.list_folders(dev_path)
    folder_count = len(folder_names)
    for i, name in enumerate(folder_names, start=1):
        folder_path = os.path.join(dev_path, name)
        print("\n" + "=" * 40)
        print(f"({i}/{folder_count}) {name}")
        print("" + "=" * 40)
        run(f"gh issue list", cwd=folder_path)
        run(f"gh pr list", cwd=folder_path)
