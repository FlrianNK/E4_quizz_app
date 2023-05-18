import jwt
import datetime
import sqlite3
from werkzeug.exceptions import Unauthorized


class JwtError(Exception):
    """Exception raised for jwt errors in the quiz app 
    """

    def __init__(self, message="Jwt error"):
        self.message = message
        super().__init__(self.message)


secret = "Le chat noir dort paisiblement"
expiration_in_seconds = 3600


def build_token():
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expiration_in_seconds),
            'iat': datetime.datetime.utcnow(),
            'sub': 'quiz-app-admin'
        }
        return jwt.encode(
            payload,
            secret,
            algorithm="HS256"
        )
    except Exception as e:
        return e


def decode_token(auth_token):
    """
    Decodes the auth token
    :param auth_token:
    :return: integer|string
    """
    try:
        payload = jwt.decode(auth_token, secret, algorithms="HS256")
        # if decoding did not fail, this means we are correctly logged in
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise JwtError('Signature expired. Please log in again.')
    except jwt.InvalidTokenError as e:
        raise JwtError('Invalid token. Please log in again.')
    
def verifyAuthorization(request):
    token_bearer = request.headers.get('Authorization')
    if token_bearer == None:
        return 'Authorization not set.', 401
    try:
        decode_token(token_bearer.replace('Bearer ', ''))
        return 'Ok', 200
    except JwtError as err:
        return str(err), 401
    except Exception as e:
        return f"Internal Server Error\n {e}", 500

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