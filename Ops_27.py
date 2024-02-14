# Imports the necessary modules
from cryptography.fernet import Fernet
import os
import logging
from logging.handlers import RotatingFileHandler

# Configure logging with rotation based on size
max_log_size_bytes = 1000000  # 1 MB
handler = RotatingFileHandler('encryption_tools.log', maxBytes=max_log_size_bytes, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# Generates a new encryption key using Fernet and saves it to (key.key.)
# Logs the operation
def generate_key():
    try:
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
        logging.info("Key generated and saved successfully.")
        return key
    except Exception as e:
        logging.error(f"Failed to generate or save key: {e}")

# Loads the encryption key from (key.key.)
# Logs failure on error
def load_key():
    try:
        return open('key.key', 'rb').read()
    except Exception as e:
        logging.error(f"Failed to load key: {e}")
        raise

# Rest of your functions remain unchanged...
