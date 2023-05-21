import json
import sqlite3
from datetime import datetime
from question_utils import *

class Participation(object):

    def __init__(self, date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), playerName="", score=0):
        self.date = date
        self.playerName = playerName
        self.score = score

    def toJson(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4, ensure_ascii=False).encode('utf8')

    def fromJson(self, json_data):
        newQuestion = Participation(**(json.loads(json_data)))
        self.__dict__.update(newQuestion.__dict__)

def getParticipationsList():
    participationsList = []
    db_connection = sqlite3.connect('./quiz.db')
    cur = db_connection.cursor()
    cur.execute("begin")
    query = f"SELECT * FROM Participation"
    cur.execute(query)
    try:
        rows = cur.fetchall()
        for row in rows:
            participation = Participation(*row[1:])
            participationsList += [json.loads(participation.toJson())]
        participationsList.sort(key=lambda participation: participation['score'], reverse=True)
    finally:
        cur.close()
        db_connection.close()
        return participationsList

def postParticipationToDB(data):
    input_participation = Participation()
    input_participation.playerName = data['playerName']
    answers = data['answers']
    questionSize = getQuestionsSize()
    if len(answers) != questionSize:
        return 'Bad request', 400
    goodAnswers = getGoodAnswersDict()
    score = 0
    for i in range(questionSize):
        if answers[i] == goodAnswers[i+1]:
            score += 1
    input_participation.score = score
    db_connection = sqlite3.connect('./quiz.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    insert_query = "INSERT INTO Participation (date, playerName, score) VALUES (?, ?, ?)"
    cur.execute(insert_query, (input_participation.date,
                input_participation.playerName, input_participation.score))
    try:
        cur.execute('commit')
        cur.close()
        db_connection.close()
        return input_participation.toJson(), 200
    except Exception as e:
        cur.execute('rollback')
        cur.close()
        db_connection.close()
        return f"Internal Server Error\n {e}", 500


def getGoodAnswersDict():
    goodAnswersDict = {}
    db_connection = sqlite3.connect('./quiz.db')
    cur = db_connection.cursor()
    cur.execute("begin")
    query = f"SELECT * FROM Question"
    cur.execute(query)
    rows = cur.fetchall()
    questions = []
    for row in rows:
        questions += [Question(*row[0:-1], ast.literal_eval(row[-1]))]
    for question in questions:
        answerPosition = 1
        for answer in question.possibleAnswers:
            if answer['isCorrect'] == True:
                goodAnswersDict[question.position] = answerPosition
                break
            answerPosition += 1
    cur.close()
    db_connection.close()
    return goodAnswersDict


def deleteAllParticipationsFromDB():
    db_connection = sqlite3.connect('./quiz.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    delete_query = "DELETE FROM Participation"
    cur.execute(delete_query)
    try:
        cur.execute('commit')
        cur.close()
        db_connection.close()
        return '', 204
    except Exception as e:
        cur.execute('rollback')
        cur.close()
        db_connection.close()
        return f"Internal Server Error\n {e}", 500
