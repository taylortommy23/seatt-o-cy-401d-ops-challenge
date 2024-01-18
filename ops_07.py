import os
from cryptography.fernet import Fernet

# Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

# Save the encryption key to a file
def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

# Load the encryption key from a file
def load_key(key_file):
    with open(key_file, 'rb') as file:
        return file.read()

# Encrypt a file
def encrypt_file(key, file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original_data = file.read()
    encrypted_data = fernet.encrypt(original_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Decrypt a file
def decrypt_file(key, file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Recursively encrypt a folder and its contents
def encrypt_folder(key, folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(key, file_path)

# Recursively decrypt a folder that was encrypted by this tool
def decrypt_folder(key, folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypt_file(key, file_path)

if __name__ == "__main__":
    key = generate_key()
    key_file = 'encryption_key.key'
    save_key(key, key_file)

    folder_to_encrypt = 'path/to/your/folder'
    encrypt_folder(key, folder_to_encrypt)
    print(f'Folder "{folder_to_encrypt}" encrypted.')

    folder_to_decrypt = 'path/to/your/encrypted/folder'
    decrypt_folder(key, folder_to_decrypt)
    print(f'Folder "{folder_to_decrypt}" decrypted.')
