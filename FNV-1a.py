# FNV-1a (Fowler-Noll-Vo) – Quick hash, non-cryptographic hashes

# is a non-cryptographic hash function designed for high speed and good distribution. This algorithm was made by Glenn Fowler, Landon Curt Noll, and Kiem-Phong Vo in 1991.


def fnv1a_32(text: bytes) -> int:
    hash = 0x811c9dc5
    for byte in text:
        hash ^= byte
        hash *= 0x01000193
        hash &= 0xffffffff
    return hash

text = input("Input Text: ").encode()
print("FNV-1a 32-bit: ", format(fnv1a_32(text), '08x'))
