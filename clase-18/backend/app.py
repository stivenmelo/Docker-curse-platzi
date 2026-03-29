from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getMyInfo')
def getMyInfo():
    value = {
        "name": "STIVEN",
        "lastname": "MELO",
        "socialMedia":
        {
            "facebookUser": "pibemelo",
            "instagramUser": "dnniiel.melo",
            "xUser": "pibemelo",
            "linkedin": "stiven-daniel-melo-guayazan",
            "githubUser": "stivenmelo"
        },
        "blog": "https://STIVEN-MELO.com",
        "author": "STIVEN MELO"
    }

    return jsonify(value)

if __name__ == '__main__':
    app.run(port=5000)