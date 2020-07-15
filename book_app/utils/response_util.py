import json
from flask import Response
import csv
import io


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


def iter_csv(data, is_dict):
    line = io.StringIO()
    writer = csv.writer(line)
    print("csv_line 1", line)
    headers = False

    for csv_line in data:
        if is_dict:
            if headers == False:
                writer.writerow(csv_line.keys())
            csv_line = csv_line.values()

        writer.writerow(csv_line)
        headers = True
        line.seek(0)
        yield line.read()
        line.truncate(0)
        line.seek(0)  # required for Python 3


def csv_response(data, is_dict=False):
    response = Response(iter_csv(data, is_dict), mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    return response
