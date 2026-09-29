# 🔑 File Hashing Tool (`filehashing.py`)

A Python security utility designed to calculate cryptographic checksums (MD5 and SHA-256) for a given file to verify data integrity and detect unauthorized modifications.

---

## 📸 Usage Screenshot

Below is a preview of the tool output in action:

<img width="959" height="534" alt="Screenshot 2026-09-29 162220" src="https://github.com/user-attachments/assets/f459e5e7-0f05-46bd-b151-c6c66639c59c" />
<img width="948" height="524" alt="Screenshot 2026-09-29 162203" src="https://github.com/user-attachments/assets/76a9410f-ca61-4aa0-9a1d-97c47508fa38" />



---

## ⚙️ Features

- **SHA-256 Checksum**: Calculates strong 256-bit cryptographic hashes for tamper verification and baseline comparisons.
- **MD5 Checksum**: Generates fast 128-bit hashes for legacy verification.
- **Integrity Checking**: Helps identify file alterations during forensic analysis, incident response, or malware checks.

---

## 🚀 How to Run

1. Open your terminal and navigate to the tool directory:
   ```bash
   cd tools/filehashing
2.   python filehashing.py <path_to_file>
3.example :
           python filehashing.py sample.txt
     
