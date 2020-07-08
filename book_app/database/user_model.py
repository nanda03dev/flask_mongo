from . import mongo_db
import json
from bson import ObjectId
from . import query

USER_COLLECTION = "users"


def collection():
    """Returns mongodb.collection"""

    return mongo_db.db[USER_COLLECTION]


def find_by_id(id):
    return query.find_one(USER_COLLECTION, {"_id": id})



def find_one(find_dict):
    return query.find_one(USER_COLLECTION, find_dict)


def insert_one(data, document=True):
    user = query.insert_one(USER_COLLECTION, data)
    return user


def insert_many(data):
    users = query.insert_one(USER_COLLECTION, data)
    return users


def find_all(query_dict, select_dict={}):
    list_of_users = query.find_all(USER_COLLECTION, query_dict, select_dict)
    return list_of_users


def find_all_for_stream(query_dict, select_dict={}):
    list_of_users = query.find_all_for_stream(
        USER_COLLECTION, query_dict, select_dict)
    return list_of_users
