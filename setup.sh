#!/bin/bash
echo "[*] Initializing Aegis-Termux Environment..."
pkg update && pkg upgrade -y
pkg install termux-api python -y
pip install requests pyAesCrypt
echo "[+] Done. Edit config.json then run: python aegis.py"

