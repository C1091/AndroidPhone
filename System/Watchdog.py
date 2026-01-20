import subprocess
import time
import os

package_name = "com.OS.Android"

def is_running(pkg):
    # Check if the app is running via Android's 'pidof'
    try:
        output = subprocess.check_output(f"pidof {pkg}", shell=True)
        return bool(output.strip())
    except subprocess.CalledProcessError:
        return False

def start_app(pkg):
    # Launch the app via 'am start'
    subprocess.run(f"am start -n {pkg}/.MainActivity", shell=True)

while True:
    if not is_running(package_name):
        print(f"{package_name} is not running. Restarting...")
        start_app(package_name)
    
    time.sleep(5)
