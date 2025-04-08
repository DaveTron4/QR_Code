import qrcode
from qrcode.image.styledpil import StyledPilImage
import vobject
import os
from static.handlers.image_configuration_handler import image_configuration


def generate_vcard_qr(name, phone, email, image_path = None):

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

    # Generate QR Code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(seriealized_vcard)
    if image_path:
        # TODO: Add module drawer that change with user input and masks as well
        qr_img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=temp_image_path)
    else:
        qr_img = qr.make_image()


    # THIS IS IMPORTANT : without this an error is shown
    # Save the QR Code to the 'output' directory
    output_dir = f"static/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn't exist
    
    qr_code_filename = f"{name}_qr.png"
    path = os.path.join(output_dir, qr_code_filename)

    # Save the QR code image
    qr_img.save(path, format='PNG')  # You can save the QR code in PNG format since it doesn't need transparency

    # Clean up the temporary image file
    if image_path:
        os.remove(temp_image_path)

    return path   