import pyotp
import qrcode

# Generate a random Base32 key
key = pyotp.random_base32()

# Create a TOTP object with the key
totp = pyotp.TOTP(key)

# Generate a QR code containing the TOTP URI
qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
qr.add_data(totp.provisioning_uri("Afri-Techy", issuer_name="Afri Techy  App"))
qr.make(fit=True)
img = qr.make_image()

# Save the QR code image to a file
img.save("qr.png")

# Verify TOTP codes
while True:
    code = input("Enter code: ")
    print("Valid code:", totp.verify(code))
