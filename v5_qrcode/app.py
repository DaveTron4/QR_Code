from flask import Flask, render_template, request, send_file, url_for
from vcard_generator import generate_vcard_qr
import os
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input from form
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")

        # Validate phone number (e.g., must be exactly 10 digits)
        if not re.fullmatch(r"\d{10}", phone):
            return render_template("index.html", qr_code_url=None, error="Invalid phone number! Please enter a 10-digit number.")

        # Generate the QR code
        qr_code_path = generate_vcard_qr(name, phone, email)

        qr_code_url = url_for("static", filename=f"output/{os.path.basename(qr_code_path)}")

        # Serve the QR code to the user
        return render_template("index.html", qr_code_url=qr_code_url)

    return render_template("index.html", qr_code_url=None)

if __name__ == "__main__":
    app.run(debug=True)