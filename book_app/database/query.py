from . import mongo_db
import json
from bson import ObjectId


def collection(COLLECTION_NAME):
    """Returns mongodb.collection"""

    return mongo_db.db[COLLECTION_NAME]


def find_by_id(COLLECTION_NAME,id):
    """
    The function to return document for given objectId

    Parameters:
        id (ObjectId): document object id

    Returns:
        Dict: A item document 
    """

    return collection(COLLECTION_NAME).find_one({"_id": id})

def find_one(COLLECTION_NAME,find_dict):
    """
    The function to return document for given objectId

    Parameters:
        find_dict : document object 

    Returns:
        Dict: A item document 
    """

    return collection(COLLECTION_NAME).find_one(find_dict)

def insert_one(COLLECTION_NAME, data, document=True):
    """
    The function to insert new document

    Parameters:
        data (dict):  new item dict

    Returns:
        Dict: A item document 
    """

    x = collection(COLLECTION_NAME).insert_one(data)
    item = x.inserted_id
    if document:
        item = find_by_id(COLLECTION_NAME, x.inserted_id)

    return item


def insert_many(COLLECTION_NAME, data):
    """
    The function to insert many document

    Parameters:
        data (dict):  new item dict

    Returns:
        Dict: A item document 
    """

    x = collection(COLLECTION_NAME).insert_many(data)
    item = find_by_id(x.inserted_id)
    return item


def find_all(COLLECTION_NAME, query_dict, select_dict={}):
    """
    The function to returns list of items 

    Parameters:
        query_dict (dict):  query dict to find data

    Returns:
        List: List of items
    """

    if "_id" in query_dict:
        query_dict["_id"] = ObjectId(query_dict["_id"])

    list_of_items = collection(COLLECTION_NAME).find(query_dict, select_dict)
    list_of_items = [each_item for each_item in list_of_items]
    return list_of_items

def find_all_for_stream(COLLECTION_NAME, query_dict, select_dict={}):
    """
    The function to returns list of items 

    Parameters:
        query_dict (dict):  query dict to find data

    Returns:
        List: List of items
    """

    if "_id" in query_dict:
        query_dict["_id"] = ObjectId(query_dict["_id"])

    list_of_items = collection(COLLECTION_NAME).find(query_dict, select_dict)
    return list_of_items
