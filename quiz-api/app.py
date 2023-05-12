import hashlib
from flask import Flask, request
from flask_cors import CORS
from jwt_utils import *
from question_utils import *
from database_utils import *

app = Flask(__name__)
CORS(app)

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
        return {"token": build_token()}, 200
    return 'Unauthorized', 401

@app.route('/rebuild-db', methods=['POST'])
def RebuildDb():
    status = verifyAuthorization(request)[1]
    if status == 200:
        return initDataBase()
    return verifyAuthorization(request)

@app.route('/questions', methods=['POST'])
def PostQuestions():
    status = verifyAuthorization(request)[1]
    if status == 200:
        data = request.get_json()
        return sendQuestionToDB(data)
    return verifyAuthorization(request)
    
@app.route('/questions', methods=['GET'])
def GetQuestionByPosition():
    position = request.args.get('position')
    return f"get position {position}"

@app.route('/questions/<int:questionId>', methods=['GET'])
def GetQuestionById(questionId):
    return f"get questionId {questionId}"

@app.route('/questions/<int:questionId>', methods=['PUT'])
def PutQuestionById(questionId):
    return f"put questionId {questionId}"
    
@app.route('/questions/<int:questionId>', methods=['DELETE'])
def DeleteQuestion(questionId):
    return f"delete questionId {questionId}"

@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestions():
    return f"delete all questions"

@app.route('/participations/all', methods=['DELETE'])
def DeleteAllParticipations():
    return f"delete all participations"


if __name__ == "__main__":
    app.run()
