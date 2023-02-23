import pyotp
from pyotp import totp

key = "mykey"  # manual key

input_code = input("Enter 2FA Code:")

code = totp.now()

print(totp.verify(input_code))

counter = 0
hotp = pyotp.HOTP(key)
print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))

for _ in range(3):
    print(hotp.verify(input("Enter Code:"), counter))
    counter += 1