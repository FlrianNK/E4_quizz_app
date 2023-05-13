import sqlite3
from participation_utils import *

def initDataBase():
    try:
        db_connection = sqlite3.connect('./DataBase.db')
        cur = db_connection.cursor()
        cur.execute("begin")
        cur.execute('DROP TABLE IF EXISTS Question')
        cur.execute('DROP TABLE IF EXISTS Participation')
        cur.execute(
            'CREATE TABLE Question (id INTEGER NOT NULL UNIQUE PRIMARY KEY, text TEXT, title TEXT, image TEXT, position INTEGER, possibleAnswers TEXT)')
        cur.execute(
            'CREATE TABLE Participation (id INTEGER NOT NULL UNIQUE PRIMARY KEY, date TEXT, playerName TEXT, score INTEGER)')
        db_connection.commit()
        cur.close()
        db_connection.close()
        return 'Ok', 200
    except Exception as e:
        return f"Internal Server Error\n {e}", 500


def getQuestionsSize():
    row_count = 0
    db_connection = sqlite3.connect('./DataBase.db')
    cur = db_connection.cursor()
    cur.execute("begin")
    query = f"SELECT COUNT(*) FROM Question"
    cur.execute(query)
    try:
        result = cur.fetchone()
        row_count = result[0]
    finally:
        cur.close()
        db_connection.close()
        return row_count


def getParticipationsList():
    participationsList = []
    db_connection = sqlite3.connect('./DataBase.db')
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
