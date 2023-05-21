import json
import sqlite3
import ast

class Question(object):

    def __init__(self, id="", text="", title="", image="", position=0, possibleAnswers=[]):
        self.id = id
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

def getQuestionsSize():
    row_count = 0
    db_connection = sqlite3.connect('./quiz.db')
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


def postQuestionToDB(data):
    db_connection = sqlite3.connect('./quiz.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    query = f"SELECT COUNT(*) FROM Question"
    cur.execute(query)
    result = cur.fetchone()
    totalQuestionsNumber = result[0]
    input_question = Question(**data)
    if input_question.position <= 0:
        input_question.position = 1
    if input_question.position < totalQuestionsNumber:
        condition = "position >= " + str(input_question.position)
        update_query = f"UPDATE Question SET position = position + ? WHERE {condition}"
        cur.execute(update_query, (1,))
    else:
        input_question.position = totalQuestionsNumber+1
    insert_query = "INSERT INTO Question (text, title, image, position, possibleAnswers) VALUES (?, ?, ?, ?, ?)"
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
    db_connection = sqlite3.connect('./quiz.db')
    cur = db_connection.cursor()
    cur.execute("begin")
    select_query = f"SELECT * FROM Question WHERE {field} = ?"
    cur.execute(select_query, (value,))
    rows = cur.fetchone()
    cur.close()
    db_connection.close()
    return ('Request respond Not Found', 404) if rows == None else (Question(*rows[:-1], ast.literal_eval(rows[-1])).toJson(), 200)


def getAllQuestionFromDb():
    questionList = []
    db_connection = sqlite3.connect('./quiz.db')
    cur = db_connection.cursor()
    cur.execute("begin")
    query = f"SELECT * FROM Question"
    cur.execute(query)
    try:
        rows = cur.fetchall()
        for row in rows:
            question = Question(*row)
            questionList.append(json.loads(question.toJson()))
        questionList.sort(key=lambda question: question['position'])
        cur.close()
        db_connection.close()
        return questionList, 200
    except Exception as e:
        cur.close()
        db_connection.close()
        return f"Internal Server Error\n {e}", 500


def updateQuestionInDB(id, newData):
    db_connection = sqlite3.connect('./quiz.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    select_query = f"SELECT * FROM Question WHERE id == {id}"
    cur.execute(select_query)
    if cur.fetchone() == None:
        cur.close()
        db_connection.close()
        return 'Request respond Not Found', 404
    update_question = Question(id, **newData)
    query = f"SELECT COUNT(*) FROM Question"
    cur.execute(query)
    result = cur.fetchone()
    totalNumberOfQuestions = result[0]
    if update_question.position > totalNumberOfQuestions:
        update_question.position = totalNumberOfQuestions
    if update_question.position <= 0:
        update_question.position = 1
    select_query = f"SELECT * FROM Question WHERE position == {update_question.position}"
    cur.execute(select_query)
    old_data = cur.fetchone()
    if old_data:
        questionWithSamePos = Question(*old_data)
        if update_question.position == questionWithSamePos.position and id != questionWithSamePos.id:
            select_query = f"SELECT * FROM Question WHERE id == {id}"
            cur.execute(select_query)
            old_question = Question(*cur.fetchone())
            old_position = old_question.position
            new_position = update_question.position
            if new_position < old_position:
                condition = f"(position >= {new_position} AND position < {old_position})"
                update_query = f"UPDATE Question SET position = position + ? WHERE {condition}"
            else:
                condition = f"(position <= {new_position} AND position > {old_position})"
                update_query = f"UPDATE Question SET position = position - ? WHERE {condition}"
            cur.execute(update_query, (1,))
    update_query = "UPDATE Question SET text = ?, title = ?, image = ?, position = ?, possibleAnswers = ? WHERE id = ?"
    cur.execute(update_query, (update_question.text, update_question.title,
                update_question.image, update_question.position, str(update_question.possibleAnswers), id))
    if cur.rowcount < 1:
        cur.close()
        db_connection.close()
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
    db_connection = sqlite3.connect('./quiz.db')
    db_connection.isolation_level = None
    cur = db_connection.cursor()
    cur.execute("begin")
    select_query = f"SELECT * FROM Question WHERE id == {id}"
    cur.execute(select_query)
    old_data = cur.fetchone()
    if old_data:
        old_question = Question(*old_data)
        condition = "position >= " + str(old_question.position)
        update_query = f"UPDATE Question SET position = position - ? WHERE {condition}"
        cur.execute(update_query, (1,))
    delete_query = "DELETE FROM Question WHERE id = ?"
    cur.execute(delete_query, (id,))
    if cur.rowcount < 1:
        cur.close()
        db_connection.close()
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
    db_connection = sqlite3.connect('./quiz.db')
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
