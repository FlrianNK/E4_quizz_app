import json
import sqlite3
import ast


class Question(object):

    def __init__(self, text="", title="", image="", position=0, possibleAnswers=[]):
        self.text = text
        self.title = title
        self.image = image
        self.position = position
        self.possibleAnswers = possibleAnswers

    def toJson(self):
        return json.dumps(self.__dict__, default=lambda o: o.__dict__, indent=4, ensure_ascii=False).encode('utf8')

    def fromJson(self, json_data):
        newQuestion = Question(**(json.loads(json_data)))
        self.__dict__.update(newQuestion.__dict__)

class Answer(object):
    def __init__(self):
        self.text = ""
        self.isCorrect = False

    def toJson(self):
        return json.dumps(self.__dict__, ensure_ascii=False).encode('utf8')

    def fromJson(self, json_data):
        newAnswer = Answer(**(json.loads(json_data)))
        self.__dict__.update(newAnswer.__dict__)


def postQuestionToDB(data):
    db_connection = sqlite3.connect('./DataBase.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    insert_query = "INSERT INTO Question (text, title, image, position, possibleAnswers) VALUES (?, ?, ?, ?, ?)"
    input_question = Question(**data)
    cur.execute(insert_query, (input_question.text, input_question.title,
                input_question.image, input_question.position, str(input_question.possibleAnswers)))
    try:
        cur.execute('commit')
        id = cur.lastrowid
        cur.close()
        db_connection.close()
        return {"id": id}, 200
    except Exception as e:
        cur.execute('rollback')
        cur.close()
        db_connection.close()
        return f"Internal Server Error\n {e}", 500


def getQuestionFromDB(field, value):
    db_connection = sqlite3.connect('./DataBase.db')
    cur = db_connection.cursor()
    select_query = f"SELECT * FROM Question WHERE {field} = ?"
    cur.execute(select_query, (value,))
    rows = cur.fetchone()
    cur.close()
    db_connection.close()
    return ('Request respond Not Found', 404) if rows == None else (Question(*rows[1:-1], ast.literal_eval(rows[-1])).toJson(), 200)


def updateQuestionInDB(id, newData):
    db_connection = sqlite3.connect('./DataBase.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    update_query = "UPDATE Question SET text = ?, title = ?, image = ?, position = ?, possibleAnswers = ? WHERE id = ?"
    update_question = Question(**newData)
    cur.execute(update_query, (update_question.text, update_question.title,
                update_question.image, update_question.position, str(update_question.possibleAnswers), id))
    if cur.rowcount == 0:
        return 'Request respond Not Found', 404
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


def deleteQuestionFromDB(id):
    db_connection = sqlite3.connect('./DataBase.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    delete_query = "DELETE FROM Question WHERE id = ?"
    cur.execute(delete_query, (id,))
    if cur.rowcount == 0:
        return 'Request respond Not Found', 404
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


def deleteAllQuestionsFromDB():
    db_connection = sqlite3.connect('./DataBase.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    delete_query = "DELETE FROM Question"
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
