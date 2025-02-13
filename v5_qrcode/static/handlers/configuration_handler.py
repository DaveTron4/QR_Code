import os
from flask import Flask

def configuration():
    app = Flask(__name__, template_folder="../../templates", static_folder="../../static")

    # Configuration for uploaded files
    UPLOAD_FOLDER = "static/uploads"
    OUTPUT_FOLDER = "static/output"
    

    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)
    return app

# Helper function to check allowed file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS