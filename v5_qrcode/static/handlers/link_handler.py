from flask import url_for
from link_qr_generator import generate_link_qr
import os


def link_handler(link, image_path = None):
    # Generate the QR code with or without the image
    qr_code_path = generate_link_qr(link, image_path)  # Pass the image path to the function if available

    # Clean up the uploaded image after QR code generation
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    return qr_code_path
    