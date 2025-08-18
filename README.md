# QR Code Generator Web App

A web application that allows users to generate QR codes for different types of data including vCards, URLs, Wi-Fi credentials, and more. This project is built with **Flask**, integrates **Python libraries for QR code generation**, and is deployable on platforms like **Render**.

---

## Table of Contents

- [Description](#description)  
- [Technologies Used](#technologies-used)  
- [Features](#features)  
- [Installation and Running Locally](#installation-and-running-locally)  
- [Usage](#usage)  
- [Images & GIFs](#images--gifs)  
- [Folder Structure](#folder-structure)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Description

This project is a **QR Code Generator web app** that allows users to easily create QR codes for different purposes such as:

- vCard QR codes for sharing contact information  
- URLs and links  
- Wi-Fi credentials  
- Custom calendar event 

The app is designed for simplicity, fast generation, and easy deployment on cloud services.

---

## Technologies Used

- **Python 3.13** – Backend programming language  
- **Flask 3.1.1** – Web framework  
- **Jinja2** – Templating engine  
- **Pillow** – Image processing for QR codes  
- **qrcode** – QR code generation  
- **vobject** – vCard handling  
- **Python-dotenv** – Environment variable management  
- **Gunicorn** – WSGI server for deployment  

Optional development tools:

- **VSCode** – Code editor  
- **Git** – Version control  

---

## Features

- Generate QR codes for different types of data  
- Save QR codes as images  
- Responsive web interface  
- Multi-step form for vCard generation  

---

## Installation and Running Locally

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator
```

2. **Create and activate a virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
flask run
```

5. **Open your browser at http://127.0.0.1:5000**

---

## Images & GIFS

---

## Folder Structure
```csharp
v5_qrcode/
 ├── app.py               # Main Flask app
 ├── requirements.txt
 ├── static/              # CSS, JS, and images
 ├── templates/           # HTML templates
 │    └── index.html
 ├── handlers/            # vCard and other handlers
 └── README.md
```