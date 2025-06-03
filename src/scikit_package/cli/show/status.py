import os
import subprocess

import click

from scikit_package.utils import api, auth, io
from scikit_package.utils.shell import run
from scikit_package.utils import file


def main(args):
    dev_path = io.get_config_value("dev_path")
    # Get folders below the dev path
    folder_names = file.list_folders(dev_path)
    # Loop through each folder and list the issues and PRs with run
    for folder in folder_names:
        folder_path = os.path.join(dev_path, folder)
        print(f"\nFolder: {folder}")
        run(
            f"gh issue list",
            cwd=folder_path,
        )
        run(
            f"gh pr list",
            cwd=folder_path,
        )
