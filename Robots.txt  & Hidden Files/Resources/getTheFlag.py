import requests
import re
import sys
import time

sys.setrecursionlimit(3000)
url = "http://10.13.100.223/.hidden/"

def find_flag(url):
    readme = requests.get(url+'README')
    print(readme.text.strip())
    if len(readme.text.replace(" ", "")) > 30:
        sys.exit(readme.text)  
    res = requests.get(url)
    res = list(dict.fromkeys(re.findall("[a-z]{26}", res.text.split('</h1>')[1])))
    for elm in res:
        find_flag(url+elm+'/')
        time.sleep(0.005)

find_flag(url)