import boto3
from botocore.exceptions import NoCredentialsError
from pathlib import Path

from infra.config import ConfigManager


def upload_to_s3(file_path, object_name=None, bucket=ConfigManager.get_config().bucket,
                 region_name=ConfigManager.get_config().region_name):
    config = ConfigManager.get_config()
    admin_access_key = ConfigManager.get_admin_access_key()

    s3_client = boto3.client('s3', region_name=region_name, aws_access_key_id=admin_access_key.access_key_id,
                             aws_secret_access_key=admin_access_key.secret_access_key)

    file_name = Path(file_path).expanduser()

    if object_name is None:
        object_name = file_name

    target_object_name = f"{config.folder}/{object_name}" if config.folder else file_path

    try:
        s3_client.upload_file(file_path, bucket, target_object_name)
        print(f"File {file_path} has been uploaded to {bucket}/{target_object_name}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found")
    except NoCredentialsError:
        print("Credentials not available")


def download_from_s3(object_name, file_path=None, bucket=ConfigManager.get_config().bucket,
                     region_name=ConfigManager.get_config().region_name):
    config = ConfigManager.get_config()
    admin_access_key = ConfigManager.get_admin_access_key()

    s3_client = boto3.client('s3', region_name=region_name, aws_access_key_id=admin_access_key.access_key_id,
                             aws_secret_access_key=admin_access_key.secret_access_key)

    if file_path is None:
        file_path = object_name

    target_object_name = f"{config.folder}/{object_name}" if config.folder else object_name

    try:
        s3_client.download_file(bucket, target_object_name, file_path)
        print(f"File {target_object_name} has been downloaded from {bucket} to {file_path}")
    except FileNotFoundError:
        print(f"The file {file_path} was not found locally.")
    except NoCredentialsError:
        print("Credentials not available")
    except Exception as e:
        print(f"An error occurred: {e}")