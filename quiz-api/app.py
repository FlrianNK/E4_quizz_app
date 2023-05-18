import hashlib
from flask import Flask, request
from flask_cors import CORS
from jwt_utils import *
from question_utils import *
from participation_utils import *

app = Flask(__name__)
CORS(app)


@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
    return { "size": getQuestionsSize(), "scores": getParticipationsList() }, 200


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
        return postQuestionToDB(data)
    return verifyAuthorization(request)


@app.route('/questions', methods=['GET'])
def GetQuestionByPosition():
    position = request.args.get('position')
    return getQuestionFromDB('position', position)

@app.route('/questions/all', methods=['GET'])
def GetAllQuestions():
    return getAllQuestionFromDb()

@app.route('/questions/<int:questionId>', methods=['GET'])
def GetQuestionById(questionId):
    return getQuestionFromDB('id', questionId)


@app.route('/questions/<int:questionId>', methods=['PUT'])
def PutQuestionById(questionId):
    status = verifyAuthorization(request)[1]
    if status == 200:
        data = request.get_json()
        return updateQuestionInDB(questionId, data)
    return verifyAuthorization(request)


@app.route('/questions/<int:questionId>', methods=['DELETE'])
def DeleteQuestion(questionId):
    status = verifyAuthorization(request)[1]
    if status == 200:
        return deleteQuestionFromDB(questionId)
    return verifyAuthorization(request)


@app.route('/questions/all', methods=['DELETE'])
def DeleteAllQuestions():
    status = verifyAuthorization(request)[1]
    if status == 200:
        return deleteAllQuestionsFromDB()
    return verifyAuthorization(request)


@app.route('/participations', methods=['POST'])
def PostParticipation():
    data = request.get_json()
    return postParticipationToDB(data)


@app.route('/participations/all', methods=['DELETE'])
def DeleteAllParticipations():
    status = verifyAuthorization(request)[1]
    if status == 200:
        return deleteAllParticipationsFromDB()
    return verifyAuthorization(request)


if __name__ == "__main__":
    app.run()
