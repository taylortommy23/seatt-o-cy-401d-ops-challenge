from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    return open('key.key', 'rb').read()

def encrypt_file(filepath, key):
    try:
        with open(filepath, 'rb') as file:
            file_data = file.read()
        encrypted_data = Fernet(key).encrypt(file_data)
        with open(filepath, 'wb') as file:
            file.write(encrypted_data)
    except Exception as e:
        print(f"Error encrypting file: {e}")

def decrypt_file(filepath, key):
    try:
        with open(filepath, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = Fernet(key).decrypt(encrypted_data)
        with open(filepath, 'wb') as file:
            file.write(decrypted_data)
    except Exception as e:
        print(f"Error decrypting file: {e}")

def encrypt_message(message, key):
    try:
        return Fernet(key).encrypt(message.encode())
    except Exception as e:
        print(f"Error encrypting message: {e}")

def decrypt_message(encrypted_message, key):
    try:
        # Convert the string representation of bytes back to bytes
        encrypted_message_bytes = encrypted_message.encode().decode('unicode_escape').encode('ISO-8859-1')
        return Fernet(key).decrypt(encrypted_message_bytes).decode()
    except Exception as e:
        print(f"Error decrypting message: {e}")

def main():
    print("Choose a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice in ['1', '3']:
        key = generate_key()  # Generate a new key for encryption
    elif choice in ['2', '4']:
        key = load_key()  # Load the existing key for decryption

    if choice in ['1', '2']:
        filepath = input("Enter the file path: ")
        if choice == '1':
            encrypt_file(filepath, key)
            print("File encrypted successfully.")
        elif choice == '2':
            decrypt_file(filepath, key)
            print("File decrypted successfully.")

    elif choice in ['3', '4']:
        if choice == '3':
            message = input("Enter the message to encrypt: ")
            encrypted_message = encrypt_message(message, key)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == '4':
            encrypted_message = input("Enter the encrypted message to decrypt (without b' and '): ")
            print("Decrypted message:", decrypt_message(encrypted_message, key))

if __name__ == "__main__":
    main()
