import hashlib
import os

def calculate_hash(filename):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()

    try:
        with open(filename, "rb") as file:
            # Read in 4KB chunks to handle large files efficiently
            for chunk in iter(lambda: file.read(4096), b""):
                md5.update(chunk)
                sha256.update(chunk)
        return md5.hexdigest(), sha256.hexdigest()
    except FileNotFoundError:
        print(f"[!] Error: The file '{filename}' was not found.")
        return None, None
    except Exception as e:
        print(f"[!] Error reading file: {e}")
        return None, None

if __name__ == "__main__":
    filepath = input("Enter file path: ").strip()
    
    if os.path.exists(filepath):
        md5_val, sha256_val = calculate_hash(filepath)
        if md5_val and sha256_val:
            print(f"MD5:    {md5_val}")
            print(f"SHA-256: {sha256_val}")
    else:
        print("[!] Invalid path provided.")
