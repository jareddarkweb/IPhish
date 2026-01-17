import os
import subprocess
import sys

def setup():
    print("--- IPhish Automated Setup ---")
    
    # 1. Install dependencies
    print("[*] Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask", "pyngrok", "python-dotenv"])

    # 2. Create directory structure
    print("[*] Creating folders...")
    folders = ['templates', 'static']
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # 3. Create a default .env file if it's missing
    if not os.path.exists('.env'):
        print("[*] Creating default .env file...")
        with open('.env', 'w') as f:
            f.write("ADMIN_PASSWORD=admin123\n")
            f.write("FLASK_SECRET=change_this_to_something_random\n")
            f.write("NGROK_AUTH_TOKEN=YOUR_NGROK_TOKEN_HERE\n")
        print("[!] ACTION REQUIRED: Please edit the .env file with your actual ngrok token.")

    print("\n[+] Setup Complete! You can now run 'python server.py'")

if __name__ == "__main__":
    setup()
