#!/usr/bin/env python3

# Script Name: Web App Fingerprinting
# Purpose: Banner grabbing/service fingerprinting to check if target computer supports specific services (intel gathering)

# import modules
import subprocess
import sys

def netcat_grabber(target, port_num):
    try:
        banner = subprocess.run(['nc', target, str(port_num)], capture_output=True, text=True, timeout=3)
        print(f"Netcat banner: \n{banner.stdout}")
    except subprocess.TimeoutExpired:
        print("Netcat timed out. Please try again")
    except Exception as e:
        print(f"The following error occurred: {e}")
def telnet_grabber(target, port_num):
    try:
        banner = subprocess.run(f"telnet {target} {port_num}", capture_output=True, text=True, timeout=3)
        print(f"Telnet banner: \n{banner.stdout}")
    except subprocess.TimeoutExpired:
        print("Telnet timed out. Please try again")
    except Exception as e:
        print(f"The following error occurred: {e}")
def nmap_grabber(target):
    try:
        banner = subprocess.run(['nmap', '-sV', target], capture_output=True, text=True, timeout=3)
        print(f"Nmap banner: \n{banner.stdout}")
    except subprocess.TimeoutExpired:
        print("Nmap timed out. Please try again")
    except Exception as e:
        print(f"The following error occurred: {e}")
def main():
    target = input("Please enter the target URL or IP address: ")
    port_num = input("Please enter the target port number: ")
    print("\n Will now perform banner grabbing using Netcat, Telnet, and Nmap: ")
    netcat_grabber(target, port_num)
    telnet_grabber(target, port_num)
    nmap_grabber(target, port_num)
if __name__ == "__main__":
    main()
  # Worked with David Renteria on this script
