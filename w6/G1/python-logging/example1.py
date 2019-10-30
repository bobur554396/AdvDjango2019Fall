import logging

logging.basicConfig(
    filename='example1.log',
    filemode='w',
    format='%(asctime)s -- %(levelno)s:%(levelname)s -- %(message)s',
    level=logging.DEBUG
)

name = 'Bobur'


logging.debug('%s says: debug message', name)
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
