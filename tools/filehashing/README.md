# 🔑 File Hashing Tool (filehashing.py)

A Python security utility that calculates **MD5** and **SHA-256** hashes for a file. Hashes can be used to compare files and help detect whether their contents have changed.

---

## 📸 Usage Screenshots

Examples of the tool output:

<img width="959" height="534" alt="File hashing tool output" src="https://github.com/user-attachments/assets/f459e5e7-0f05-46bd-b151-c6c66639c59c" />

<img width="948" height="524" alt="File hashing tool example" src="https://github.com/user-attachments/assets/76a9410f-ca61-4aa0-9a1d-97c47508fa38" />

---

## ⚙️ Features

- **MD5 Hashing**: Generates a 128-bit MD5 digest.
- **SHA-256 Hashing**: Generates a 256-bit SHA-256 digest.
- **Chunked File Reading**: Reads the file in 4 KB chunks instead of loading the entire file into memory.
- **Basic Error Handling**: Handles missing files and file-reading errors.

> **Security note:** MD5 is included for learning and legacy compatibility. For security-sensitive integrity verification, prefer SHA-256 or another modern cryptographic hash.

---

## 🚀 How to Run

1. Open your terminal and navigate to the tool directory:

   ```bash
   cd tools/filehashing
   ```

2. Run the script:

   ```bash
   python filehashing.py
   ```

3. Enter the path of the file when prompted.

Example:

```text
Enter file path: sample.txt
MD5:    <md5-hash>
SHA-256: <sha256-hash>
```

---

## 🧠 What I Learned

- Using Python's hashlib module.
- Opening files in binary mode with rb.
- Reading large files in chunks.
- Generating hexadecimal hash values with hexdigest().
