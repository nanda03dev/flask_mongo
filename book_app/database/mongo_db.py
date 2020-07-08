import pymongo
from flask import g
from pymongo.errors import ServerSelectionTimeoutError
import sys
from threading import Timer

MAX_RETRY = 3


HOST = "mongodb://localhost:27017/"
MAX_POOL_SIZE = 200
WAIT_QUEUE_TIMEOUT_MS = 100
DATABASE_NAME = "book_app"
SERVER_SELECTION_TIMEOUT_MS = 2000
CONNECT_TIME_OUT_MS = 2000


def start(Iteration=0):
    myclient = pymongo.MongoClient(
        host=HOST,
        maxPoolSize=MAX_POOL_SIZE,
        waitQueueTimeoutMS=WAIT_QUEUE_TIMEOUT_MS,
        serverSelectionTimeoutMS=SERVER_SELECTION_TIMEOUT_MS,
        connectTimeoutMS=CONNECT_TIME_OUT_MS)

    print("Creating Mongo DB connection...")
    try:
        info = myclient.server_info()  # Forces a call.
        mydb = myclient[DATABASE_NAME]
        global db
        db = mydb
        print("Mongo DB started successfully")
    except ServerSelectionTimeoutError:
        print("server is down , will try after 2 sec ")
        Iteration = int(Iteration)
        if(Iteration < MAX_RETRY):
            Iteration = Iteration +1
            Timer(2.0, start,(str(Iteration))).start()
        else:
            print("Mongo db connection failed , retry count reached Max count")

