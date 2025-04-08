document.addEventListener("DOMContentLoaded", function () {
    if (activeForm) {
        changeForm(activeForm);
    }
});

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
                    <label for="qr-style">QR Style:</label>
                    <select id="encryption" name="encryption" required>
                        <option value="none">None</option>
                        <option value="SquareModuleDrawer">SquareModuleDrawer</option>
                        <option value="GrappedSquareMofuleDrawer">GrappedSquareMofuleDrawer</option>
                        <option value="CircleModuleDrawer">CircleModuleDrawer</option>
                        <option value="RoundedModuleDrawer">RoundedModuleDrawer</option>
                        <option value="VerticalBarsDrawer">VerticalBarsDrawer</option>
                        <option value="HorizontalBarsDrawer">HorizontalBarsDrawer</option>
                    </select>
                </div>
                <div>
                    <label for="color-masks">QR Masks:</label>
                    <select id="encryption" name="encryption" required>
                        <option value="none">None</option>
                        <option value="SolidFillColorMask">SolidFillColorMask</option>
                        <option value="RadialGradiantColorMask">RadialGradiantColorMask</option>
                        <option value="SquareGradiantColorMask">SquareGradiantColorMask</option>
                        <option value="HorizontalGradiantColorMask">HorizontalGradiantColorMask</option>
                        <option value="VerticalGradiantColorMask">VerticalGradiantColorMask</option>
                        <option value="ImageColorMask">ImageColorMask</option>
                    </select>
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
                    <label for="qr-style">QR Style:</label>
                    <select id="encryption" name="encryption" required>
                        <option value="none">None</option>
                        <option value="SquareModuleDrawer">SquareModuleDrawer</option>
                        <option value="GrappedSquareMofuleDrawer">GrappedSquareMofuleDrawer</option>
                        <option value="CircleModuleDrawer">CircleModuleDrawer</option>
                        <option value="RoundedModuleDrawer">RoundedModuleDrawer</option>
                        <option value="VerticalBarsDrawer">VerticalBarsDrawer</option>
                        <option value="HorizontalBarsDrawer">HorizontalBarsDrawer</option>
                    </select>
                </div>
                <div>
                    <label for="color-masks">QR Masks:</label>
                    <select id="encryption" name="encryption" required>
                        <option value="none">None</option>
                        <option value="SolidFillColorMask">SolidFillColorMask</option>
                        <option value="RadialGradiantColorMask">RadialGradiantColorMask</option>
                        <option value="SquareGradiantColorMask">SquareGradiantColorMask</option>
                        <option value="HorizontalGradiantColorMask">HorizontalGradiantColorMask</option>
                        <option value="VerticalGradiantColorMask">VerticalGradiantColorMask</option>
                        <option value="ImageColorMask">ImageColorMask</option>
                    </select>
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
                    <label for="qr-style">QR Style:</label>
                    <select id="encryption" name="encryption" required>
                        <option value="none">None</option>
                        <option value="SquareModuleDrawer">SquareModuleDrawer</option>
                        <option value="GrappedSquareMofuleDrawer">GrappedSquareMofuleDrawer</option>
                        <option value="CircleModuleDrawer">CircleModuleDrawer</option>
                        <option value="RoundedModuleDrawer">RoundedModuleDrawer</option>
                        <option value="VerticalBarsDrawer">VerticalBarsDrawer</option>
                        <option value="HorizontalBarsDrawer">HorizontalBarsDrawer</option>
                    </select>
                </div>
                <div>
                    <label for="color-masks">QR Masks:</label>
                    <select id="encryption" name="encryption" required>
                        <option value="none">None</option>
                        <option value="SolidFillColorMask">SolidFillColorMask</option>
                        <option value="RadialGradiantColorMask">RadialGradiantColorMask</option>
                        <option value="SquareGradiantColorMask">SquareGradiantColorMask</option>
                        <option value="HorizontalGradiantColorMask">HorizontalGradiantColorMask</option>
                        <option value="VerticalGradiantColorMask">VerticalGradiantColorMask</option>
                        <option value="ImageColorMask">ImageColorMask</option>
                    </select>
                </div>
                <button type="submit">Generate QR Code</button>
            </form>
        `;
    }
    // else{
    //     formContent.innerHTML = ''
    // }
}