import re
from flask import render_template, url_for
from vcard_generator import generate_vcard_qr
import os


def vcard_handler(name, phone, email, image_path = None):
    # Validate phone number (e.g., must be exactly 10 digits)
    if not re.fullmatch(r"\d{10}", phone):
        return render_template("index.html", qr_code_url=None, error="Invalid phone number! Please enter a 10-digit number.")

    # Generate the QR code with or without the image
    qr_code_path = generate_vcard_qr(name, phone, email, image_path)  # Pass the image path to the function if available
    qr_code_filename = os.path.basename(qr_code_path)
    qr_code_url = url_for("static", filename=f"output/{qr_code_filename}")

    # Clean up the uploaded image after QR code generation
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    return qr_code_url
    
