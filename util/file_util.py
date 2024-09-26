from pathlib import Path


def check_file_existence(file_path):
    file_path = Path(file_path)
    return file_path.exists()
