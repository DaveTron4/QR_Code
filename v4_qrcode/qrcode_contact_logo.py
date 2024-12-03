import PIL
from PIL import Image, ImageDraw
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, CircleModuleDrawer, SquareModuleDrawer
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer
from  qrcode.image.styles.colormasks import SolidFillColorMask
import vobject

if __name__ == "__main__":

    # vCard Version
    vcard = vobject.vCard()
    vcard.add("version")
    vcard.version.value = "3.0"

    # Name
    vcard.add("fn")
    vcard.fn.value = "test name"

    # Phone
    vcard.add("tel")
    vcard.tel.value = "404 965-9874"
    vcard.tel.type_param = "MOBILE"

    # Email
    vcard.add("email")
    vcard.tel.value = "example@gmail.com"
    vcard.tel.type_param = "INTERNET"

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


    im = Image.open('v4_qrcode/assets/logo.png')
    im = add_corners(im, 50)
    im = im.convert("RGBA")
    im.save('v4_qrcode/assets/logo.png')

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(seriealized_vcard)
    qr_img = qr.make_image(image_factory=StyledPilImage,
                        embeded_image_path="v4_qrcode/assets/logo.png")
    
    
    qr_img.save('v4_qrcode/qr_output/qrcode_vcard_logo.png')
    qr_img

    
