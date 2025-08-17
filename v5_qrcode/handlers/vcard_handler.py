import re
from flask import render_template, url_for
from vcard_generator import generate_vcard_qr
import os


def vcard_handler(name, phone, email, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path = None, data_solid_color=None, data_start_color=None, data_end_color=None, data_mask_image_path=None, inner_solid_color=None, inner_start_color=None, inner_end_color=None, inner_mask_image_path=None, outer_solid_color=None, outer_start_color=None, outer_end_color=None, outer_mask_image_path=None):
    # Validate phone number (e.g., must be exactly 10 digits)
    if not re.fullmatch(r"\d{10}", phone):
        return render_template("index.html", qr_code_url=None, error="Invalid phone number! Please enter a 10-digit number.")

    # Generate the QR code
    qr_code_path = generate_vcard_qr(name, phone, email, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path,data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)  # Pass the image path to the function if available

    # Clean up the uploaded image after QR code generation
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    return qr_code_path
    
