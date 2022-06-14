import requests
import re
import sys
import time


def find_flag(url):
    readme = requests.get(url+'README')
    if len(readme.text.replace(" ", "")) > 30:
        sys.exit(readme.text)
    else:
        print(readme.text.strip())
    res = requests.get(url)
    res = list(dict.fromkeys(re.findall("[a-z]{26}", res.text.split('</h1>')[1])))
    for elm in res:
        find_flag(url+elm+'/')
        time.sleep(0.005)

if len(sys.argv) == 2 and sys.argv[1]:
    url = "http://"+sys.argv[1]+"/.hidden/"
    find_flag(url)
else:
    exit()