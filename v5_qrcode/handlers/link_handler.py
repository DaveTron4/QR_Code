from link_qr_generator import generate_link_qr
import os


def link_handler(link, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path):
    # Generate the QR code with or without the image
    qr_code_path = generate_link_qr(link, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)  # Pass the image path to the function if available

    # Clean up the uploaded image after QR code generation
    if image_path and os.path.exists(image_path):
        os.remove(image_path)

    return qr_code_path
    