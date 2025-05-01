# MD5 (Message-Digest Algorithm 5)

# is a cryptographic algorithm that produces 128-bit (16-byte) output in the form of a 32 character hexadecimal string from any input.

import hashlib

text = input("Input Text: ")
print("\n")


# MD5 (Message Digest 5)
hashed = hashlib.md5(text.encode())
print("MD5: ",hashed.hexdigest())
print("\n")


