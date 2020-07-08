from flask import request,Blueprint
import json
import io
import csv
import re
from ..database import user_model
from .. import utils

response = utils.response

user_bp = Blueprint('user_template', __name__)

@user_bp.route('/book/insert', methods=["POST"])

@user_bp.route('/user/insert', methods=["POST"])
def user_insert():
    req_body = request.get_json()
    result = user_model.insert_one(req_body)
    return response.success(result)


@user_bp.route('/user/insertmany', methods=["POST"])
def user_insert_many():
    req_body = request.files["file"]

    stream = io.StringIO(req_body.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)

    headers = next(csv_input)
    headers = [re.sub("\W+","",txt) for txt in headers]
    result = []
    for row in csv_input:
        each_document = dict(zip(headers, row))
        inserted_id = user_model.insert_one(each_document, document=False)
        result.append(inserted_id)

    stream.seek(0)
    return response.success({"totalInsertedCount": len(result)})


@user_bp.route('/user', methods=["POST"])
def user_get_all():
    find_dict = request.get_json()["findObj"]
    select_dict = request.get_json()["selectObj"]
    result = user_model.find_all(find_dict, select_dict)
    return response.success(result)


@user_bp.route('/user/csv', methods=["POST"])
def user_get_all_csv():
    find_dict = request.get_json().get("findObj", {})
    select_dict = request.get_json().setdefault("selectObj", {})
    result = user_model.find_all_for_stream(find_dict, select_dict)
    return response.csv_response(data=result, is_dict=True)

@user_bp.route('/user/login', methods=["POST"])
def user_login():
    req_body = request.get_json()
    query = {
        "EMail": req_body.get("email"),
        "Password": req_body.get("password")
    }
    result = user_model.find_one(query)
    return response.success(result)