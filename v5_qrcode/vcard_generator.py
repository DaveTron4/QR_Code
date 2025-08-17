import uuid
import qrcode, os, vobject
from qrcode.image.styledpil import StyledPilImage
from static.handlers.image_configuration_handler import image_configuration
from static.handlers.qr_styles_handler import get_drawer, get_color_mask
from static.handlers.qr_styles_handler import style_inner_eyes, style_outer_eyes

def generate_vcard_qr(name, phone, email, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path = None, data_solid_color=None, data_start_color=None, data_end_color=None, data_mask_image_path=None, inner_solid_color=None, inner_start_color=None, inner_end_color=None, inner_mask_image_path=None, outer_solid_color=None, outer_start_color=None, outer_end_color=None, outer_mask_image_path=None):

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

    # Module drawer and color mask for the data
    module_drawer_data = get_drawer(data_shape)
    color_mask_data = get_color_mask(qr_style_data, data_solid_color, data_start_color, data_end_color, data_mask_image_path)

    # Module drawer and color mask for the inner and outer eyes
    module_drawer_inner = get_drawer(inner_eye_shape)
    color_mask_inner = get_color_mask(inner_eye_style, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path)
    module_drawer_outer = get_drawer(outer_eye_shape)
    color_mask_outer = get_color_mask(outer_eye_style, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)

    # Generate QR Code
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=15, border=5)
    qr.add_data(seriealized_vcard)
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
    inner_eye_mask = style_inner_eyes(qr_img, box_size=15, quiet_zone=5)
    outer_eye_mask = style_outer_eyes(qr_img, box_size=15, quiet_zone=5)

    # Start with the base image
    final_image = qr_img.copy()

    # Paste the inner eyes
    final_image.paste(qr_inner_eyes_img, (0, 0), inner_eye_mask)

    # Paste the outer eyes
    final_image.paste(qr_outer_eyes_img, (0, 0), outer_eye_mask)

    qr_code_filename = f"vcard_qr_{uuid.uuid4().hex[:8]}.png"
    path = os.path.join(output_folder, qr_code_filename)

    # Save the QR code image
    final_image.save(path, format='PNG')  # You can save the QR code in PNG format since it doesn't need transparency

    # Clean up the temporary image file
    if image_path:
        os.remove(temp_image_path)

    return path   