from flask import Flask
from flask_cors import CORS

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


if __name__ == "__main__":
    app.run()
