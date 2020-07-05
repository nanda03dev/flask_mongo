import json
from flask import Response

SUCCESS_CODE = 200
BAD_REQUEST = 400


def success(data):
    data = {
        "statusCode": SUCCESS_CODE,
        "data": data
    }
    return Response(json.dumps(data, default=str), mimetype='application/json', status=SUCCESS_CODE)


def bad_request(error):
    data = {
        "statusCode": BAD_REQUEST,
        "error": data
    }
    return Response(json.dumps(error, default=str), mimetype='application/json', status=BAD_REQUEST)
