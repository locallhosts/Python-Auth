# pip install pytotp

import time
import pyotp

# # Generate a random Base32 key
# key = pyotp.random_base32()
#
# print("Generated key:", key)


# Generate a random Base32 key
key = pyotp.random_base32()

# Create a TOTP object with the key and a period of 30 seconds
totp = pyotp.TOTP(key, interval=30)

# Get the current OTP
otp = totp.now()

print(otp)


