import requests
import re
import sys

url = "http://10.13.100.223/.hidden/"
# res = requests.get(url)
# print(res.text.split('</h1>')[1])
# res = list(dict.fromkeys(re.findall("[a-z]{26}", res.text)))
# print(res)
def find_flag(url):
    file = requests.get(url+'README')
    print(file.text)
    if len(file.text) > 34:
        sys.exit(file.text)  
    res = requests.get(url)
    res = list(dict.fromkeys(re.findall("[a-z]{26}", res.text.split('</h1>')[1])))
    for elm in res:
        find_flag(url+elm+'/')

find_flag(url)