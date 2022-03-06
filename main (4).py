from flask import Flask
from flask_restful import Api
import requests

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def index():
  r = requests.get("https://gist.githubusercontent.com/cloutjs/b6e7e2150e5e0a5804968aea3cf85986/raw/")
  return r.text

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=1337)