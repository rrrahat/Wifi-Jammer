# WiFi Jammer Educational Script (Updated)
# Author: Rahat Hasan
# For Educational Purpose Only

import os
import time
import shutil

def check_aircrack():
    if not shutil.which("airmon-ng"):
        print("[-] Error: aircrack-ng tools not installed.")
        exit(1)

def wifi_jam(interface, duration=300):
    print(f"[+] Starting WiFi Jammer on {interface} for {duration//60} minutes...")
    time.sleep(2)
    os.system(f"airmon-ng start {interface}")
    os.system(f"airodump-ng {interface}mon &")
    time.sleep(duration)
    os.system(f"airmon-ng stop {interface}mon")
    print("[+] WiFi Jam Session Ended.")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("[-] Please run as root or with sudo.")
        exit(1)
        
    check_aircrack()
    interface = input("[?] Enter your WiFi Interface (example: wlan0): ").strip()
    wifi_jam(interface)
