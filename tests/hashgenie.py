import hashlib
import itertools

def crack_hash(target_hash, charset='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    for length in range(1, 8):  # Adjust the range based on the expected length of the original text
        for guess in itertools.product(charset, repeat=length):
            guess_text = ''.join(guess)
            hashed_text = hashlib.sha256(guess_text.encode()).hexdigest()  # Change the hash function as needed
            if hashed_text == target_hash:
                return guess_text
    return None

# Example usage
target_hash = input("Enter the hash to crack: ")
original_text = crack_hash(target_hash)
if original_text:
    print("The original text is:", original_text)
else:
    print("Unable to crack the hash.")
