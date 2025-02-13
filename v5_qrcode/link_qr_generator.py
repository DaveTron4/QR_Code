import qrcode
from qrcode.image.styledpil import StyledPilImage
import os

from static.handlers.image_configuration_handler import image_configuration

def generate_link_qr(link, image_path = None):
    # Handles image configuration
    if image_path:
        temp_image_path = image_configuration(image_path)

    # Generates QR COde
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(link)
    if image_path:
        qr_img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=temp_image_path)
    else:
        qr_img = qr.make_image()

    # THIS IS IMPORTANT : without this an error is shown
    # Save the QR Code to the 'output' directory
    output_dir = f"static/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    qr_code_filename = f"link_qr.png"
    path = os.path.join(output_dir, qr_code_filename)

    # Save the QR code image
    qr_img.save(path, format='PNG') 

    # Clean up the temporary image file
    if image_path:
        os.remove(temp_image_path)

    return path