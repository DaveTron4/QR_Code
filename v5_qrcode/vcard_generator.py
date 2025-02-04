from PIL import Image, ImageDraw
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer
from  qrcode.image.styles.colormasks import SolidFillColorMask
import vobject
import os
import base64

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

    def add_corners(im, rad):
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2 - 1, rad * 2 - 1), fill=255)
        alpha = Image.new('L', im.size, 255)
        w, h = im.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        im.putalpha(alpha)
        return im

    if image_path:
        # Check the file extension
        file_extension = os.path.splitext(image_path)[1].lower()
        image = Image.open(image_path)
        # Add corners as you did previously
        image = add_corners(image, 50)
        if file_extension == '.png':
            # If the file is PNG, preserve the transparency (RGBA)
            image = image.convert("RGBA")
        elif file_extension == '.jpeg' or file_extension == '.jpg':
            # If the file is JPEG, convert to RGB (no transparency)
            image = image.convert("RGB")
        # Save the modified image to a temporary file
        temp_image_path = "temp_image.png"  # You can change the file extension if needed
        image.save(temp_image_path)

    # Generate QR Code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(seriealized_vcard)
    if image_path:
        qr_img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=temp_image_path)
    else:
        qr_img = qr.make_image()


    # THIS IS IMPORTANT : without this an error is shown
    # Save the QR Code to the 'output' directory
    output_dir = f"v5_qrcode/static/output"
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