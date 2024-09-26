import getpass
from infra.config import ConfigManager


def input_config():
    access_key_id = getpass.getpass("Enter your aws access key id: ")
    secret_access_key = getpass.getpass("Enter your password aws secret_access key: ")
    ConfigManager.init_admin_access_key(access_key_id=access_key_id, secret_access_key=secret_access_key)

