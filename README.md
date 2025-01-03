# QR Code Generator with vCard Integration

## Overview

This project is a QR Code generator that integrates vCard information. It allows users to generate QR codes that contain their contact details (name, phone, and email) in the vCard format. The project also supports embedding custom images in the QR code, such as logos or personal pictures, with customizable corners.

Generated QR codes are saved on the server and can be downloaded by users. The system can automatically delete the QR code images after a specified period to manage server storage.

## Features

- **vCard QR Code Generation**: Converts user-provided contact details into a vCard format, which can be read by QR code scanners.
- **Custom Image Embedding**: Embed custom images (like logos or profile pictures) into the center of the QR code with customizable corner rounding.
- **Automatic Cleanup**: QR code images are deleted automatically after 24 hours to save server space.
- **Flask Web Application**: Built using the Flask framework for easy web-based usage and download.

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.x installed on your system.
- `pip` for installing Python packages.

### Required Python Libraries

The project depends on several Python libraries, which can be installed via `pip`:

```bash
pip install -r requirements.txt
```

## Requirements

`requirements.txt` should contain:
```bash
Flask==2.0.3
Pillow==8.4.0
qrcode==7.3.1
vobject==0.9.6.1
```
## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/DaveTron4/QR_Code
    cd qr-code-generator
    ```

2. Set up a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use .venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to access the QR code generator interface.

3. Enter your contact details (name, phone, email) and upload an optional image (logo or profile picture) to embed in the QR code.

4. Click on the "Generate QR Code" button to create your QR code.

5. Once the QR code is generated, you can download it directly from the page.

6. The server will automatically delete the QR code image after 24 hours to keep storage usage minimal.

## File Structure

```text
/qr-code-generator
    /static
        /output        # Folder where generated QR codes are stored
        style.css
    /templates
        index.html     # HTML template for the QR code generator page
    app.py             # Main Flask application file
    vcard_generator.py # Module for generating the vCard QR code
    requirements.txt  # Required dependencies
    README.md         # Project documentation
```

## Code Breakdown

### `app.py`
- **Main Flask Application**: Handles the web routes and logic for generating and serving the QR codes.
- **Routes**:
    - `/`: Displays the QR code generation form and handles form submissions.
    - `/download_qr/<filename>`: Allows users to download their generated QR code.

### `vcard_generator.py`
- **QR Code Generation**: Converts user input into a vCard format and generates a QR code using the `qrcode` library.
- **Image Embedding**: Supports embedding custom images in the QR code, with the option to round the corners of the image.

### Automatic Cleanup (Scheduled Task)
A cleanup task runs in the background to automatically delete QR code files that are older than 24 hours to free up space on the server.

## How to Delete QR Codes

- **Automatic Deletion**: QR codes are automatically deleted after 24 hours of being created.
- **Manual Deletion**: You can manually delete the generated QR codes from the `static/output` folder if necessary.

## Contributing
Feel free to fork the project, create a branch, and submit pull requests for any improvements or bug fixes. Contributions are always welcome!
