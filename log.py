import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

if not os.path.exists('temp'):
    os.makedirs('temp')
file_handler = logging.FileHandler('temp/app.log')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('[%(asctime)s]%(name)s: %(levelname)s: %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)