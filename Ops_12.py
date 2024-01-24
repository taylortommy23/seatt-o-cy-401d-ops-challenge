#!/usr/bin/env python3

# Script Name: Add Ping Sweep Mode to Nmap Scanner using Scapy
# Author: David Renteria
# Purpose: Ping Sweep & Scan network using Scapy

# import necessary modules
from scapy.all import IP, sr1,TCP, send, ICMP
import random
from ipaddress import ip_address

# define function to scan ports
def port_scan():
    while True:
        try:
            # get host/target IP address
            target_ip = input("Please enter the target IP of the computer on which you want to conduct either a TCP port scan: ")
            ip_address(target_ip)
            break
        except ValueError:
            print("Please enter a valid IP address")
    # identify ports to scan
    port_range = [20, 21, 22, 23, 53, 69, 80, 123, 179, 264, 443, 520]
    # loop through ports on target IP address
    for port in port_range:
        src_port = random.randint(1024, 65535)
        response = sr1(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags='S'), timeout=1, verbose=0)
        # conditionals to perform task based on port status
        if response is None:
            print(f"Port {port} is filtered and silently dropped")
        elif response.haslayer(TCP):
            if response.getlayer(TCP).flags == 0x12:
                send(IP(dst=target_ip)/TCP(sport=src_port, dport=port, flags='R'), verbose=0)
                print(f"Port {port} is open")
            elif response.getlayer(TCP).flags == 0x14:
                print(f"Port {port} is closed")

# define function for ICMP Ping Sweeps
def ping_sweep():
    my_net = '192.168.0.0/24'
    num_hosts = 0
    net_ipaddrs = ipaddress.IPv4Network(my_net).hosts()
    # loop through the ip addresses on the network to ping
    for target_ip in net_ipaddrs:
        print("Pinging", str(target_ip), "- please wait...")
        response = sr1(IP(dst=str(target_ip))/ICMP(), timeout=2, verbose=0)
        # condition based responses
        if response is None:
            print(f"Target IP {target_ip} is unresponsive.")
        elif response.haslayer(ICMP):
            if int(response.getlayer(ICMP).type) == 3 and int(response.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]:
                print(f"Target IP {target_ip} is actively blocking ICMP pings.")
            else:
                print(f"Target IP {target_ip} is responsive.")
                num_hosts += 1
    print(f"The current number of IPs online is {num_hosts}")

# define main function to provide user a menue and tie it all together
def main():
    user_input = input("Please select a number for a respective task:\n1: Port Scanner\n2: Ping Sweep\n")
    # user input conditional
    if user_input == '1':
        port_scan()
    elif user_input == '2':
        ping_sweep()
    else:
        print("Please enter only the number 1 or 2.")

if __name__ == '__main__':
    main()
