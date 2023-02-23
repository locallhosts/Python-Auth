# Python-Auth
# OTP App

This is a simple OTP (One-Time Password) app that uses PyOTP and QRCode libraries to 
generate and display OTPs using TOTP (Time-Based One-Time Password) algorithm.

# Requirements
To use this app, you need to have the following:

#Python 3.x installed on your machine
PyOTP library installed (you can install it using pip: pip install pyotp)
QRCode library installed (you can install it using pip: pip install qrcode)

# Usage

Clone this repository to your local machine.
Open a terminal and navigate to the project directory.

Run the following command to generate a new key:
**python otp.py**

The app will display a provisioning URI and save a QR code image to the project directory.
Scan the QR code using a TOTP-compatible app (e.g. Google Authenticator).
The app will start displaying OTPs every 30 seconds


# Customization
You can customize the following parameters in the otp.py file:

key: The secret key used to generate OTPs. You can generate a random key using pyotp.random_base32() method.
name: The name of the user/account (used in the provisioning URI).
issuer_name: The name of the issuer/app (used in the provisioning URI).
interval: The time interval (in seconds) used to generate OTPs. The default value is 30 seconds.
# License

This app is released under the MIT License. Feel free to use, modify and distribute it.
