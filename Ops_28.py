
import logging

# Create logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# Create handlers
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('my_log.log')

# Set logging levels for handlers
stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.DEBUG)

# Create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# Log some messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
# Worked with Brittany, Breanna, and Edwin on this Ops challenge 
