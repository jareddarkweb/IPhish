#!/bin/bash
clear
echo "=========================================="
echo "      IPhish - Automated Setup           "
echo "=========================================="

# 1. Create venv if missing
if [ ! -d "venv" ]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv venv
fi

# 2. Install Dependencies
echo "[*] Ensuring libraries are installed..."
./venv/bin/pip install flask pyngrok python-dotenv --quiet

# 3. Launching (Using absolute path to the venv python)
echo "[+] Starting Server..."
./venv/bin/python3 server.py

# 4. Keep window open if it crashes
echo "------------------------------------------"
echo "[!] Server has stopped."
read -p "Press Enter to exit..."
