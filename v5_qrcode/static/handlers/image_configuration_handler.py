from PIL import Image, ImageDraw
import os


def image_configuration(image_path = None):
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

    return temp_image_path