import os
from flask import Flask

def configuration():
    app = Flask(__name__, template_folder="../../templates", static_folder="../../static")

    # Base directory where app is running
    base_dir = os.path.abspath(os.path.join(app.root_path, "../../"))

    # Absolute paths
    UPLOAD_FOLDER = os.path.join(base_dir, "static", "uploads")
    OUTPUT_FOLDER = os.path.join(base_dir, "static", "output")
    

    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    return app

# Helper function to check allowed file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS