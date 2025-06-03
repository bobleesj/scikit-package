import os


def list_folders(path):
    """Get folder names in the given path."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"The path {path} does not exist.")
    return [
        f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))
    ]
