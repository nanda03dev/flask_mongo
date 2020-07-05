import json
from ..database import book_model
from flask import request
from . import routes
from .. import response
import io
import csv

@routes.route('/book/new', methods=["POST"])
def add_new_book():
    req_body = request.get_json()
    result = book_model.insert_one(req_body)
    return response.success(result)

@routes.route('/book/insertmany', methods=["POST"])
def insertmany():
    req_body = request.files["file"]

    stream = io.StringIO(req_body.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)

    headers = next(csv_input)
    result = []
    for row in csv_input:
        each_document = dict(zip(headers,row))
        inserted_id = book_model.insert_one(each_document,document=False)
        result.append(inserted_id)

    stream.seek(0)
    return response.success(result)


@routes.route('/book', methods=["POST"])
def get_all():
    req_body = request.get_json()
    result = book_model.find_all(req_body)
    return response.success(result)
