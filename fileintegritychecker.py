import hashlib
import os

def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file"""
    sha256 = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print("File not found!")
        return None


def save_hash(file_path, hash_value):
    """Save hash value to a file"""
    with open("hash_store.txt", "w") as f:
        f.write(f"{file_path}|{hash_value}")


def load_hash():
    """Load stored hash value"""
    if not os.path.exists("hash_store.txt"):
        return None, None
    
    with open("hash_store.txt", "r") as f:
        data = f.read().split("|")
        return data[0], data[1]


def check_integrity(file_path):
    """Compare current hash with stored hash"""
    stored_path, stored_hash = load_hash()
    
    if stored_hash is None:
        print("No stored hash found. Saving current hash.")
        current_hash = calculate_hash(file_path)
        save_hash(file_path, current_hash)
        print("Hash saved successfully!")
        return
    
    current_hash = calculate_hash(file_path)

    if current_hash == stored_hash:
        print("✅ File Integrity Verified. No changes detected.")
    else:
        print("❌ WARNING! File has been modified.")


# -------- MAIN PROGRAM --------
file_path = input("Enter file path to monitor: ")
check_integrity(file_path)
