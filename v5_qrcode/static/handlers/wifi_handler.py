from wifi_generator import generate_wifi_qr
import os


def wifi_handler(ssid, password, encryption, image_path = None):
    # Generate the QR code with or without the image
    qr_code_path = generate_wifi_qr(ssid, password, encryption, image_path)  # Pass the image path to the function if available

    # Clean up the uploaded image after QR code generation
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    return qr_code_path
    