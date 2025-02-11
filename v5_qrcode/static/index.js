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
                <button type="submit">Generate QR Code</button>
            </form>
        `;
    }
    else if (type == 'link') {
        formContent.innerHTML = `
            <form action = "/generate_qr_link" method="POST" enctype="multipart/form-data">
                <div>
                    <label for="link">Enter Link:</label>
                    <input type="url" id="link" name="link" required>
                </div>
                <button type="submit">Generate QR Code</button>
            </form>
        `;
    }
    // else{
    //     formContent.innerHTML = ''
    // }
}