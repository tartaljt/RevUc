from flask import Flask, request, jsonify, send_file, session
from flask_socketio import SocketIO, send, join_room, leave_room
from flask_cors import CORS, cross_origin
import json
import psycopg2
import datetime
import boto3

users = []

app = Flask(__name__)
app.debug = True
app.host = 'localhost'
app.config['SECRET_KEY'] = 'mysecret'
cors = CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000","http://localhost:5173","http://127.0.0.1:5173"]}})

credentials = json.loads(boto3.client(
    service_name='secretsmanager',
    region_name='us-east-2'
).get_secret_value(SecretId='rds-db-credentials/cluster-QWGHP2U3X2JAX5OS3G3GAG2G2Q/mcs/1708810086121')['SecretString'])

class RDSDatabase:
    def __init__(self, user, password, database, host):
        self.user = user
        self.password = password
        self.database = database
        self.host = host

database = RDSDatabase(
    credentials['username'], 
    credentials['password'], 
    "postgres", 
    credentials['host']
)

import providers_api
import schedule_api
#socket = SocketIO(app, cors_allowed_origins="*")

database = psycopg2.connect(f"dbname={database.database} user={database.user} password={database.password} host={database.host}")

def updateUsers(user_id: int, socket_id: str):
    for user in users:
        if user['id'] == user_id:
            user['socket'] = socket_id
            return
        else:
            users.append({'id': user_id, 'socket': socket_id})

#def sendMessageToDatabase(fromUser, toUser, message):
#    database_cursor = database.cursor()
#    database_cursor.execute(f"INSERT INTO rev_chats (fromuser, touser, msg, timesent, datesent) VALUES ({fromUser}, {toUser}, '{message}', '{datetime.datetime.now().time()}', '{datetime.date.today()}');")
#    database.commit()
#    database_cursor.close()
#    return None

#def getMessageFromDatabase(fromUser, toUser, numMessages = 1): 
#    database_cursor = database.cursor()
#    database_cursor.execute(f"SELECT msg FROM rev_chats WHERE fromuser = {fromUser} AND touser = {toUser} ORDER BY timesent DESC;")
#    messages = database_cursor.fetchmany(numMessages)
#    database_cursor.close()
#    return messages


def sendJournalToDatabase(user_id, journal_data):
    if journal_data == "" or journal_data == None:
        return None
    database_cursor = database.cursor()
    database_cursor.execute(f"INSERT INTO rev_journals (userid, entry, timesent, datesent) VALUES (%s, %s, %s, %s);", (user_id, journal_data, datetime.datetime.now().time(), datetime.date.today()))
    database.commit()
    database_cursor.close()
    return None

@app.route('/journal', methods=["POST"])
def handleJournal():
    data = request.json
    sendJournalToDatabase(data["userID"], data["journal"])
    print(data)
    return jsonify({"status": "success"})

    