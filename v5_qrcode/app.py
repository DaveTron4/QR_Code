from flask import Flask, render_template, request, send_file, url_for, redirect, abort
from werkzeug.utils import secure_filename
import os
import re
from vcard_generator import generate_vcard_qr

app = Flask(__name__)

# Configuration for uploaded files
UPLOAD_FOLDER = "v5_qrcode/static/uploads"
OUTPUT_FOLDER = "v5_qrcode/static/output"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input from form
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")

        # Validate phone number (e.g., must be exactly 10 digits)
        if not re.fullmatch(r"\d{10}", phone):
            return render_template("index.html", qr_code_url=None, error="Invalid phone number! Please enter a 10-digit number.")

        # Handle image upload
        image_file = request.files.get("image")
        image_path = None
        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image_file.save(image_path)

        # Generate the QR code with or without the image
        qr_code_path = generate_vcard_qr(name, phone, email, image_path)  # Pass the image path to the function if available
        qr_code_filename = os.path.basename(qr_code_path)
        qr_code_url = url_for("static", filename=f"output/{qr_code_filename}")

        # Clean up the uploaded image after QR code generation
        if image_path and os.path.exists(image_path):
            os.remove(image_path)

        # Serve the QR code to the user
        return render_template("index.html", qr_code_url=qr_code_url)

    return render_template("index.html", qr_code_url=None)

@app.route('/download_qr/<filename>')
def download_qr(filename):
    output_dir = "v5_qrcode/static/output"
    file_path = os.path.join(output_dir, filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        abort(404)  # If not found, return 404 error

    # Serve the file for download
    try:
        # Send the file to the user
        response = send_file(file_path, as_attachment=True)

        # After sending the file, delete it
        os.remove(file_path)
        
        return response
    except Exception as e:
        abort(500)  # Handle any errors that might occur

if __name__ == "__main__":
    app.run(debug=True)
