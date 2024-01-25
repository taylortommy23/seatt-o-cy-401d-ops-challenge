#!/usr/bin/env python3

# Script Name: Ntwk Sec Tool Pt 3
# Author: Tommy Taylor
# Purpose: Combine Port Scanner & Ping Sweep

# import necessary modules
from scapy.all import IP, sr1,TCP, send, ICMP
import random

# define function to scan ports
def scan_ports(target_ip):
    port_range = [20, 21, 22, 23, 80, 443, 3389]
    for port in port_range:
        src_port = random.randint(1024, 65535)
        response = sr1(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags='S'), timeout=1, verbose=0)
        # condition based responses
        if response is None:
            print(f"Port {port} is filtered/silently dropped")
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                send(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags='R'), verbose=0)
                print(f"Port {port} is open")
            elif response.getlayer(TCP).flags == 0x14:
                print(f"Port {port} is closed")
def ping_sweep(target_ip):
    response = sr1(IP(dst=target_ip)/ICMP(), timeout=1, verbose=0)
    if response:
        return True
    else:
        return False
def main():
    target_ip = input("Please enter the target IP address you want to test: ")
    if ping_sweep(target_ip):
        print(f"Target IP address {target_ip} is active. Scanning ports now...")
        scan_ports(target_ip)
    else:
        print(f"Target IP address {target_ip} is not responding to Ping requests. Please try again later")

if __name__ == '__main__':
    main()
  

Collaberated with David Renteria
