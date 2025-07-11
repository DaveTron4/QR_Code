from .configuration_handler import allowed_file
import os
from werkzeug.utils import secure_filename


def image_upload(file, app):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)
        return file_path
    return None