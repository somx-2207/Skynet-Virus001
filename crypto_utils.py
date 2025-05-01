from cryptography.fernet import Fernet
import os

KEY_FILE = os.path.expanduser("~/.keyfile_demo")

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

def load_key():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def encrypt_file(file_path, fernet):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted)
        return True
    except Exception:
        return False

def decrypt_file(file_path, fernet):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        decrypted = fernet.decrypt(data)
        with open(file_path, 'wb') as f:
            f.write(decrypted)
        return True
    except Exception:
        return False
