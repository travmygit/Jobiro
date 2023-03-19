import logging

# 创建logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建handler并设置日志等级
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler('log.log')
file_handler.setLevel(logging.DEBUG)

# 设置输出格式
formatter = logging.Formatter('[%(asctime)s]%(name)s: %(levelname)s: %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将handler添加到logger中
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 输出日志
# logger.debug('debug message')
# logger.info('info message')
# logger.warning('warning message')
# logger.error('error message')
# logger.critical('critical message')
