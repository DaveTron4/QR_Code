document.addEventListener("DOMContentLoaded", function () {
    if (activeForm) {
        changeForm(activeForm);
    }
});

function attachQrStyleListener() {
    const qrStyleSelect = document.getElementById("qr_style");
    const styleOptionsDiv = document.getElementById("styleOptions");

    if (!qrStyleSelect || !styleOptionsDiv) return; 

    qrStyleSelect.addEventListener("change", function () {
        const style = this.value;
        styleOptionsDiv.innerHTML = ''; // Clear previous fields

        if (style === 'SolidFillColorMask') {
            styleOptionsDiv.innerHTML = `
                <div>
                    <label for="solid-color">Color:</label>
                    <input type="color" id="solid-color" name="solid_color" value="#000000">
                </div>
            `;
        } else if (
            style === 'RadialGradiantColorMask' ||
            style === 'SquareGradiantColorMask' ||
            style === 'HorizontalGradiantColorMask' ||
            style === 'VerticalGradiantColorMask'
        ) {
            styleOptionsDiv.innerHTML = `
                <div>
                    <label for="start-color">Start Color:</label>
                    <input type="color" id="start-color" name="start_color" value="#000000">
                </div>
                <div>
                    <label for="end-color">End Color:</label>
                    <input type="color" id="end-color" name="end_color" value="#ffffff">
                </div>
            `;
        } else if (style === 'ImageColorMask') {
            styleOptionsDiv.innerHTML = `
                <div>
                    <label for="mask-image">Upload Color Mask Image:</label>
                    <input type="file" id="mask-image" name="mask_image" accept="image/*">
                </div>
            `;
        }
    });
}

function changeForm(type) {
    let formContent = document.getElementById("form-container");

    formContent.innerHTML = '';

    if (type == 'vcard' ) {
        formContent.innerHTML = `
            <form action = "/generate_qr_vcard" method="POST" enctype="multipart/form-data">
                <div>
                    <label for="name">Full Name:</label>
                    <input type="text" id="name" name="name" placeholder="John Doe" required>
                </div>
                <div>
                    <label for="phone">Phone Number:</label>
                    <input type="tel" id="phone" name="phone" pattern="\\d{10}" placeholder="1234567890" required
                        oninvalid="this.setCustomValidity('Please enter a valid 10-digit phone number.')"
                        oninput="this.setCustomValidity('')">
                </div>
                <div>
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" placeholder="example@example.com" required>
                </div>
                <div>
                    <label for="image">Upload Image (optional):</label>
                    <input type="file" id="image" name="image" accept="image/*">
                </div>
                <div>
                    <label for="qr-shape">QR Shape:</label>
                    <select id="qr_shape" name="qr_shape" required>
                        <option value="none">None</option>
                        <option value="square">Square</option>
                        <option value="gapped_square">Gapped Square</option>
                        <option value="circle">Circle</option>
                        <option value="rounded">Rounded</option>
                        <option value="vertical_bar">Vertical Bars</option>
                        <option value="horizontal_bar">Horizontal Bars</option>
                    </select>
                </div>
                <div>
                    <label for="color-masks">QR Style:</label>
                    <select id="qr_style" name="qr_style" required>
                        <option value="none">None</option>
                        <option value="SolidFillColorMask">Solid Fill</option>
                        <option value="RadialGradiantColorMask">Radial Gradiant</option>
                        <option value="SquareGradiantColorMask">Square Gradiant</option>
                        <option value="HorizontalGradiantColorMask">Horizontal Gradiant</option>
                        <option value="VerticalGradiantColorMask">Vertical Gradiant</option>
                        <option value="ImageColorMask">Image</option>
                    </select>

                    <div id="styleOptions"></div>
                </div>
                <button type="submit">Generate QR Code</button>
            </form>
        `;
    } else if (type == 'link') {
        formContent.innerHTML = `
            <form action = "/generate_qr_link" method="POST" enctype="multipart/form-data">
                <div>
                    <label for="link">Enter Link:</label>
                    <input type="url" id="link" name="link" required>
                </div>
                <div>
                    <label for="image">Upload Image (optional):</label>
                    <input type="file" id="image" name="image" accept="image/*">
                </div>
                <div>
                    <label for="qr-shape">QR Shape:</label>
                    <select id="qr_shape" name="qr_shape" required>
                        <option value="none">None</option>
                        <option value="square">Square</option>
                        <option value="gapped_square">Gapped Square</option>
                        <option value="circle">Circle</option>
                        <option value="rounded">Rounded</option>
                        <option value="vertical_bar">Vertical Bars</option>
                        <option value="horizontal_bar">Horizontal Bars</option>
                    </select>
                </div>
                <div>
                    <label for="color-masks">QR Style:</label>
                    <select id="qr_style" name="qr_style" required>
                        <option value="none">None</option>
                        <option value="SolidFillColorMask">Solid Fill</option>
                        <option value="RadialGradiantColorMask">Radial Gradiant</option>
                        <option value="SquareGradiantColorMask">Square Gradiant</option>
                        <option value="HorizontalGradiantColorMask">Horizontal Gradiant</option>
                        <option value="VerticalGradiantColorMask">Vertical Gradiant</option>
                        <option value="ImageColorMask">Image</option>
                    </select>

                    <div id="styleOptions"></div>
                </div>
                <button type="submit">Generate QR Code</button>
            </form>
        `;
    } else if (type == 'wifi') {
        formContent.innerHTML = `
            <form action = "/generate_qr_wifi" method="POST" enctype="multipart/form-data">
                <div>
                    <label for="ssid">SSID:</label>
                    <input type="text" id="ssid" name="ssid" required>
                </div>
                <div>
                    <label for="password">Password:</label>
                    <input type="password" id="password" name="password" required>
                </div>
                <div>
                    <label for="encryption">Encryption:</label>
                    <select id="encryption" name="encryption" required>
                        <option value="none">None</option>
                        <option value="WPA">WPA</option>
                        <option value="WEP">WEP</option>
                        <option value="nopass">No Password</option>
                    </select>
                </div>
                <div>
                    <label for="image">Upload Image (optional):</label>
                    <input type="file" id="image" name="image" accept="image/*">
                </div>
                <div>
                    <label for="qr-shape">QR Shape:</label>
                    <select id="qr_shape" name="qr_shape" required>
                        <option value="none">None</option>
                        <option value="square">Square</option>
                        <option value="gapped_square">Gapped Square</option>
                        <option value="circle">Circle</option>
                        <option value="rounded">Rounded</option>
                        <option value="vertical_bar">Vertical Bars</option>
                        <option value="horizontal_bar">Horizontal Bars</option>
                    </select>
                </div>
                <div>
                    <label for="color-masks">QR Style:</label>
                    <select id="qr_style" name="qr_style" required>
                        <option value="none">None</option>
                        <option value="SolidFillColorMask">Solid Fill</option>
                        <option value="RadialGradiantColorMask">Radial Gradiant</option>
                        <option value="SquareGradiantColorMask">Square Gradiant</option>
                        <option value="HorizontalGradiantColorMask">Horizontal Gradiant</option>
                        <option value="VerticalGradiantColorMask">Vertical Gradiant</option>
                        <option value="ImageColorMask">Image</option>
                    </select>

                    <div id="styleOptions"></div>
                </div>
                <button type="submit">Generate QR Code</button>
            </form>
        `;
    } else if (type == 'calendar') {
        formContent.innerHTML = `
            <form action = "/generate_qr_calendar" method="POST" enctype="multipart/form-data">
                <div>
                    <label for="event">Event:</label>
                    <input type="text" id="event" name="event" required>
                </div>
                <div>
                    <label for="datetime">Date and Time:</label>
                    <input type="datetime-local" id="datetime" name="datetime" required>
                </div>
                <div>
                    <label for="location">Location:</label>
                    <input type="text" id="location" name="location" required>
                </div>
                <div>
                    <label for="description">Description:</label>
                    <textarea id="description" name="description"></textarea>
                </div>
                <div>
                    <label for="duration">Duration:</label>
                    <input type="text" id="duration" name="duration" placeholder="e.g., 1 hour">
                </div>
                <div>
                    <label for="timezone">Timezone:</label>
                    <select id="timezone" name="timezone" required>
                        <option value="UTC">UTC</option>
                        <option value="America/New_York">America/New_York</option>
                        <option value="America/Los_Angeles">America/Los_Angeles</option>
                        <option value="Europe/London">Europe/London</option>
                        <option value="Asia/Tokyo">Asia/Tokyo</option>
                        <option value="Australia/Sydney">Australia/Sydney</option>
                        <option value="Europe/Paris">Europe/Paris</option>
                    </select>
                </div>
                <div>
                    <label for="image">Upload Image (optional):</label>
                    <input type="file" id="image" name="image" accept="image/*">
                </div>
                <div>
                    <label for="qr-shape">QR Shape:</label>
                    <select id="qr_shape" name="qr_shape" required>
                        <option value="none">None</option>
                        <option value="square">Square</option>
                        <option value="gapped_square">Gapped Square</option>
                        <option value="circle">Circle</option>
                        <option value="rounded">Rounded</option>
                        <option value="vertical_bar">Vertical Bars</option>
                        <option value="horizontal_bar">Horizontal Bars</option>
                    </select>
                </div>
                <div>
                    <label for="color-masks">QR Style:</label>
                    <select id="qr_style" name="qr_style" required>
                        <option value="none">None</option>
                        <option value="SolidFillColorMask">Solid Fill</option>
                        <option value="RadialGradiantColorMask">Radial Gradiant</option>
                        <option value="SquareGradiantColorMask">Square Gradiant</option>
                        <option value="HorizontalGradiantColorMask">Horizontal Gradiant</option>
                        <option value="VerticalGradiantColorMask">Vertical Gradiant</option>
                        <option value="ImageColorMask">Image</option>
                    </select>

                    <div id="styleOptions"></div>
                </div>
                <button type="submit">Generate QR Code</button>
            </form>
        `;
    }
    // else{
    //     formContent.innerHTML = ''
    // }

    attachQrStyleListener();
}