from flask import request,Blueprint,current_app as app
import json
import io
import csv
import re
from ..database import book_model
from ..utils import response,file as file_util


book_bp = Blueprint('book', __name__)

@book_bp.route('/book/insert', methods=["POST"])
def book_insert():
    req_body = request.get_json()
    result = book_model.insert_one(req_body)
    return response.success(result)


@book_bp.route('/book/insertmany', methods=["POST"])
def book_insert_many():
    req_body = request.files["file"]

    stream = io.StringIO(req_body.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)

    headers = next(csv_input)
    headers = [re.sub("\W+","",txt) for txt in headers]
    result = []
    for row in csv_input:
        each_document = dict(zip(headers, row))
        inserted_id = book_model.insert_one(each_document, document=False)
        result.append(inserted_id)

    stream.seek(0)
    return response.success({"totalInsertedCount": len(result)})


@book_bp.route('/book', methods=["POST"])
def book_get_all():
    find_dict = request.get_json()["findObj"]
    select_dict = request.get_json()["selectObj"]
    result = book_model.find_all(find_dict, select_dict)
    return response.success(result)


@book_bp.route('/book/csv', methods=["POST"])
def book_get_all_csv():
    find_dict = request.get_json().get("findObj", {})
    select_dict = request.get_json().setdefault("selectObj", {})
    result = book_model.find_all_for_stream(find_dict, select_dict)
    return response.csv_response(data=result, is_dict=True)

@book_bp.route('/book/upload', methods=["POST"])
def upload_book():
    if 'file' not in request.files:
       response.bad_request("file is mandatory")
    result= file_util.write_file(request.files["file"])
    if result["status"]:
        return response.success("File upload succesfully")
    else:
        return response.bad_request("Upload failed")
