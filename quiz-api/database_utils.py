import sqlite3

def initDataBase():
    try:
        db_connection = sqlite3.connect('./DataBase.db')
        cur = db_connection.cursor()
        cur.execute('DROP TABLE IF EXISTS Question')
        cur.execute('DROP TABLE IF EXISTS Participation')
        cur.execute(
            'CREATE TABLE Question (id INTEGER NOT NULL UNIQUE PRIMARY KEY, text TEXT, title TEXT, image TEXT, position INTEGER, possibleAnswers TEXT)')
        cur.execute('CREATE TABLE Participation (id INTEGER NOT NULL UNIQUE PRIMARY KEY, date TEXT, playerName TEXT, answers TEXT, score INTEGER)')
        db_connection.commit()
        cur.close()
        db_connection.close()
        return 'Ok', 200
    except Exception as e:
        return f"Internal Server Error\n {e}", 500
