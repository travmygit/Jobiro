import json
from log import logger


class Config:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


_config = None


def load_config():
    global _config
    try:
        with open('config.json', 'r') as f:
            _config = json.load(f, object_hook=lambda d: Config(**d))
    except FileNotFoundError:
        logger.error('Config file not found')
        raise
    except json.JSONDecodeError:
        logger.error('Config file is not a valid JSON file')
        raise

def conf():
    return _config