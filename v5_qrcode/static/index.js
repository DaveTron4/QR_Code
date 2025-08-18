document.addEventListener("DOMContentLoaded", function () {
    if (activeForm) {
        changeForm(activeForm);
    }
});

function getRepeatableCode() {
    return `
    <div>
                    <label for="image">Upload Image (optional):</label>
                    <input type="file" id="image" name="image" accept="image/*">
                </div>

                <div class="style_options_section">
                    <div class="data_modules_options">
                        <h2 class="data_modules_title">Data Modules</h2>
                        <div class="data_modules_options_container" id="shape_container">
                            <label for="data_shape">Shape:</label>
                            <select id="data_shape" name="data_shape" required>
                                <option value="none" ${window.formData.data_shape === 'none' ? 'selected' : ''}>None</option>
                                <option value="square" ${window.formData.data_shape === 'square' ? 'selected' : ''}>Square</option>
                                <option value="gapped_square" ${window.formData.data_shape === 'gapped_square' ? 'selected' : ''}>Gapped Square</option>
                                <option value="circle" ${window.formData.data_shape === 'circle' ? 'selected' : ''}>Circle</option>
                                <option value="rounded" ${window.formData.data_shape === 'rounded' ? 'selected' : ''}>Rounded</option>
                                <option value="vertical_bar" ${window.formData.data_shape === 'vertical_bar' ? 'selected' : ''}>Vertical Bars</option>
                                <option value="horizontal_bar" ${window.formData.data_shape === 'horizontal_bar' ? 'selected' : ''}>Horizontal Bars</option>
                            </select>
                        </div>

                        <div class="data_modules_options_container" id="style_container">
                            <label for="qr_style">Style:</label>
                            <select class="qr-style-select" name="qr_style_data" required>
                                <option value="none" ${window.formData.qr_style_data === 'none' ? 'selected' : ''}>None</option>
                                <option value="SolidFillColorMask" ${window.formData.qr_style_data === 'SolidFillColorMask' ? 'selected' : ''}>Solid Fill</option>
                                <option value="RadialGradiantColorMask" ${window.formData.qr_style_data === 'RadialGradiantColorMask' ? 'selected' : ''}>Radial Gradiant</option>
                                <option value="SquareGradiantColorMask" ${window.formData.qr_style_data === 'SquareGradiantColorMask' ? 'selected' : ''}>Square Gradiant</option>
                                <option value="HorizontalGradiantColorMask" ${window.formData.qr_style_data === 'HorizontalGradiantColorMask' ? 'selected' : ''}>Horizontal Gradiant</option>
                                <option value="VerticalGradiantColorMask" ${window.formData.qr_style_data === 'VerticalGradiantColorMask' ? 'selected' : ''}>Vertical Gradiant</option>
                                <option value="ImageColorMask" ${window.formData.qr_style_data === 'ImageColorMask' ? 'selected' : ''}>Image</option>
                            </select>
                            <div id="qr-style-options"></div>
                        </div>
                    </div>

                    <div class="inner_eye_options">
                        <h2 class="inner_eye_title">Inner Eye</h2>
                        <div class="inner_eye_options_container" id="inner_eye_shape_container">
                            <label for="inner_eye_shape">Shape:</label>
                            <select id="inner_eye_shape" name="inner_eye_shape" required>
                                <option value="none" ${window.formData.inner_eye_shape === 'none' ? 'selected' : ''}>None</option>
                                <option value="square" ${window.formData.inner_eye_shape === 'square' ? 'selected' : ''}>Square</option>
                                <option value="gapped_square" ${window.formData.inner_eye_shape === 'gapped_square' ? 'selected' : ''}>Gapped Square</option>
                                <option value="circle" ${window.formData.inner_eye_shape === 'circle' ? 'selected' : ''}>Circle</option>
                                <option value="rounded" ${window.formData.inner_eye_shape === 'rounded' ? 'selected' : ''}>Rounded</option>
                                <option value="vertical_bar" ${window.formData.inner_eye_shape === 'vertical_bar' ? 'selected' : ''}>Vertical Bars</option>
                                <option value="horizontal_bar" ${window.formData.inner_eye_shape === 'horizontal_bar' ? 'selected' : ''}>Horizontal Bars</option>
                            </select>
                        </div>

                        <div class="inner_eye_options_container" id="inner_eye_style_container">
                            <label for="inner_eye_style">Style:</label>
                            <select class="qr-style-select" name="qr_style_inner" required>
                                <option value="none" ${window.formData.qr_style_inner === 'none' ? 'selected' : ''}>None</option>
                                <option value="SolidFillColorMask" ${window.formData.qr_style_inner === 'SolidFillColorMask' ? 'selected' : ''}>Solid Fill</option>
                                <option value="RadialGradiantColorMask" ${window.formData.qr_style_inner === 'RadialGradiantColorMask' ? 'selected' : ''}>Radial Gradiant</option>
                                <option value="SquareGradiantColorMask" ${window.formData.qr_style_inner === 'SquareGradiantColorMask' ? 'selected' : ''}>Square Gradiant</option>
                                <option value="HorizontalGradiantColorMask ${window.formData.qr_style_inner === 'HorizontalGradiantColorMask' ? 'selected' : ''}>Horizontal Gradiant</option>
                                <option value="VerticalGradiantColorMask" ${window.formData.qr_style_inner === 'VerticalGradiantColorMask' ? 'selected' : ''}>Vertical Gradiant</option>
                                <option value="ImageColorMask" ${window.formData.qr_style_inner === 'ImageColorMask' ? 'selected' : ''}>Image</option>
                            </select>
                            
                            <div id="qr-style-options"></div>
                        </div>
                    </div>

                    <div class="outer_eye_options">
                        <h2 class="outer_eye_title">Outer Eye</h2>
                        <div class="outer_eye_options_container" id="outer_eye_shape_container">
                            <label for="outer_eye_shape">Shape:</label>
                            <select id="outer_eye_shape" name="outer_eye_shape" required>
                                <option value="none" ${window.formData.outer_eye_shape === 'none' ? 'selected' : ''}>None</option>
                                <option value="square" ${window.formData.outer_eye_shape === 'square' ? 'selected' : ''}>Square</option>
                                <option value="gapped_square" ${window.formData.outer_eye_shape === 'gapped_square' ? 'selected' : ''}>Gapped Square</option>
                                <option value="circle" ${window.formData.outer_eye_shape === 'circle' ? 'selected' : ''}>Circle</option>
                                <option value="rounded" ${window.formData.outer_eye_shape === 'rounded' ? 'selected' : ''}>Rounded</option>
                                <option value="vertical_bar" ${window.formData.outer_eye_shape === 'vertical_bar' ? 'selected' : ''}>Vertical Bars</option>
                                <option value="horizontal_bar" ${window.formData.outer_eye_shape === 'horizontal_bar' ? 'selected' : ''}>Horizontal Bars</option>
                            </select>
                        </div>

                        <div class="outer_eye_options_container" id="outer_eye_style_container">
                            <label for="outer_eye_style">Style:</label>
                            <select class="qr-style-select" name="qr_style_outer" required>
                                <option value="none" ${window.formData.qr_style_outer === 'none' ? 'selected' : ''}>None</option>
                                <option value="SolidFillColorMask" ${window.formData.qr_style_outer === 'SolidFillColorMask' ? 'selected' : ''}>Solid Fill</option>
                                <option value="RadialGradiantColorMask" ${window.formData.qr_style_outer === 'RadialGradiantColorMask' ? 'selected' : ''}>Radial Gradiant</option>
                                <option value="SquareGradiantColorMask" ${window.formData.qr_style_outer === 'SquareGradiantColorMask' ? 'selected' : ''}>Square Gradiant</option>
                                <option value="HorizontalGradiantColorMask" ${window.formData.qr_style_outer === 'HorizontalGradiantColorMask' ? 'selected' : ''}>Horizontal Gradiant</option>
                                <option value="VerticalGradiantColorMask" ${window.formData.qr_style_outer === 'VerticalGradiantColorMask' ? 'selected' : ''}>Vertical Gradiant</option>
                                <option value="ImageColorMask" ${window.formData.qr_style_outer === 'ImageColorMask' ? 'selected' : ''}>Image</option>
                            </select>
                            <div id="qr-style-options"></div>
                        </div>
                    </div>
                </div>
                <button type="submit">Generate QR Code</button>
                `
}

// TODO: Add options to change attributes of modules like radius, size, etc.

function attachQrStyleListeners() {
    const styleSelectors = document.querySelectorAll('.qr-style-select');

    styleSelectors.forEach(select => {
        const optionsContainer = select.nextElementSibling; // assumes the .qr-style-options div comes right after
        const name = select.getAttribute('name');
        const prefix = name.replace('qr_style_', '');

        select.addEventListener("change", function () {
            const style = this.value;
            optionsContainer.innerHTML = ''; // Clear previous options

            if (style === 'SolidFillColorMask') {
                optionsContainer.innerHTML = `
                    <div>
                        <label>Color:</label>
                        <input type="color" name="${prefix}_solid_color" value="${window.formData[prefix + '_solid_color'] || ''}">
                    </div>
                `;
            } else if (
                style === 'RadialGradiantColorMask' ||
                style === 'SquareGradiantColorMask' ||
                style === 'HorizontalGradiantColorMask' ||
                style === 'VerticalGradiantColorMask'
            ) {
                optionsContainer.innerHTML = `
                    <div>
                        <label>Start Color:</label>
                        <input type="color" name="${prefix}_start_color" value="${window.formData[prefix + '_start_color'] || ''}">
                    </div>
                    <div>
                        <label>End Color:</label>
                        <input type="color" name="${prefix}_end_color" value="${window.formData[prefix + '_end_color'] || ''}">
                    </div>
                `;
            } else if (style === 'ImageColorMask') {
                optionsContainer.innerHTML = `
                    <div>
                        <label>Upload Color Mask Image:</label>
                        <input type="file" name="${prefix}_mask_image" accept="image/*">
                    </div>
                `;
            }
        });
    });
}

document.addEventListener("DOMContentLoaded", attachQrStyleListeners);


function changeForm(type) {
    let formContent = document.getElementById("form-container");

    formContent.innerHTML = '';

    if (type == 'vcard' ) {
        formContent.innerHTML = `
            <form action = "/generate_qr_vcard" method="POST" enctype="multipart/form-data">
                <div>
                    <label for="name">Full Name:</label>
                    <input type="text" id="name" name="name" placeholder="John Doe"  value="${window.formData.name || ''}" required>
                </div>
                <div>
                    <label for="phone">Phone Number:</label>
                    <input type="tel" id="phone" name="phone" pattern="\\d{10}" placeholder="1234567890" value="${window.formData.phone || ''}" required
                        oninvalid="this.setCustomValidity('Please enter a valid 10-digit phone number.')"
                        oninput="this.setCustomValidity('')">
                </div>
                <div>
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" placeholder="example@example.com" value="${window.formData.email || ''}"required>
                </div>
                ${getRepeatableCode()}

            </form>
        `;
    } else if (type == 'link') {
        formContent.innerHTML = `
            <form action = "/generate_qr_link" method="POST" enctype="multipart/form-data">
                <div>
                    <label for="link">Enter Link:</label>
                    <input type="url" id="link" name="link" value="${window.formData.link || ''}" required>
                </div>
                ${getRepeatableCode()}
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
                ${getRepeatableCode()}
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
                ${getRepeatableCode()}
            </form>
        `;
    } else if (type == 'default') {
        formContent.innerHTML = `
            <div>
                <h2>Please select a form type to generate a QR code.</h2>
                <h3>Available options: vCard, Link, WiFi, Calendar.</h3>
            </div>
        `;
    }
    else {
        formContent.innerHTML = `
            <div>
                <h2>Invalid form type selected.</h2>
                <h3>Please select a valid form type.</h3>
            </div>
        `;
    }

    attachQrStyleListeners();
}