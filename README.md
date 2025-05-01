# 🔐 Hashing Algorithm Demonstration

[![MIT License](https://img.shields.io/github/license/Finsa-SC/Hashing?color=green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/downloads/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Finsa--SC%2FHashing-181717?logo=github)](https://github.com/Finsa-SC/Hashing)

A Python demonstration of various **hashing** and **password hashing** algorithms.  
Supports both **text input** and **file-based hashing** (e.g., `example.txt`).  
Perfect for cryptography beginners and developers who want to explore hashing techniques.

---

## ✨ Features

✅ Includes popular hash algorithms:

- `bcrypt` (secure password hashing)
- `scrypt` (memory-hard password hashing)
- `Argon2` (modern, secure, memory-hard)
- `BLAKE2b` (fast and secure)
- `SHA1`, `SHA256`, `SHA3-512`
- `MD5` (legacy, not secure for passwords)
- `RIPEMD-160` (SHA alternative)
- `Whirlpool` (512-bit hash)
- `CRC32` & `FNV-1a` (non-cryptographic, fast)

✅ Supports:
- 🔤 Text/password hashing from input
- 📄 File hashing (e.g., `example.txt`)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Finsa-SC/Hashing.git
cd Hashing
```

### 2. Install dependencies
```bash
pip install bcrypt argon2-cffi pycryptodome whirlpool-py
```

## ▶️ How to Use
Enter a string when prompted, and the program will display its hashes using multiple algorithms.
If example.txt exists, the script will also compute its file hashes.

#### ⚠️ Security Notes
> ❌ Do not use MD5, SHA1, CRC32, or FNV for password storage.
✅ Use bcrypt, scrypt, or Argon2 for secure password hashing.
These are resistant to brute-force and rainbow table attacks.


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributions
Pull requests and stars ⭐ are welcome!
Original repository: Finsa-SC/Hashing

## 🧠 Author
Developed by Finsa-SC
Crafted with a passion for cryptography, Python, and clean code 🧪🔐
