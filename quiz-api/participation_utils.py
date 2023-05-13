import json
import sqlite3
from datetime import datetime


class Participation(object):

    def __init__(self, playerName="", answers=[]):
        current_time = datetime.now()
        self.date = current_time.strftime("%d/%m/%Y %H:%M:%S")
        self.playerName = playerName
        self.answers = answers
        self.score = 0

    def toJson(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4, ensure_ascii=False).encode('utf8')

    def fromJson(self, json_data):
        newQuestion = Participation(**(json.loads(json_data)))
        self.__dict__.update(newQuestion.__dict__)

def deleteAllParticipationsFromDB():
    db_connection = sqlite3.connect('./DataBase.db')
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
