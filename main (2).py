import os
import requests
import json
import time
import keep_alive

token=os.environ['apikey']
gist_id="b6e7e2150e5e0a5804968aea3cf85986"
filename="links.txt"

keep_alive.keep_alive()

while True:
    e = "by portia (https://twitter.com/portia1337)<br><br>"
    urls = open('list.txt', 'r')
    for url in urls:
      try:
        r = requests.get(url.strip(), timeout=5)
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
    r = requests.get("https://gist.githubusercontent.com/cloutjs/b6e7e2150e5e0a5804968aea3cf85986/")
    time.sleep(200)

