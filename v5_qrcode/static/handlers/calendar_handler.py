from calendar_generator import generate_calendar_qr
import os

def calendar_handler(event_name, dtstart, location, duration, description, image_path = None):
    # Generate the QR code with or without the image
    qr_code_path = generate_calendar_qr(event_name, dtstart, location, duration,description, image_path)  # Pass the image path to the function if available

    # Clean up the uploaded image after QR code generation
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    return qr_code_path