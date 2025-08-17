import uuid
import qrcode, os
from qrcode.image.styledpil import StyledPilImage
from handlers.image_configuration_handler import image_configuration
from handlers.qr_styles_handler import get_drawer, get_color_mask
from handlers.qr_styles_handler import style_inner_eyes, style_outer_eyes


def generate_calendar_qr(event_name, dtstart, dtend, location, description, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path=None, data_solid_color=None, data_start_color=None, data_end_color=None, data_mask_image_path=None, inner_solid_color=None, inner_start_color=None, inner_end_color=None, inner_mask_image_path=None, outer_solid_color=None, outer_start_color=None, outer_end_color=None, outer_mask_image_path=None):
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
    
    # Handles image configuration
    if image_path:
        temp_image_path = image_configuration(image_path)

    # Module drawer and color mask for the data
    module_drawer_data = get_drawer(data_shape)
    color_mask_data = get_color_mask(qr_style_data, data_solid_color, data_start_color, data_end_color, data_mask_image_path)

    # Module drawer and color mask for the inner and outer eyes
    module_drawer_inner = get_drawer(inner_eye_shape)
    color_mask_inner = get_color_mask(inner_eye_style, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path)
    module_drawer_outer = get_drawer(outer_eye_shape)
    color_mask_outer = get_color_mask(outer_eye_style, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)

    # Generates QR COde
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(calendar_data)
    qr.make(fit=True)

    qr_inner_eyes_img = qr.make_image(image_factory=StyledPilImage,
                            eye_drawer=module_drawer_inner,
                            color_mask=color_mask_inner).convert("RGB")
    qr_outer_eyes_img = qr.make_image(image_factory=StyledPilImage,
                                eye_drawer=module_drawer_outer,
                                color_mask=color_mask_outer).convert("RGB")

    if image_path:
        qr_img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=temp_image_path, module_drawer=module_drawer_data, color_mask=color_mask_data).convert("RGB")
    else:
        qr_img = qr.make_image(image_factory=StyledPilImage, module_drawer=module_drawer_data, color_mask=color_mask_data).convert("RGB")

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Create inner and outer eye masks
    inner_eye_mask = style_inner_eyes(qr_img, box_size=10, quiet_zone=4)
    outer_eye_mask = style_outer_eyes(qr_img, box_size=10, quiet_zone=4)

    # Start with the base image
    final_image = qr_img.copy()

    # Paste the inner eyes
    final_image.paste(qr_inner_eyes_img, (0, 0), inner_eye_mask)

    # Paste the outer eyes
    final_image.paste(qr_outer_eyes_img, (0, 0), outer_eye_mask)
    
    qr_code_filename = f"calendar_qr_{uuid.uuid4().hex[:8]}.png"
    path = os.path.join(output_folder, qr_code_filename)

    # Save the QR code image
    final_image.save(path, format='PNG')

    # Clean up the temporary image file
    if image_path:
        os.remove(temp_image_path)

    return path