import logging


logging.basicConfig(
    filename='ex1.log',
    level=logging.INFO,
    filemode='w',
    format='%(asctime)s -- %(levelname)s -- %(message)s'
)

name = 'test text'

logging.debug('debug message')
logging.info('info message: %s', name)
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')
