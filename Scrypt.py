# Scrypt
# is a password-based key derivation function designed by Colin Percival in 2009. This algorithm was created to improve safety against brute-force attacks and special hardware-based attacks such as ASIC



import hashlib
import os


text = input("Input Text: ").encode()
salt = os.urandom(16)
hashed = hashlib.scrypt(text, salt=salt, n=16384, r=8, p=1)
print("scrypt: ", hashed.hex())