import logging
from logging.handlers import RotatingFileHandler


logger = logging.getLogger('ex3')

handler = RotatingFileHandler('ex3.log', maxBytes=2000, backupCount=10)

logger.addHandler(handler)

for i in range(500):
    logger.warning('test message %d', i)
