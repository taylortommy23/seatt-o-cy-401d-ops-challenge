#!/usr/bin/env python3
# used chatgpt to help understanding
# Imports the necessary modules
from cryptography.fernet import Fernet
import os
import logging

# Configure logging
# Configures the logging system to append messages to encryption_tools.log, with a specific format including timestamp, log level, and message
# Logs all messages at the DEBUG level and above
logging.basicConfig(filename='encryption_tools.log',
                    filemode='a',  # Append to the log file if it exists
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)

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
        logging.error("Failed to load key: {e}")
        raise
# Encrypts a file at filepath with the provided key and replaces its contents with the encrypted data
# Logs the operation and any errors
def encrypt_file(filepath, key):
    try:
        with open(filepath, 'rb') as file:
            file_data = file.read()
        encrypted_data = Fernet(key).encrypt(file_data)
        with open(filepath, 'wb') as file:
            file.write(encrypted_data)
        logging.info(f"File {filepath} encrypted successfully.")
    except Exception as e:
        logging.error(f"Error encrypting file {filepath}: {e}")
# Decrypts a file at filepath with the provided key and replaces its contents with the decrypted data 
# Logs the operation and any errors
def decrypt_file(filepath, key):
    try:
        with open(filepath, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = Fernet(key).decrypt(encrypted_data)
        with open(filepath, 'wb') as file:
            file.write(decrypted_data)
        logging.info(f"File {filepath} decrypted successfully.")
    except Exception as e:
        logging.error(f"Error decrypting file {filepath}: {e}")
# Encrypts a message string with the provided key and logs the operation
def encrypt_message(message, key):
    try:
        encrypted_message = Fernet(key).encrypt(message.encode())
        logging.info("Message encrypted successfully.")
        return encrypted_message
    except Exception as e:
        logging.error(f"Error encrypting message: {e}")
# Decrypts an encrypted message string with the provided key 
# The encrypted message is first converted from a UTF-8 string to bytes before decryption. 
# Logs the operation and any errors
def decrypt_message(encrypted_message, key):
    try:
        encrypted_message_bytes = bytes(encrypted_message, 'utf-8')
        decrypted_message = Fernet(key).decrypt(encrypted_message_bytes).decode()
        logging.info("Message decrypted successfully.")
        return decrypted_message
    except Exception as e:
        logging.error(f"Error decrypting message: {e}")
# Defines the main program logic
# Logs the start of the program
# Prompts the user to choose an operation mode
def main():
    logging.info("Program started")
    print("Choose a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message")
    choice = input("Enter your choice (1/2/3/4): ")

    # Depending on the user's choice, generates a new key for encryption or loads an existing key for decryption
    if choice in ['1', '3']:
        key = generate_key()
    elif choice in ['2', '4']:
        key = load_key()

    # If the choice is to encrypt or decrypt a file, prompts for the file path and calls the appropriate function
    if choice in ['1', '2']:
        filepath = input("Enter the file path: ")
        if choice == '1':
            encrypt_file(filepath, key)
        elif choice == '2':
            decrypt_file(filepath, key)
    # If the choice is to encrypt or decrypt a message, handles input and output accordingly, displaying the result to the user
    elif choice in ['3', '4']:
        if choice == '3':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '4':
            encrypted_message = input("Enter the encrypted message to decrypt: ")
            decrypted_message = decrypt_message(encrypted_message, key)
            print(f"Decrypted message: {decrypted_message}")
# Ensures that the main() function is called when the script is executed directly, starting the program
if __name__ == "__main__":
    main()
