# CRC32

# is an error checking algorithm used to detect changes or damage to data in transmission or storage. CRC (Cyclic Redundancy Check) works by generating 32-bit hash values from the data provided, which are then used to verify data integrity when received.


import zlib

text = input("Input Text: ").encode()
hashed = zlib.crc32(text)
print("CRC32: ", format(hashed, '08x'))