import json
from flask import Flask
app = Flask(__name__)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "Amin",
        "lastname": "Espinoza",
        "socialMedia":
        [
            {"facebookUser": "stiven Melo"},
            {"instagramUser": "stiven Melo"},
            {"xUser": "stiven Melo"},
            {"linkedin": "stiven Melo"},
            {"githubUser": "stiven Melo"}
        ],
        "blog": "https://stiven-Melo.com",
        "author": "stiven Melo"
    }
    return json.dumps(value)
