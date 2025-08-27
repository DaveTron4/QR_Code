# QR Code Generator Web App

A web application that allows users to generate QR codes for different types of data including vCards, URLs, Wi-Fi credentials, and more. This project is built with **Flask**, integrates **Python libraries for QR code generation**, and is deployable on platforms like **Render**.



Visit web app here: [QR Code Web App](QR Code Web App)

---

## Table of Contents

- [Description](#description)  
- [Technologies Used](#technologies-used)  
- [Features](#features)  
- [Installation and Running Locally](#installation-and-running-locally)  
- [Usage](#usage)  
- [Images & GIFs](#images--gifs)  
- [Folder Structure](#folder-structure)  

---

## Description

This project is a **QR Code Generator web app** that allows users to easily create QR codes for different purposes such as:

- vCard QR codes for sharing contact information  
- URLs and links  
- Wi-Fi credentials  
- Custom calendar event 

The app is designed for simplicity, fast generation, and easy deployment on cloud services.

Key technical aspects demonstrated in this project:

- **Backend Development with Flask**: Handling HTTP requests, rendering templates, managing user sessions, and processing form data dynamically.  
- **Frontend Development**: Custom HTML forms, CSS styling, and responsive design for smooth user experience.  
- **QR Code Generation**: Using Python libraries to generate QR codes dynamically based on user input.  
- **Session Management**: Tracking user progress through multi-step forms with Flask sessions.  
- **File Handling and Image Manipulation**: Generating QR codes with optional logos and custom shapes.  
- **Deployment Ready**: Configured to run locally or on cloud platforms like Render.  
- **Error Handling**: Robust template rendering and route handling with proper exception management.  

This project highlights skills in **full-stack development**, **backend Python programming**, **frontend UI/UX design**, **data processing**, and **deployment readiness**.

---

## Technologies Used

- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS, JavaScript  
- **QR Code Library**: `qrcode` and `Pillow` for image manipulation  
- **Template Engine**: Jinja2  
- **Session Management**: Flask sessions  
- **Deployment**: Render  

---

## Features

- Generate QR codes for multiple data types.
- Multi-step input forms for better UX.
- Session-based tracking to resume forms.
- Option to add logos or custom shapes to QR codes.
- Fully responsive design for desktop and mobile.
- Ready for cloud deployment with Render.

---

## Installation and Running Locally

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/qr-code-generator.git
cd QR_Code/v5_qrcode

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
      ├── output/
      └── uploads/
 ├── templates/           # HTML templates
 │    └── index.html
 ├── handlers/            # vCard and other handlers
 └── README.md
```
