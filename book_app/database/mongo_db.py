import pymongo

HOST = "mongodb://localhost:27017/"


def start():
    myclient = pymongo.MongoClient(HOST)
    mydb = myclient["mydatabase"]
    global db
    db = mydb
    
    print("Mongo DB started...")
