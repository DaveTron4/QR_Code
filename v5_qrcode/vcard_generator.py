import PIL
from PIL import Image, ImageDraw
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer
from  qrcode.image.styles.colormasks import SolidFillColorMask
import vobject
import os

def generate_vcard_qr(name, phone, email):

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

    seriealized_vcard = vcard.serialize()

    # Generate QR Code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(seriealized_vcard)
    qr_img = qr.make_image()



    # THIS IS IMPORTANT : without this an error is shown
    # Save the QR Code to the 'output' directory
    output_dir = f"v5_qrcode/static/output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # Create the directory if it doesn't exist

    path = os.path.join(output_dir, f"{name}_qr.png")
    qr_img.save(path)

    return path