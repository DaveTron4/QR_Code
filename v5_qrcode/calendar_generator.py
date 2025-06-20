import qrcode, os, uuid
from qrcode.image.styledpil import StyledPilImage
from static.handlers.image_configuration_handler import image_configuration
from static.handlers.qr_styles_handler import get_drawer


def generate_calendar_qr(event_name, dtstart, dtend, location, description, qr_shape, qr_style, image_path=None):
    # Ensure all data fields are stripped of extra whitespace
    event_name = event_name.strip()
    location = location.strip()
    description = description.strip()

    # Generate the calendar data in iCalendar format
    calendar_data = f"""BEGIN:VCALENDAR
VERSION:2.0
BEGIN:VEVENT
SUMMARY:{event_name}
DTSTART:{dtstart}
DTEND:{dtend}
LOCATION:{location}
DESCRIPTION:{description}
END:VEVENT
END:VCALENDAR"""
    
    module_drawer = get_drawer(qr_shape)
    
    # Handles image configuration
    if image_path:
        temp_image_path = image_configuration(image_path)
    
    # Generates QR COde
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(calendar_data)
    qr.make(fit=True)

    if image_path:
        # TODO: Add module drawer that change with user input and masks as well
        qr_img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=temp_image_path, module_drawer=module_drawer)
    else:
        qr_img = qr.make_image(image_factory=StyledPilImage, module_drawer=module_drawer)

    # THIS IS IMPORTANT : without this an error is shown
    # Save the QR Code to the 'output' directory
    output_dir = f"static/output/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    qr_code_filename = f"{event_name}_qr.png"
    path = os.path.join(output_dir, qr_code_filename)

    # Save the QR code image
    qr_img.save(path, format='PNG')

    # Clean up the temporary image file
    if image_path:
        os.remove(temp_image_path)

    return path