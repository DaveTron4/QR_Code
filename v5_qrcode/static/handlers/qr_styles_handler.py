from qrcode.image.styles.moduledrawers import *
from qrcode.image.styles.colormasks import *
import PIL
from PIL import Image, ImageDraw

# Function to get the appropriate module drawer based on the QR shape
def get_drawer(qr_shape):
    if qr_shape =="none":
        return None
    elif qr_shape == "rounded":
        return RoundedModuleDrawer()
    elif qr_shape == "gapped_square":
        return GappedSquareModuleDrawer()
    elif qr_shape == "square":
        return SquareModuleDrawer()
    elif qr_shape == "circle":
        return CircleModuleDrawer()
    elif qr_shape == "vertical_bar":
        return VerticalBarsDrawer()
    elif qr_shape == "horizontal_bar":
        return HorizontalBarsDrawer()
    else:
        raise ValueError(f"Unknown QR shape: {qr_shape}")

# Function to convert hex color to RGB tuple
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
 
# Function to get the color mask based on the style and colors provided
def get_color_mask(qr_style, solid_color=None, start_color=None, end_color=None, mask_image_path=None):
    if qr_style == "none" or qr_style is None:
        return SolidFillColorMask(
            back_color=(255, 255, 255),
            front_color=(0, 0, 0)
        )
    if qr_style == "SolidFillColorMask" and solid_color:
        return SolidFillColorMask(
            back_color=(255, 255, 255),
            front_color=hex_to_rgb(solid_color)
        )
    elif qr_style == "RadialGradiantColorMask" and start_color and end_color:
        return RadialGradiantColorMask(
            back_color=(255, 255, 255),
            center_color=hex_to_rgb(start_color),
            edge_color=hex_to_rgb(end_color)
        )

    elif qr_style == "SquareGradiantColorMask" and start_color and end_color:
        return SquareGradiantColorMask(
            back_color=(255, 255, 255),
            center_color=hex_to_rgb(start_color),
            edge_color=hex_to_rgb(end_color)
        )
    elif qr_style == "HorizontalGradiantColorMask" and start_color and end_color:
        return HorizontalGradiantColorMask(
            back_color=(255, 255, 255),
            left_color=hex_to_rgb(start_color),
            right_color=hex_to_rgb(end_color)
        )
    elif qr_style == "VerticalGradiantColorMask" and start_color and end_color:
        return VerticalGradiantColorMask(
            back_color=(255, 255, 255),
            top_color=hex_to_rgb(start_color),
            bottom_color=hex_to_rgb(end_color)
        )
    elif qr_style == "ImageColorMask" and mask_image_path:
        return ImageColorMask(color_mask_path=mask_image_path)

    else:
        raise ValueError(f"Invalid or missing parameters for color mask style: {qr_style}")

def style_inner_eyes(img):
  img_size = img.size[0]
  eye_size = 70 #default
  quiet_zone = 40 #default
  mask = Image.new('L', img.size, 0)
  draw = ImageDraw.Draw(mask)
  draw.rectangle((60, 60, 90, 90), fill=255) #top left eye
  draw.rectangle((img_size-90, 60, img_size-60, 90), fill=255) #top right eye
  draw.rectangle((60, img_size-90, 90, img_size-60), fill=255) #bottom left eye
  return mask

def style_outer_eyes(img):
  img_size = img.size[0]
  eye_size = 70 #default
  quiet_zone = 40 #default
  mask = Image.new('L', img.size, 0)
  draw = ImageDraw.Draw(mask)
  draw.rectangle((40, 40, 110, 110), fill=255) #top left eye
  draw.rectangle((img_size-110, 40, img_size-40, 110), fill=255) #top right eye
  draw.rectangle((40, img_size-110, 110, img_size-40), fill=255) #bottom left eye
  draw.rectangle((60, 60, 90, 90), fill=0) #top left eye
  draw.rectangle((img_size-90, 60, img_size-60, 90), fill=0) #top right eye
  draw.rectangle((60, img_size-90, 90, img_size-60), fill=0) #bottom left eye  
  return mask  


