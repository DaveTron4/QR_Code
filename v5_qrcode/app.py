from flask import render_template, request, send_file, abort, send_from_directory
import os
from static.handlers.vcard_handler import vcard_handler
from static.handlers.configuration_handler import configuration
from static.handlers.image_upload_handler import image_upload
from static.handlers.link_handler import link_handler
from static.handlers.wifi_handler import wifi_handler
from static.handlers.calendar_handler import calendar_handler
from static.handlers.date_time_handler import handle_date_time

app = configuration()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Route for getting input from vcard form
@app.route("/generate_qr_vcard", methods=["GET", "POST"])
def generate_qr_vcard():
    if request.method == "POST":
        # Get user input from form
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        image_file = request.files.get("image")
        
        # Handle image upload
        image_path = image_upload(image_file, app)

        # Handle vcard creation
        qr_code_url = vcard_handler(name, phone, email, image_path)

        # Serve the QR code to the user
        return render_template("index.html", qr_code_url=qr_code_url, active_form = "vcard")


# Route for getting input from link form
@app.route("/generate_qr_link", methods=["GET", "POST"])
def generate_qr_link():
    if request.method == "POST":
        # Get user input from form
        link = request.form.get("link")
        image_file = request.files.get("image")

        # Handle image upload
        image_path = image_upload(image_file, app)

        # Handle link qr creation
        qr_code_url = link_handler(link, image_path) if image_path else link_handler(link, None)
        
        return render_template("index.html", qr_code_url = qr_code_url, active_form = "link")

# Route for getting imput from wifi form
@app.route("/generate_qr_wifi", methods=["GET", "POST"])
def generate_qr_wifi():
    if request.method == "POST":
        # Get user input from form
        ssid = request.form.get("ssid")
        password = request.form.get("password")
        encryption = request.form.get("encryption")

        image_file = request.files.get("image")

        # Handle image upload
        image_path = image_upload(image_file, app)

        # Handle wifi qr creation
        qr_code_url = wifi_handler(ssid, password, encryption, image_path) if image_path else wifi_handler(ssid, password, encryption, None)

        return render_template("index.html", qr_code_url = qr_code_url, active_form = "wifi")
    
# Route for getting imput from calendar form
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

        # Split the date and time
        date, time = raw_datetime.split('T')

        # Handle the date and time along with duration
        dtstart, dtend = handle_date_time(date, time, timezone, duration)

        image_file = request.files.get("image")

        # Handle image upload
        image_path = image_upload(image_file, app)

        # Pass the duration as part of the function call
        qr_code_url = calendar_handler(event_name, dtstart, dtend, location, description, image_path) if image_path else calendar_handler(event_name, dtstart, dtend, location, description, None)

        return render_template("index.html", qr_code_url=qr_code_url, active_form="calendar")




# @app.route("/static/output/<filename>")
# def serve_qr_code(filename):
#     return render_template("index.html", qr_code_url = f"static/output/{filename}", active_form = "link")

@app.route('/download_qr/<filename>')
def download_qr(filename):
    output_dir = app.config["OUTPUT_FOLDER"]
    file_path = os.path.join(output_dir, filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        abort(404)  # If not found, return 404 error

    # Serve the file for download
    try:
        # Send the file to the user
        response = send_file(file_path, as_attachment=True)

        # After sending the file, delete it
        os.remove(file_path)
        
        return response
    except Exception as e:
        abort(500)  # Handle any errors that might occur

if __name__ == "__main__":
    app.run(debug=True)
