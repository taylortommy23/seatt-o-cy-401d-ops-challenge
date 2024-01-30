#!/usr/bin/env python3

# Script Name: Brute Force Wordlist Attack Tool
# Author: David Renteria
# Purpose: Tool that uses both offensive & defensive dictionary attack tactics



# import necessary modules
import ssl
import time

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
            if user_word in (word.strip() for word in file):
                print(f"The word '{user_word}' is in the word list.")
            else:
                print(f"The word {user_word} is not in the word list.")
    except FileNotFoundError:
        print("That is not a valide file path.")

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
