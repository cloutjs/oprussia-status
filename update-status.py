import os
import requests
import json
import time

token = "github api token"
gist_id = "gist id"
filename = "links.txt"
github_user = "github username"

while True:
    e = "by portia (https://twitter.com/portia1337)<br><br>"
    urls = open('list.txt', 'r')
    for url in urls:
      try:
        r = requests.get(url.strip(), timeout=15)
        if r.status_code == 200:
            e = str(e) + f"{url.strip()} - Up<br>"
        elif r.status_code == 403:
            e = str(e) + f"{url.strip()} - Might be down (Status Code: {r.status_code})<br>"
        else:
            e = str(e) + f"{url.strip()} - Down<br>"
      except:
        e = str(e) + f"{url.strip()} - Down<br>"
    headers = {'Authorization': f'token {token}'}
    r = requests.patch('https://api.github.com/gists/' + gist_id, data=json.dumps({'files':{filename:{"content":e}}}),headers=headers) 
    time.sleep(65)
    r = requests.get("https://gist.githubusercontent.com/" + github_user + "/" + gist_id)
    time.sleep(200)

