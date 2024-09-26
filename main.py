import argparse

from infra.adapter.prompter import input_config
from infra.aws.s3 import upload_to_s3, download_from_s3
from infra.config import ConfigManager
from util.file_util import check_file_existence


def launch_app():
    parser = argparse.ArgumentParser(description="Select download or upload mode")
    parser.add_argument('--mode', choices=['down', 'up'],
                        help="Choose the mode down or up")
    parser.add_argument('target_paths', nargs='+', help="Target paths to process")
    args = parser.parse_args()

    ConfigManager.load_config()

    if args.mode == 'down':
        input_config()
        object_name = args.target_paths[0]
        assert object_name
        download_from_s3(object_name=object_name)
    elif args.mode == 'up':
        input_config()
        file_path = args.target_paths[0]
        assert (check_file_existence(file_path))
        upload_to_s3(file_path=file_path)
    else:
        print('Invalid mode. please choose "down" or "up"')


if __name__ == "__main__":
    launch_app()
