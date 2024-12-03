import qrcode
import os

def generate_vcard_qr(name, phone, email):
    # vCard format
    vcard = f"""BEGIN:VCARD
    VERSION:3.0
    FN:{name}
    TEL:{phone}
    EMAIL:{email}
    END:VCARD"""

    # Generate QR code
    qr = qrcode.make(vcard)

    # Save to a specific directory
    output_dir = os.path.join(os.getcwd(), "static")  # Ensure "static" exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    path = os.path.join(output_dir, f"{name}_vcard.png")
    qr.save(path)

    return path