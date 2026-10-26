import hashlib
import os

def calculate_file_signatures(text_content):
    # Encoding simulated text stream to bytes
    byte_data = text_content.encode('utf-8')
    
    # Executing hash function objects
    md5_hash = hashlib.md5(byte_data).hexdigest()
    sha256_hash = hashlib.sha256(byte_data).hexdigest()
    
    return md5_hash, sha256_hash

if __name__ == "__main__":
    print("--- Security Forensic Tool: Static Malware Hash Analyzer ---")
    
    # Simulating a suspicious file string input stream
    simulated_malware_file_content = "MaliciousPayload_TrojanDownloader_ExecutionStrings_2026"
    
    md5_res, sha256_res = calculate_file_signatures(simulated_malware_file_content)
    
    print(f"\n[+] Analyzing Simulated Executable Content Data...")
    print(f"===========================================================")
    print(f"Generated MD5 Hash Signature (IOC):    {md5_res}")
    print(f"Generated SHA-256 Hash Signature (IOC): {sha256_res}")
    print(f"===========================================================")
    print("[SUCCESS] Static cryptographic attributes extracted successfully.")
