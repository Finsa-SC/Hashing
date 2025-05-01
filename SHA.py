# SHA (Secure Hash Algorithm)

# is one of the hashing algorithms used to secure data. SHA was developed by the National Security Agency (NSA) and managed by the National Institute of Standards and Technology (NIST).

import hashlib


text = input("Input Text: ")


# SHA-1 (Secure Hash Algorithm)
hashed = hashlib.sha1(text.encode())
print("SHA-1: ", hashed.hexdigest())
print("\n")


# SHA-2 (Secure Hash Algorithm)
hashed = hashlib.sha256(text.encode())
print("SHA-256: ", hashed.hexdigest())
print("\n")


# SHA-3 (Secure Hash Algorithm)
hashed = hashlib.sha3_256(text.encode())
print("SHA3-256: ", hashed.hexdigest())
print("\n")