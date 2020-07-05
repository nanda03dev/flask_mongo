from . import mongo_db
import json
from bson import ObjectId

BOOK_COLLECTION = "books"


def collection():
    """Returns mongodb.collection"""

    return mongo_db.db[BOOK_COLLECTION]


def find_by_id(id):
    """
    The function to return document for given objectId

    Parameters:
        id (ObjectId): document object id

    Returns:
        Dict: A Book document 
    """

    return collection().find_one({"_id": id})


def insert_one(data, document=True):
    """
    The function to insert new document

    Parameters:
        data (dict):  new book dict

    Returns:
        Dict: A Book document 
    """

    x = collection().insert_one(data)
    book = x.inserted_id
    if document:
        book = find_by_id(x.inserted_id)

    return book

def insert_many(data):
    """
    The function to insert many document

    Parameters:
        data (dict):  new book dict

    Returns:
        Dict: A Book document 
    """

    x = collection().insert_one(data)
    book = find_by_id(x.inserted_id)
    return book

def find_all(query_dict):
    """
    The function to returns list of books 

    Parameters:
        query_dict (dict):  query dict to find data

    Returns:
        List: List of books
    """

    if "_id" in query_dict:
        query_dict["_id"] = ObjectId(query_dict["_id"])

    list_of_books = mongo_db.db[BOOK_COLLECTION].find(query_dict)
    list_of_books = [each_book for each_book in list_of_books]
    return list_of_books
