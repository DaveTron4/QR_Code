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
