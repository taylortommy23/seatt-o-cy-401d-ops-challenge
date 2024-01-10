import time
from datetime import datetime
from ping3 import ping, SocketTimeout

def check_host_status(destination_ip):
    try:
        response = ping(destination_ip, timeout=1)
        if response is not None:
            return True
        else:
            return False
    except SocketTimeout:
        return False

def main():
    destination_ip = "192.168.1.1"  # Replace with the IP address you want to test

    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = check_host_status(destination_ip)

        if status:
            print(f"[{timestamp}] Host {destination_ip} is UP")
        else:
            print(f"[{timestamp}] Host {destination_ip} is DOWN")

        time.sleep(2)

if __name__ == "__main__":
    main()
