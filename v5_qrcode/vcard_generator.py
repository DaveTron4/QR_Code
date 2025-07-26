import qrcode, os, vobject
from qrcode.image.styledpil import StyledPilImage
from static.handlers.image_configuration_handler import image_configuration
from static.handlers.qr_styles_handler import get_drawer, get_color_mask
from static.handlers.qr_styles_handler import style_inner_eyes, style_outer_eyes

from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *


def generate_vcard_qr(name, phone, email, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path = None, data_solid_color=None, data_start_color=None, data_end_color=None, data_mask_image_path=None, inner_solid_color=None, inner_start_color=None, inner_end_color=None, inner_mask_image_path=None, outer_solid_color=None, outer_start_color=None, outer_end_color=None, outer_mask_image_path=None):

    # vCard Version
    vcard = vobject.vCard()
    vcard.add("version")
    vcard.version.value = "3.0"

    # Name
    vcard.add("fn")
    vcard.fn.value = name

    # Phone
    vcard.add("tel")
    vcard.tel.value = phone
    vcard.tel.type_param = "MOBILE"

    # Email
    vcard.add("email")
    vcard.email.value =email
    vcard.email.type_param = "INTERNET"

    # TODO: this will have to go on the image_configuration_handler.py script
    # Add Image if provided
    # if image_path:
    #     try:
    #         with open(image_path, "rb") as image_file:
    #             encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    #             photo = vcard.add("photo")
    #             photo.value = f"data:image/jpeg;base64,{encoded_image}"
    #             photo.encoding_param = "BASE64"
    #             photo.type_param = "JPEG"
    #     except Exception as e:
    #         print(f"Error loading image: {e}")

    seriealized_vcard = vcard.serialize()

    if image_path:
        temp_image_path = image_configuration(image_path)

    # Get the module drawer and color mask based on the provided styles

    print(f"Data Shape: {data_shape}, Data Style: {qr_style_data}, Inner Eye Shape: {inner_eye_shape}, Inner Eye Style: {inner_eye_style}, Outer Eye Shape: {outer_eye_shape}, Outer Eye Style: {outer_eye_style}")
    print(f"Data Solid Color: {data_solid_color}, Data Start Color: {data_start_color}, Data End Color: {data_end_color}, Data Mask Image Path: {data_mask_image_path}")
    print(f"Inner Solid Color: {inner_solid_color}, Inner Start Color: {inner_start_color}, Inner End Color: {inner_end_color}, Inner Mask Image Path: {inner_mask_image_path}")
    print(f"Outer Solid Color: {outer_solid_color}, Outer Start Color: {outer_start_color}, Outer End Color: {outer_end_color}, Outer Mask Image Path: {outer_mask_image_path}")

    module_drawer_data = get_drawer(data_shape)
    color_mask_data = get_color_mask(qr_style_data, data_solid_color, data_start_color, data_end_color, data_mask_image_path)

    module_drawer_inner = get_drawer(inner_eye_shape)
    color_mask_inner = get_color_mask(inner_eye_style, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path)

    module_drawer_outer = get_drawer(outer_eye_shape)
    color_mask_outer = get_color_mask(outer_eye_style, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)

    # Generate QR Code
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(seriealized_vcard)
    qr.make(fit=True)

    qr_inner_eyes_img = qr.make_image(image_factory=StyledPilImage,
                            eye_drawer=VerticalBarsDrawer(),
                            color_mask=SolidFillColorMask(front_color=(182, 174, 211))).convert("RGB")

    qr_outer_eyes_img = qr.make_image(image_factory=StyledPilImage,
                                eye_drawer=HorizontalBarsDrawer(),
                                color_mask=SolidFillColorMask(front_color=(63, 42, 86))).convert("RGB")


    if image_path:
        qr_img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=temp_image_path, module_drawer=module_drawer_data, color_mask=color_mask_data).convert("RGB")
    else:
        qr_img = qr.make_image(image_factory=StyledPilImage, module_drawer=module_drawer_data, color_mask=color_mask_data).convert("RGB")


    # THIS IS IMPORTANT : without this an error is shown
    # Save the QR Code to the 'output' directory
    output_dir = f"static/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn't exist
    
    # Create inner and outer eye masks
    inner_eye_mask = style_inner_eyes(qr_img, box_size=20, quiet_zone=5)
    outer_eye_mask = style_outer_eyes(qr_img, box_size=20, quiet_zone=5)

    # Start with the base image
    final_image = qr_img.copy()

    # Paste the inner eyes
    final_image.paste(qr_inner_eyes_img, (0, 0), inner_eye_mask)

    # Paste the outer eyes
    final_image.paste(qr_outer_eyes_img, (0, 0), outer_eye_mask)

    qr_code_filename = f"{name}_qr.png"
    path = os.path.join(output_dir, qr_code_filename)

    # Save the QR code image
    qr_img.save(path, format='PNG')  # You can save the QR code in PNG format since it doesn't need transparency

    # Clean up the temporary image file
    if image_path:
        os.remove(temp_image_path)

    return path   