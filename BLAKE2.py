# BLAKE2

# is a cryptographic hash function that is faster than MD5, SHA-1, SHA-2, and SHA-3, but still has a high level of security. This algorithm was developed as the successor to BLAKE, which was a finalist in the SHA-3 competition.


import hashlib

text = input("Input Text: ").encode()


hashed = hashlib.blake2b(text) #512-bit
print("BLAKE2b: ", hashed.hexdigest())

hashed = hashlib.blake2s(text) #256-bit
print("BLAKE2s: ", hashed.hexdigest())