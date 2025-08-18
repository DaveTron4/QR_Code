from datetime import timedelta
import os
import uuid
from flask import Flask, session, current_app
from dotenv import load_dotenv

def configuration():
    load_dotenv()  # Load variables from .env

    app = Flask(__name__, template_folder="../templates", static_folder="../static")
    app.secret_key = os.getenv("SECRET_KEY")

    base_dir = os.path.abspath(os.path.join(app.root_path, "../"))

    app.config["UPLOAD_FOLDER_BASE"] = os.path.join(base_dir, "static", "uploads")
    app.config["OUTPUT_FOLDER_BASE"] = os.path.join(base_dir, "static", "output")

    os.makedirs(app.config["UPLOAD_FOLDER_BASE"], exist_ok=True)
    os.makedirs(app.config["OUTPUT_FOLDER_BASE"], exist_ok=True)

    # Session timeout: 30 minutes
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

    return app


# Helper function to check allowed file extensions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_user_folders():
    # Assign a unique user_id if it's not already in the session
    if "user_id" not in session:
        session["user_id"] = str(uuid.uuid4())

    user_id = session["user_id"]

    # Create per-user folders
    upload_folder = os.path.join(current_app.config["UPLOAD_FOLDER_BASE"], user_id)
    output_folder = os.path.join(current_app.config["OUTPUT_FOLDER_BASE"], user_id)

    os.makedirs(upload_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    return upload_folder, output_folder