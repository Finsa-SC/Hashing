import bcrypt
import hashlib
import zlib
import os
from argon2 import PasswordHasher
from argon2.low_level import Type
from Crypto.Hash import RIPEMD
import whirlpool

def fnv1a_32(data: bytes) -> int:
    hash = 0x811c9dc5
    for byte in data:
        hash ^= byte
        hash *= 0x01000193
        hash &= 0xffffffff
    return hash

def hash_file(file_path: str):
    print(f"\n=== File Hashing for: {file_path} ===")

    with open(file_path, 'rb') as f:
        file_data = f.read()

    print("\n[File] MD5:")
    print(hashlib.md5(file_data).hexdigest())

    print("\n[File] SHA1:")
    print(hashlib.sha1(file_data).hexdigest())

    print("\n[File] SHA256:")
    print(hashlib.sha256(file_data).hexdigest())

    print("\n[File] SHA3-512:")
    print(hashlib.sha3_512(file_data).hexdigest())

    print("\n[File] BLAKE2b:")
    print(hashlib.blake2b(file_data).hexdigest())

    print("\n[File] CRC32:")
    print(format(zlib.crc32(file_data), '08x'))

    print("\n[File] FNV-1a 32-bit:")
    print(format(fnv1a_32(file_data), '08x'))

    print("\n[File] RIPEMD-160:")
    ripemd_hash = RIPEMD.new()
    ripemd_hash.update(file_data)
    print(ripemd_hash.hexdigest())

    print("\n[File] Whirlpool:")
    whirlpool_hash = whirlpool.new(file_data)
    print(whirlpool_hash.hexdigest())


if __name__ == "__main__":
    hash_file("example.txt")
