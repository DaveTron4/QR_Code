from .configuration_handler import allowed_file
import os
from werkzeug.utils import secure_filename


def image_upload(image_file, app):
    image_path = None
    if image_file and allowed_file(image_file.filename):
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        image_file.save(image_path)
    return image_path