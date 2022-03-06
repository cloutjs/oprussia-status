from flask import Flask
from flask_restful import Api
import requests

app = Flask(__name__)
api = Api(app)

gist_id = "gist id"
github_user = "github username"

@app.route('/', methods=['GET'])
def index():
  r = requests.get("https://gist.githubusercontent.com/" + github_user + "/" + gist_id + "/raw/")
  return r.text

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=1337)
