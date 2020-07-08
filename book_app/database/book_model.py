from . import mongo_db
import json
from bson import ObjectId
from . import query

BOOK_COLLECTION = "books"


def collection():
    """Returns mongodb.collection"""

    return mongo_db.db[BOOK_COLLECTION]


def find_by_id(id):
    return query.find_one(BOOK_COLLECTION, {"_id": id})


def insert_one(data, document=True):
    book = query.insert_one(BOOK_COLLECTION, data)
    return book


def insert_many(data):
    books = query.insert_one(BOOK_COLLECTION, data)
    return books


def find_all(query_dict, select_dict={}):
    list_of_books = query.find_all(BOOK_COLLECTION, query_dict, select_dict)
    return list_of_books


def find_all_for_stream(query_dict, select_dict={}):
    list_of_books = query.find_all_for_stream(
        BOOK_COLLECTION, query_dict, select_dict)
    return list_of_books
