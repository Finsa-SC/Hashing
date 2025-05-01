# RIPEMD (RACE Integrity Primitives Evaluation Message Digest)

# is a cryptographic hash algorithm developed by European academics, not by the NSA (like SHA).
# Designed for more open and independent alternatives to MD5 and SHA-1.

# pip install pycryptodome

from Crypto.Hash import RIPEMD


text = input("Input Text: ")
text = text.encode()
hashed = RIPEMD.new()
hashed.update(text)
print("RIPEMD-160: ", hashed.hexdigest())