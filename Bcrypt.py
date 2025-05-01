
# Bcrypt
# is a hashing function designed for password security. This algorithm was developed by Niels Provos and David Mazières in 1999 and is based on the Blowfish cipher.


# pip install bcrypt

import bcrypt

text = input("Input Text: ").encode()
hashed = bcrypt.hashpw(text, bcrypt.gensalt())
print("bcrypt: ", hashed)