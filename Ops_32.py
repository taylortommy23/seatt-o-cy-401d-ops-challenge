#!/usr/bin/python3

import hashlib
import os
import datetime

def calculate_md5(filepath):
    md5_hash = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def main():
    file_path = "/path/to/your/file.txt"  # Replace this with the actual file path
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)
    md5_hash = calculate_md5(file_path)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("Timestamp:", timestamp)
    print("File Name:", file_name)
    print("File Size:", file_size, "bytes")
    print("File Path:", file_path)
    print("MD5 Hash:", md5_hash)

if __name__ == "__main__":
    main()

# had to resort to Chat GPT to get my script to run right
