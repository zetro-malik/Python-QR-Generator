import qrcode

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # QR code version (1 to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=20,  # Size of each box/pixel in the QR code
    border=2,  # Border size around the QR code
)

# Data to be encoded in the QR code
data = "https://zeeshan-cv.vercel.app/FYP"

# Add data to the QR code instance
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("qrcode.png")
