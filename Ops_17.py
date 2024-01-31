#!/usr/bin/env python3

# Script Name: Brute Force Wordlist Attack Tool Pt 2
# Author: Tommy Taylor
# Purpose: Tool that uses both offensive & defensive dictionary attack tactics by authenticating to an SSH server by its IP address



# import necessary modules
import ssl
import time
import paramiko
import getpass

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# define functions for modes
def dict_it(target_file):
    try:
        # open file, read, and savie to mem as 'file'
        with open(target_file, 'r') as file:
            # iterate through word list
            for word in file:
                # remove any leading/ending characters
                word = word.strip()
                print(word)
                # 2 second delay between words
                time.sleep(2)
    except FileNotFoundError:
        print("Please check the file path and try again.")

def pass_rec(user_word, target_file):
    try:
        with open(target_file, 'r') as file:
            if user_word in (word.strip().lower() for word in file):
                print(f"The word '{user_word}' is in the word list.")
            else:
                print(f"The word {user_word} is not in the word list.")
    except FileNotFoundError:
        print("That is not a valide file path.")

def get_host():
    host = input("Enger an SSH Client to connect to or enter for default: ") or "192.168.12.211"
    return host

def get_user():
    user = input("Please enter a username or enter for default: ") or "user1"
    return user

def get_password():
    password = input("Please enter a password or enter for default: ") or "password1234"
    return password

def ssh_endpoint():
    port = 22
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(get_host(), port, get_user(), get_password())
        stdin, stdout, stderr = ssh.exec_command("whoami")
        time.sleep(2)
        output = stdout.read()
        print("-" * 80)
        print(output)
        stdin, stdout, stderr = ssh.exec_command("ls -l")
        time.sleep(2)
        output = stdout.read()
        print(output)
        stdin, stdout, stderr = ssh.exec_command("uptime")
        time.sleep(2)
        output = stdout.read()
        print(output)
        print("-" * 80)
    except paramiko.AuthenticationException as e:
        print("Authentication failed.")
        print(e)

def main():
    user_mode = input("Please enter '1' if you'd like to use the 'dictionay iterator' tactic or '2' if you want to check whether certain strings are in the password list\n")
    if user_mode == '1':
        target_file = input("Please enter the file path of the word list you want to search: ")
        dict_it(target_file)
    elif user_mode == '2':
        user_word = input("Please enter a word you would like to search for in the password list: ")
        target_file = input("Please enter the file path of the word list you want to search: ")
        pass_rec(user_word, target_file)
    else: 
        print("Please only enter the number 1 or 2: ")

if __name__ == "__main__":
    main()
    ssh_endpoint()
    # Roger's class17 demo
    # David Renteria
    # Brittany Powell
