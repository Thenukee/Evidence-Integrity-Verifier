import hashlib
import os
import sys
from datetime import datetime

def generate_hashes(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        print(f"[-] Error: File '{file_path}' not found.")
        return

    # Initialize hash algorithms
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()

    print(f"[*] Analyzing: {os.path.abspath(file_path)}")
    print(f"[*] Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)

    # Read file in chunks (to handle large forensic images without crashing RAM)
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
        
        # Output results
        print(f"MD5:    {md5_hash.hexdigest()}")
        print(f"SHA256: {sha256_hash.hexdigest()}")
        print("-" * 50)
        print("[+] Integrity check complete.")

    except Exception as e:
        print(f"[-] An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python evidence_verifier.py <file_path>")
    else:
        generate_hashes(sys.argv[1])
