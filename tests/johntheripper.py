import hashlib

def crack_password(hash_to_crack, dictionary):
    for password in dictionary:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == hash_to_crack:
            return password
    return None

# Example usage
hash_to_crack = "098f6bcd4621d373cade4e832627b4f6"  # MD5 hash of "test"
dictionary = ["password", "123456", "qwerty", "test"]

result = crack_password(hash_to_crack, dictionary)
if result:
    print(f"Password cracked: {result}")
else:
    print("Password not found in dictionary.")
