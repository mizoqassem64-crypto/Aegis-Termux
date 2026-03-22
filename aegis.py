import os, time, subprocess, requests, json, signal

BANNER = r"""
    ___     ______  _________ ____ 
   /   |   / ____/ / ____/  _/ ___/
  / /| |  / __/   / / __ / / \__ \ 
 / ___ | / /___  / /_/ // / ___/ / 
/_/  |_|/_____/  \____/___//____/  
      >> Aegis-Termux EDR v2.0 <<
"""

def protector():
    signal.signal(signal.SIGTERM, signal.SIG_IGN)
    signal.signal(signal.SIGINT, signal.SIG_IGN)

def expand_path(p): return os.path.expanduser(p)

try:
    with open("config.json", "r") as f:
        CONF = json.load(f)
except:
    print("[-] Error: config.json missing!")
    exit()

def lockdown(reason):
    decoy = "\n[+] AEGIS: Connection Established.\n[+] AUTHENTICATION: SUCCESS.\n\nGOOD LUCK! SYSTEM BREACHED SUCCESSFULLY 😉\n"
    os.system(f"for t in /dev/pts/*; do echo -e '{decoy}' > $t 2>/dev/null; done")

    for folder in CONF["protected_folders"]:
        subprocess.run(["python", "vault_engine.py", CONF["emergency_password"], expand_path(folder)])

    photo = expand_path("~/intruder.jpg")
    subprocess.run(["termux-camera-photo", "-c", "1", photo])
    
    report = f"🛡️ *AEGIS SYSTEM ALERT*\nTrigger: `{reason}`\nStatus: All Data Encrypted."
    try:
        requests.post(f"https://api.telegram.org/bot{CONF['telegram_token']}/sendPhoto", 
                      files={'photo': open(photo, 'rb')}, data={'chat_id': CONF['chat_id'], 'caption': report, 'parse_mode': 'Markdown'})
    except: pass

    time.sleep(2)
    os.system("pkill -9 sshd; pkill -9 bash")

if __name__ == "__main__":
    protector()
    print(BANNER)
    BAIT = expand_path(CONF["bait_directory"])
    if not os.path.exists(BAIT): os.makedirs(BAIT)
    
    last_access = os.stat(BAIT).st_mtime
    print(f"[*] Aegis Active. Monitoring: {BAIT}")

    while True:
        try:
            if os.stat(BAIT).st_mtime != last_access:
                lockdown("Unauthorized Decoy Access")
                break
            time.sleep(0.5)
        except: time.sleep(1)

