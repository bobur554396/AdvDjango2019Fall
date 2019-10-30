import logging

logger = logging.getLogger(__name__)

f_format = logging.Formatter('%(name)s - %(asctime)s -- %(levelno)s:%(levelname)s -- %(message)s')
s_format = logging.Formatter('%(name)s - %(levelno)s:%(levelname)s -- %(message)s')

f_handler = logging.FileHandler('example2.log')
f_handler.setLevel(logging.ERROR)

s_handler = logging.StreamHandler()
s_handler.setLevel(logging.INFO)

f_handler.setFormatter(f_format)
s_handler.setFormatter(s_format)

logger.addHandler(f_handler)
logger.addHandler(s_handler)


logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
