from flask import render_template, request, send_file, render_template_string
from io import BytesIO
import os
from uuid import uuid4
from static.handlers.vcard_handler import vcard_handler
from static.handlers.configuration_handler import configuration
from static.handlers.image_upload_handler import image_upload
from static.handlers.link_handler import link_handler
from static.handlers.wifi_handler import wifi_handler
from static.handlers.calendar_handler import calendar_handler
from static.handlers.date_time_handler import handle_date_time
from static.handlers.qr_cleanup_handler import clear_output_folder

app = configuration()

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

#! Route for getting input from vcard form
@app.route("/generate_qr_vcard", methods=["GET", "POST"])
def generate_qr_vcard():
    if request.method == "POST":
        # Get user input from form
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        image_file = request.files.get("image")
        # Inputs for QR Data
        data_shape = request.form.get("data_shape")
        qr_style_data = request.form.get("qr_style_data")
        # Inputs for QR Inner eyes
        inner_eye_shape = request.form.get("inner_eye_shape")
        inner_eye_style = request.form.get("qr_style_inner")
        # Inputs for QR Outer eyes
        outer_eye_shape = request.form.get("outer_eye_shape")
        outer_eye_style = request.form.get("qr_style_outer")
        

        # Handle dynamic inputs
        # DATA
        data_solid_color = request.form.get("data_solid_color")
        data_start_color = request.form.get("data_start_color")
        data_end_color = request.form.get("data_end_color")
        data_mask_image_file = request.files.get("data_mask_image")

        # INNER
        inner_solid_color = request.form.get("inner_solid_color")
        inner_start_color = request.form.get("inner_start_color")
        inner_end_color = request.form.get("inner_end_color")
        inner_mask_image_file = request.files.get("inner_mask_image")

        # OUTER
        outer_solid_color = request.form.get("outer_solid_color")
        outer_start_color = request.form.get("outer_start_color")
        outer_end_color = request.form.get("outer_end_color")
        outer_mask_image_file = request.files.get("outer_mask_image")

        
        # Handle image upload
        image_path = image_upload(image_file, app)

        # Upload optional mask image (used for ImageColorMask)
        data_mask_image_path = image_upload(data_mask_image_file, app)
        inner_mask_image_path = image_upload(inner_mask_image_file, app)
        outer_mask_image_path = image_upload(outer_mask_image_file, app)

        # Handle vcard creation
        qr_code_url = vcard_handler(name, phone, email, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)
        filename = os.path.basename(qr_code_url)


        # Serve the QR code to the user
        return render_template("index.html", qr_code_url=qr_code_url, filename=filename, uuid=uuid4(), active_form = "vcard")


#! Route for getting input from link form
@app.route("/generate_qr_link", methods=["GET", "POST"])
def generate_qr_link():
    if request.method == "POST":
        # Clear the output folder before processing new QR codes
        clear_output_folder(app)

        # Get user input from form
        link = request.form.get("link")
        image_file = request.files.get("image")

        # Inputs for QR Data
        data_shape = request.form.get("data_shape")
        qr_style_data = request.form.get("qr_style_data")
        # Inputs for QR Inner eyes
        inner_eye_shape = request.form.get("inner_eye_shape")
        inner_eye_style = request.form.get("qr_style_inner")
        # Inputs for QR Outer eyes
        outer_eye_shape = request.form.get("outer_eye_shape")
        outer_eye_style = request.form.get("qr_style_outer")
        
        # Handle dynamic inputs
        # DATA
        data_solid_color = request.form.get("data_solid_color")
        data_start_color = request.form.get("data_start_color")
        data_end_color = request.form.get("data_end_color")
        data_mask_image_file = request.files.get("data_mask_image")

        # INNER
        inner_solid_color = request.form.get("inner_solid_color")
        inner_start_color = request.form.get("inner_start_color")
        inner_end_color = request.form.get("inner_end_color")
        inner_mask_image_file = request.files.get("inner_mask_image")

        # OUTER
        outer_solid_color = request.form.get("outer_solid_color")
        outer_start_color = request.form.get("outer_start_color")
        outer_end_color = request.form.get("outer_end_color")
        outer_mask_image_file = request.files.get("outer_mask_image")

        # Handle image upload
        image_path = image_upload(image_file, app)

        # Upload optional mask image (used for ImageColorMask)
        data_mask_image_path = image_upload(data_mask_image_file, app)
        inner_mask_image_path = image_upload(inner_mask_image_file, app)
        outer_mask_image_path = image_upload(outer_mask_image_file, app)

        # Handle link qr creation
        qr_code_url = link_handler(link, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)
        filename = os.path.basename(qr_code_url)

        return render_template("index.html", qr_code_url = qr_code_url, filename=filename, uuid=uuid4(), active_form = "link")

#! Route for getting imput from wifi form
@app.route("/generate_qr_wifi", methods=["GET", "POST"])
def generate_qr_wifi():
    if request.method == "POST":
        # Get user input from form
        ssid = request.form.get("ssid")
        password = request.form.get("password")
        encryption = request.form.get("encryption")
        image_file = request.files.get("image")

        # Inputs for QR Data
        data_shape = request.form.get("data_shape")
        qr_style_data = request.form.get("qr_style_data")
        # Inputs for QR Inner eyes
        inner_eye_shape = request.form.get("inner_eye_shape")
        inner_eye_style = request.form.get("qr_style_inner")
        # Inputs for QR Outer eyes
        outer_eye_shape = request.form.get("outer_eye_shape")
        outer_eye_style = request.form.get("qr_style_outer")
        
        # Handle dynamic inputs
        # DATA
        data_solid_color = request.form.get("data_solid_color")
        data_start_color = request.form.get("data_start_color")
        data_end_color = request.form.get("data_end_color")
        data_mask_image_file = request.files.get("data_mask_image")

        # INNER
        inner_solid_color = request.form.get("inner_solid_color")
        inner_start_color = request.form.get("inner_start_color")
        inner_end_color = request.form.get("inner_end_color")
        inner_mask_image_file = request.files.get("inner_mask_image")

        # OUTER
        outer_solid_color = request.form.get("outer_solid_color")
        outer_start_color = request.form.get("outer_start_color")
        outer_end_color = request.form.get("outer_end_color")
        outer_mask_image_file = request.files.get("outer_mask_image")

        # Handle image upload
        image_path = image_upload(image_file, app)

        # Upload optional mask image (used for ImageColorMask)
        data_mask_image_path = image_upload(data_mask_image_file, app)
        inner_mask_image_path = image_upload(inner_mask_image_file, app)
        outer_mask_image_path = image_upload(outer_mask_image_file, app)

        # Handle wifi qr creation
        qr_code_url = wifi_handler(ssid, password, encryption, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)
        filename = os.path.basename(qr_code_url)

        return render_template("index.html", qr_code_url = qr_code_url, filename=filename, uuid=uuid4(), active_form = "wifi")
    
#! Route for getting imput from calendar form
@app.route("/generate_qr_calendar", methods=["GET", "POST"])
def generate_qr_calendar():
    if request.method == "POST":
        # Get user input from form
        event_name = request.form.get("event")
        raw_datetime = request.form['datetime']
        location = request.form.get("location")
        duration = request.form.get("duration")
        description = request.form.get("description")
        timezone = request.form.get("timezone")
        image_file = request.files.get("image")
        
        # Split the date and time
        date, time = raw_datetime.split('T')
        # Handle the date and time along with duration
        dtstart, dtend = handle_date_time(date, time, timezone, duration)
        
        # Inputs for QR Data
        data_shape = request.form.get("data_shape")
        qr_style_data = request.form.get("qr_style_data")
        # Inputs for QR Inner eyes
        inner_eye_shape = request.form.get("inner_eye_shape")
        inner_eye_style = request.form.get("qr_style_inner")
        # Inputs for QR Outer eyes
        outer_eye_shape = request.form.get("outer_eye_shape")
        outer_eye_style = request.form.get("qr_style_outer")
        
        # Handle dynamic inputs
        # DATA
        data_solid_color = request.form.get("data_solid_color")
        data_start_color = request.form.get("data_start_color")
        data_end_color = request.form.get("data_end_color")
        data_mask_image_file = request.files.get("data_mask_image")

        # INNER
        inner_solid_color = request.form.get("inner_solid_color")
        inner_start_color = request.form.get("inner_start_color")
        inner_end_color = request.form.get("inner_end_color")
        inner_mask_image_file = request.files.get("inner_mask_image")

        # OUTER
        outer_solid_color = request.form.get("outer_solid_color")
        outer_start_color = request.form.get("outer_start_color")
        outer_end_color = request.form.get("outer_end_color")
        outer_mask_image_file = request.files.get("outer_mask_image")

        # Handle image upload
        image_path = image_upload(image_file, app)

        # Upload optional mask image (used for ImageColorMask)
        data_mask_image_path = image_upload(data_mask_image_file, app)
        inner_mask_image_path = image_upload(inner_mask_image_file, app)
        outer_mask_image_path = image_upload(outer_mask_image_file, app)

        # Pass the duration as part of the function call
        qr_code_url = calendar_handler(event_name, dtstart, dtend, location, description, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)
        filename = os.path.basename(qr_code_url)

        return render_template("index.html", qr_code_url=qr_code_url, filename=filename, uuid=uuid4(), active_form="calendar")




# @app.route("/static/output/<filename>")
# def serve_qr_code(filename):
#     return render_template("index.html", qr_code_url = f"static/output/{filename}", active_form = "link")

@app.route('/download_qr/<filename>')
def download_qr(filename):
    output_dir = app.config["OUTPUT_FOLDER"]
    file_path = os.path.join(output_dir, filename)

    if not os.path.exists(file_path):
        render_template_string("""
        <html>
        <head><title>QR Code Not Found</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>Oops! This QR code is no longer available.</h2>
            <p>It may have already been downloaded or expired.</p>
            <a href="/">Go back to Home</a>
        </body>
        </html>
        """), 404

    try:
        # Read the file into memory
        with open(file_path, "rb") as f:
            file_data = f.read()

        # Create a BytesIO stream
        byte_io = BytesIO(file_data)
        byte_io.seek(0)

        # Delete the file
        os.remove(file_path)

        # Send the in-memory file
        return send_file(
            byte_io,
            as_attachment=True,
            download_name=filename,
            mimetype='image/png'
        )
    except Exception as e:
        app.logger.error(f"Download error: {e}")
        return render_template_string("""
        <html>
        <head><title>Error</title></head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h2>Something went wrong while downloading your QR code.</h2>
            <p>Please try again later.</p>
            <a href="/">Go back to Home</a>
        </body>
        </html>
        """), 500

if __name__ == "__main__":
    app.run(debug=True)
