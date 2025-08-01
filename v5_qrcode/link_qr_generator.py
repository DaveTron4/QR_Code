import qrcode, os, uuid
from qrcode.image.styledpil import StyledPilImage
from static.handlers.image_configuration_handler import image_configuration
from static.handlers.qr_styles_handler import get_drawer, get_color_mask
from static.handlers.qr_styles_handler import style_inner_eyes, style_outer_eyes

def generate_link_qr(link, data_shape=None, qr_style_data=None, inner_eye_shape=None, inner_eye_style=None, outer_eye_shape=None, outer_eye_style=None, image_path=None, data_solid_color=None, data_start_color=None, data_end_color=None, data_mask_image_path=None, inner_solid_color=None, inner_start_color=None, inner_end_color=None, inner_mask_image_path=None, outer_solid_color=None, outer_start_color=None, outer_end_color=None, outer_mask_image_path=None):
    # Handles image configuration
    if image_path:
        temp_image_path = image_configuration(image_path)

    # Get the module drawer and color mask based on the provided styles
    module_drawer_data = get_drawer(data_shape)
    color_mask_data = get_color_mask(qr_style_data, data_solid_color, data_start_color, data_end_color, data_mask_image_path)

    module_drawer_inner = get_drawer(inner_eye_shape)
    color_mask_inner = get_color_mask(inner_eye_style, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path)

    module_drawer_outer = get_drawer(outer_eye_shape)
    color_mask_outer = get_color_mask(outer_eye_style, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)

    # Generates QR COde
    qr = qrcode.QRCode(version=5, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=20, border=5)
    qr.add_data(link)
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


    # THIS IS IMPORTANT : without this an error is shown
    # Save the QR Code to the 'output' directory
    output_dir = f"static/output/"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create inner and outer eye masks
    inner_eye_mask = style_inner_eyes(qr_img, box_size=20, quiet_zone=5)
    outer_eye_mask = style_outer_eyes(qr_img, box_size=20, quiet_zone=5)

    # Start with the base image
    final_image = qr_img.copy()

    # Paste the inner eyes
    final_image.paste(qr_inner_eyes_img, (0, 0), inner_eye_mask)

    # Paste the outer eyes
    final_image.paste(qr_outer_eyes_img, (0, 0), outer_eye_mask)

    qr_code_filename = f"link_qr_{uuid.uuid4().hex[:8]}.png"
    path = os.path.join(output_dir, qr_code_filename)

    # Save the QR code image
    # qr_img.save(path, format='PNG') 
    final_image.save(path, format='PNG')

    # Clean up the temporary image file
    if image_path:
        os.remove(temp_image_path)

    return path