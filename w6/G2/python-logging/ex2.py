import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(name)s -- %(asctime)s -- %(levelname)s -- %(message)s')
file_handler = logging.FileHandler('ex2.log')
file_handler.setFormatter(file_formatter)
file_handler.setLevel(logging.ERROR)


console_formatter = logging.Formatter('%(levelname)s -- %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)


logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
