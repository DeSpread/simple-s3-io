from dataclasses import dataclass

from functools import cache

import yaml


@dataclass
class AdminAccessKey:
    access_key_id: str
    secret_access_key: str


@dataclass
class Configuration:

    @dataclass
    class S3:
        region_name: str
        bucket: str
        folder: str


class ConfigManager:
    __admin_access_key: AdminAccessKey = None
    __config: Configuration.S3 = None

    @staticmethod
    @cache
    def init_admin_access_key(access_key_id: str, secret_access_key: str):
        ConfigManager.__admin_access_key = AdminAccessKey(access_key_id=access_key_id,
                                                          secret_access_key=secret_access_key)
        return ConfigManager.__admin_access_key

    @staticmethod
    def get_admin_access_key() -> AdminAccessKey:
        return ConfigManager.__admin_access_key

    @staticmethod
    @cache
    def load_config() -> Configuration.S3:
        with open("config.yaml", "r") as f:
            config_yaml = yaml.safe_load(f)
            ConfigManager.__config = Configuration.S3(region_name=config_yaml['s3']['region_name'],
                                                      bucket=config_yaml['s3']['bucket'],
                                                      folder=config_yaml['s3']['folder'])
        return ConfigManager.__config

    @staticmethod
    def get_config() -> Configuration.S3:
        return ConfigManager.load_config()
