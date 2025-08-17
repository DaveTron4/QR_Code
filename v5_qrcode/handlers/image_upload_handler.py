from .configuration_handler import allowed_file
import os
from werkzeug.utils import secure_filename

def image_upload(file, upload_folder):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return file_path
    return None