# Argon2

# is a password-based key derivation function designed for high security. This algorithm was developed by Alex Biryukov, Daniel Dinu, and Dmitry Khovratovich and won the 2015 Password Hashing Competition (PHC)


# pip install argon2-cffi

from argon2 import PasswordHasher

ph = PasswordHasher()
text = input("Input Text: ")
hashed = ph.hash(text)
print("Argon2: ", hashed)