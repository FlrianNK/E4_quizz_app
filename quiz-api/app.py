import hashlib
from flask import Flask, request
from flask_cors import CORS
from jwt_utils import *

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    x = "World"
    return f"Hello, {x}"


@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return {"size": 3, "scores": [
        {
            "date": "18/04/2022 11:57:48",
            "playerName": "Emil",
            "score": 10,
        },
        {
            "date": "18/04/2022 11:57:48",
            "playerName": "Dora",
            "score": 8,
        },
        {
            "date": "18/04/2022 11:57:49",
            "playerName": "Gustav",
            "score": 7,
        }]
    }, 200

@app.route('/login', methods=['POST'])
def PostLogin():
    payload = request.get_json()
    tried_password = payload['password'].encode('UTF-8')
    hashed = hashlib.md5(tried_password).digest()
    if hashed == b'\xd8\x17\x06PG\x92\x93\xc1.\x02\x01\xe5\xfd\xf4_@':
        return {"token":build_token()}, 200
    return 'Unauthorized', 401


if __name__ == "__main__":
    app.run()
