import qrcode
img = qrcode.make('https://interlokit.com/')
type(img) 
img.save("v2_qrcode/qr_output/qrcode1.png")
img
