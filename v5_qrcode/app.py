from datetime import timedelta, datetime
from flask import redirect, render_template, request, send_file, render_template_string, session, url_for
from io import BytesIO
import os
from uuid import uuid4
from static.handlers.vcard_handler import vcard_handler
from static.handlers.configuration_handler import configuration, get_user_folders
from static.handlers.image_upload_handler import image_upload
from static.handlers.link_handler import link_handler
from static.handlers.wifi_handler import wifi_handler
from static.handlers.calendar_handler import calendar_handler
from static.handlers.date_time_handler import handle_date_time
from static.handlers.qr_cleanup_handler import clear_output_folder

#TODO NOTES:
#! - Add a session timeout to clear the session and session folder after 30 minutes of inactivity
#TODO - Add a download all button that zips the output folder and allows the user to download all the qr codes they have generated in their session
#TODO - Add a section that shows the user the qr codes they have generated in their session and when clicked on the qr code it shows a larger version of the qr code and a download button and delete button
#TODO - Add default active form

app = configuration()
app.permanent_session_lifetime = app.config.get("PERMANENT_SESSION_LIFETIME", timedelta(minutes=30))

#! Save form data to session
def save_form_data():
    # Create or update a dictionary in session
    if "form_data" not in session:
        session["form_data"] = {}

    # Update the form_data dictionary with submitted values
    for key, value in request.form.items():
        session["form_data"][key] = value

#! This will be called once when the app starts serving a new session
@app.before_request
def setup_user_folder():
    if "user_folder" not in session:
        upload_folder, output_folder = get_user_folders()
        session["user_output_folder"] = output_folder
        session["user_upload_folder"] = upload_folder

#! This will be called before every request to check for session timeout
@app.before_request
def check_session_timeout():
    now = datetime.now()
    last_active = session.get("last_active")

    if last_active:
        elapsed = (now - datetime.fromisoformat(last_active)).total_seconds()
        if elapsed > 30 * 60:  # 30 minutes
            # Delete user folder if exists
            if "user_output_folder" in session:
                clear_output_folder(app, session["user_output_folder"])
            session.clear()

    # Update activity timestamp
    session["last_active"] = now.isoformat()

#! Route for main page
@app.route("/", methods=["GET", "POST"])
def index():
    session["active_form"] = "default"
    form_data = session.get("form_data", {})
    return render_template("index.html", form_data=form_data, active_form=session.get("active_form", "default"))

#! Route for getting input from vcard form
@app.route("/generate_qr_vcard", methods=["GET", "POST"])
def generate_qr_vcard():
    if request.method == "POST":
        # Save form data to session
        save_form_data()

        # Set the form type in session
        session["active_form"] = "vcard"

        # Retrieve form data from session
        form_data = session.get("form_data", {})

        # Get user upload and output folders from session
        upload_folder = session["user_upload_folder"]
        output_folder = session["user_output_folder"]

        # Get user input from form
        name = form_data.get("name")
        phone = form_data.get("phone")
        email = form_data.get("email")

        # Get the uploaded image file from the request
        image_file = request.files.get("image")

        # Inputs for QR Data
        data_shape = form_data.get("data_shape")
        qr_style_data = form_data.get("qr_style_data")
        # Inputs for QR Inner eyes
        inner_eye_shape = form_data.get("inner_eye_shape")
        inner_eye_style = form_data.get("qr_style_inner")
        # Inputs for QR Outer eyes
        outer_eye_shape = form_data.get("outer_eye_shape")
        outer_eye_style = form_data.get("qr_style_outer")
        
        # Handle dynamic inputs
        # DATA
        data_solid_color = form_data.get("data_solid_color")
        data_start_color = form_data.get("data_start_color")
        data_end_color = form_data.get("data_end_color")
        data_mask_image_file = request.files.get("data_mask_image")

        # INNER
        inner_solid_color = form_data.get("inner_solid_color")
        inner_start_color = form_data.get("inner_start_color")
        inner_end_color = form_data.get("inner_end_color")
        inner_mask_image_file = request.files.get("inner_mask_image")

        # OUTER
        outer_solid_color = form_data.get("outer_solid_color")
        outer_start_color = form_data.get("outer_start_color")
        outer_end_color = form_data.get("outer_end_color")
        outer_mask_image_file = request.files.get("outer_mask_image")
        
        # Handle image upload
        image_path = image_upload(image_file, upload_folder)

        # Upload optional mask image (used for ImageColorMask)
        data_mask_image_path = image_upload(data_mask_image_file, upload_folder)
        inner_mask_image_path = image_upload(inner_mask_image_file, upload_folder)
        outer_mask_image_path = image_upload(outer_mask_image_file, upload_folder)

        # Handle vcard creation
        full_path = vcard_handler(name, phone, email, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)
        qr_code_url  = full_path.split("static", 1)[1]
        qr_code_url = "/static" + qr_code_url.replace("\\", "/")
        filename = os.path.basename(qr_code_url)


        print(f"Session vcard data: {form_data}")


        # Serve the QR code to the user
        return render_template("index.html", qr_code_url=qr_code_url, filename=filename, form_data=form_data, uuid=uuid4(), active_form=session.get("active_form", "default"))


#! Route for getting input from link form
@app.route("/generate_qr_link", methods=["GET", "POST"])
def generate_qr_link():
    if request.method == "POST":
        # Save form data to session
        save_form_data()

        # Set the form type in session
        session["active_form"] = "link"

        # Retrieve form data from session
        form_data = session.get("form_data", {})

        # Get user upload and output folders from session
        upload_folder = session["user_upload_folder"]
        output_folder = session["user_output_folder"]

        # Get user input from form
        link = form_data.get("link")

        # Get the uploaded image file from the request
        image_file = request.files.get("image")

        # Inputs for QR Data
        data_shape = form_data.get("data_shape")
        qr_style_data = form_data.get("qr_style_data")
        # Inputs for QR Inner eyes
        inner_eye_shape = form_data.get("inner_eye_shape")
        inner_eye_style = form_data.get("qr_style_inner")
        # Inputs for QR Outer eyes
        outer_eye_shape = form_data.get("outer_eye_shape")
        outer_eye_style = form_data.get("qr_style_outer")
        
        # Handle dynamic inputs
        # DATA
        data_solid_color = form_data.get("data_solid_color")
        data_start_color = form_data.get("data_start_color")
        data_end_color = form_data.get("data_end_color")
        data_mask_image_file = request.files.get("data_mask_image")

        # INNER
        inner_solid_color = form_data.get("inner_solid_color")
        inner_start_color = form_data.get("inner_start_color")
        inner_end_color = form_data.get("inner_end_color")
        inner_mask_image_file = request.files.get("inner_mask_image")

        # OUTER
        outer_solid_color = form_data.get("outer_solid_color")
        outer_start_color = form_data.get("outer_start_color")
        outer_end_color = form_data.get("outer_end_color")
        outer_mask_image_file = request.files.get("outer_mask_image")

        # Handle image upload
        image_path = image_upload(image_file, upload_folder)

        # Upload optional mask image (used for ImageColorMask)
        data_mask_image_path = image_upload(data_mask_image_file, upload_folder)
        inner_mask_image_path = image_upload(inner_mask_image_file, upload_folder)
        outer_mask_image_path = image_upload(outer_mask_image_file, upload_folder)

        # Handle link qr creation
        full_path = link_handler(link, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)
        qr_code_url  = full_path.split("static", 1)[1]
        qr_code_url = "/static" + qr_code_url.replace("\\", "/")
        filename = os.path.basename(qr_code_url)


        print(f"Session link data: {form_data}")


        return render_template("index.html", qr_code_url = qr_code_url, filename=filename, form_data=form_data, uuid=uuid4(), active_form=session.get("active_form", "default"))

#! Route for getting imput from wifi form
@app.route("/generate_qr_wifi", methods=["GET", "POST"])
def generate_qr_wifi():
    if request.method == "POST":
        # Save form data to session
        save_form_data()

        # Set the form type in session
        session["active_form"] = "wifi"

        # Retrieve form data from session
        form_data = session.get("form_data", {})

        # Get user upload and output folders from session
        upload_folder = session["user_upload_folder"]
        output_folder = session["user_output_folder"]

        # Get user input from form
        ssid = form_data.get("ssid")
        password = form_data.get("password")
        encryption = form_data.get("encryption")
        image_file = request.files.get("image")

        # Inputs for QR Data
        data_shape = form_data.get("data_shape")
        qr_style_data = form_data.get("qr_style_data")
        # Inputs for QR Inner eyes
        inner_eye_shape = form_data.get("inner_eye_shape")
        inner_eye_style = form_data.get("qr_style_inner")
        # Inputs for QR Outer eyes
        outer_eye_shape = form_data.get("outer_eye_shape")
        outer_eye_style = form_data.get("qr_style_outer")
        
        # Handle dynamic inputs
        # DATA
        data_solid_color = form_data.get("data_solid_color")
        data_start_color = form_data.get("data_start_color")
        data_end_color = form_data.get("data_end_color")
        data_mask_image_file = request.files.get("data_mask_image")

        # INNER
        inner_solid_color = form_data.get("inner_solid_color")
        inner_start_color = form_data.get("inner_start_color")
        inner_end_color = form_data.get("inner_end_color")
        inner_mask_image_file = request.files.get("inner_mask_image")

        # OUTER
        outer_solid_color = form_data.get("outer_solid_color")
        outer_start_color = form_data.get("outer_start_color")
        outer_end_color = form_data.get("outer_end_color")
        outer_mask_image_file = request.files.get("outer_mask_image")

        # Handle image upload
        image_path = image_upload(image_file, upload_folder)

        # Upload optional mask image (used for ImageColorMask)
        data_mask_image_path = image_upload(data_mask_image_file, upload_folder)
        inner_mask_image_path = image_upload(inner_mask_image_file, upload_folder)
        outer_mask_image_path = image_upload(outer_mask_image_file, upload_folder)

        # Handle wifi qr creation
        full_path = wifi_handler(ssid, password, encryption, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)
        qr_code_url  = full_path.split("static", 1)[1]
        qr_code_url = "/static" + qr_code_url.replace("\\", "/")
        filename = os.path.basename(qr_code_url)


        print(f"Session wifi data: {form_data}")


        return render_template("index.html", qr_code_url = qr_code_url, filename=filename, form_data=form_data, uuid=uuid4(), active_form=session.get("active_form", "default"))
    
#! Route for getting imput from calendar form
@app.route("/generate_qr_calendar", methods=["GET", "POST"])
def generate_qr_calendar():
    if request.method == "POST":
        # Save form data to session
        save_form_data()

        # Set the form type in session
        session["active_form"] = "calendar"

        # Retrieve form data from session
        form_data = session.get("form_data", {})

        # Get user upload and output folders from session
        upload_folder = session["user_upload_folder"]
        output_folder = session["user_output_folder"]

        # Get user input from form
        event_name = form_data.get("event")
        raw_datetime = request.form['datetime']
        location = form_data.get("location")
        duration = form_data.get("duration")
        description = form_data.get("description")
        timezone = form_data.get("timezone")
        image_file = request.files.get("image")
        
        # Split the date and time
        date, time = raw_datetime.split('T')
        # Handle the date and time along with duration
        dtstart, dtend = handle_date_time(date, time, timezone, duration)
        
        # Inputs for QR Data
        data_shape = form_data.get("data_shape")
        qr_style_data = form_data.get("qr_style_data")
        # Inputs for QR Inner eyes
        inner_eye_shape = form_data.get("inner_eye_shape")
        inner_eye_style = form_data.get("qr_style_inner")
        # Inputs for QR Outer eyes
        outer_eye_shape = form_data.get("outer_eye_shape")
        outer_eye_style = form_data.get("qr_style_outer")
        
        # Handle dynamic inputs
        # DATA
        data_solid_color = form_data.get("data_solid_color")
        data_start_color = form_data.get("data_start_color")
        data_end_color = form_data.get("data_end_color")
        data_mask_image_file = request.files.get("data_mask_image")

        # INNER
        inner_solid_color = form_data.get("inner_solid_color")
        inner_start_color = form_data.get("inner_start_color")
        inner_end_color = form_data.get("inner_end_color")
        inner_mask_image_file = request.files.get("inner_mask_image")

        # OUTER
        outer_solid_color = form_data.get("outer_solid_color")
        outer_start_color = form_data.get("outer_start_color")
        outer_end_color = form_data.get("outer_end_color")
        outer_mask_image_file = request.files.get("outer_mask_image")

        # Handle image upload
        image_path = image_upload(image_file, upload_folder)

        # Upload optional mask image (used for ImageColorMask)
        data_mask_image_path = image_upload(data_mask_image_file, upload_folder)
        inner_mask_image_path = image_upload(inner_mask_image_file, upload_folder)
        outer_mask_image_path = image_upload(outer_mask_image_file, upload_folder)

        # Pass the duration as part of the function call
        full_path = calendar_handler(event_name, dtstart, dtend, location, description, output_folder, data_shape, qr_style_data, inner_eye_shape, inner_eye_style, outer_eye_shape, outer_eye_style, image_path, data_solid_color, data_start_color, data_end_color, data_mask_image_path, inner_solid_color, inner_start_color, inner_end_color, inner_mask_image_path, outer_solid_color, outer_start_color, outer_end_color, outer_mask_image_path)
        qr_code_url  = full_path.split("static", 1)[1]
        qr_code_url = "/static" + qr_code_url.replace("\\", "/")
        filename = os.path.basename(qr_code_url)


        print(f"Session calendar data: {form_data}")


        return render_template("index.html", qr_code_url=qr_code_url, filename=filename, form_data=form_data, uuid=uuid4(), active_form=session.get("active_form", "default"))

#! Route for downloading the generated QR code
@app.route('/download_qr/<filename>')
def download_qr(filename):
    output_folder = session["user_output_folder"]
    file_path = os.path.join(output_folder, filename)

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

@app.route("/clear_output")
def clear_output():
    clear_output_folder(app, session["user_output_folder"])
    active_form = session.get("active_form", "default")  # default if not set
    return render_template("index.html", active_form=active_form)

@app.route("/clear_session")
def clear_session():
    # Clear the session data
    clear_output_folder(app, session["user_output_folder"])
    session.clear()
    
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)