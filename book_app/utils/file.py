from werkzeug.utils import secure_filename
from .validation import allowed_file
from flask import current_app as app
import os

def write_file(file):
    if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = app.config['UPLOAD_FOLDER']
            file.save(os.path.join(upload_folder, filename))
            return {"status":True, "data":"Successfully uploaded"}
    else:
        return {"status":False, "data":"Upload failed"}