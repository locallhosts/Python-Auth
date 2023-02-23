import pyotp

key = pyotp.random_base32()


#key ="mykey" this manaully key create

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter Code:")))
