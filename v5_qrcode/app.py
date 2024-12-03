from flask import Flask, render_template, request, send_file
from vcard_generator import generate_vcard_qr
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get user input from form
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")

        # Generate the QR code
        qr_code_path = generate_vcard_qr(name, phone, email)

        # Serve the QR code to the user
        return send_file(qr_code_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)