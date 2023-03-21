import json
from log import logger


class Config:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


config = None


def load_config():
    global config
    assert config is None, "The config has already been loaded"
    try:
        logger.info('Loading config')
        with open('app_config.json', 'r') as f:
            config = json.load(f, object_hook=lambda d: Config(**d))
    except FileNotFoundError:
        logger.error('Config file not found')
        raise
    except json.JSONDecodeError:
        logger.error('Config file is not a valid JSON file')
        raise

def reload_config():
    global config
    config = None
    load_config()


load_config()