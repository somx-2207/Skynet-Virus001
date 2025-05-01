from cryptography.fernet import Fernet
import os
from common.crypto_utils import decrypt_file

key = input("Enter decryption key: ")
fernet = Fernet(key.encode())

TARGET_FOLDERS = [
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Pictures"),
    os.path.expanduser("~/Music"),
    os.path.expanduser("~/Videos"),
]

for folder in TARGET_FOLDERS:
    for root, _, files in os.walk(folder):
        for file in files:
            decrypt_file(os.path.join(root, file), fernet)
print("Decryption complete.")
