# Whirlpool

# is a cryptographic hash function that produces a 512-bit hash value of an input of any length less than 2²⁵⁶ bit. This algorithm was designed by Vincent Rijmen and Paulo S. L. M. Barreto, and is based on the Square block cipher, which has a structure similar to AES but with special modifications.

# pip install whirlpool

import whirlpool

text = input("Input Text: ")
data = text.encode("utf-8")
hashed = whirlpool.new(data)
print("Whirlpool 512-bit digest: ", hashed.hexdigest())