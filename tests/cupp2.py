def calculate_password_strength(password):
    length = len(password)
    uppercase_chars = sum(1 for char in password if char.isupper())
    lowercase_chars = sum(1 for char in password if char.islower())
    digits = sum(1 for char in password if char.isdigit())
    special_chars = length - (uppercase_chars + lowercase_chars + digits)
    
    # Calculate password complexity score
    complexity_score = (uppercase_chars > 0) + (lowercase_chars > 0) + (digits > 0) + (special_chars > 0)
    
    # Strength rating based on password length and complexity
    if length < 8:
        strength = 'Very weak'
    elif length < 12:
        strength = 'Weak'
    elif length < 16:
        strength = 'Moderate'
    elif length < 20:
        strength = 'Strong'
    else:
        strength = 'Very strong'
    
    # Adjust strength based on complexity score
    if complexity_score == 1:
        strength = 'Weak'
    elif complexity_score == 2:
        strength = 'Moderate'
    elif complexity_score == 3:
        strength = 'Strong'
    elif complexity_score == 4:
        strength = 'Very strong'
    
    return strength

def generate_passwords(details):
    passwords = set()
    # Generate passwords based on user details
    for detail in details:
        passwords.add(detail)
        passwords.add(detail[::-1])  # Reverse of detail
        passwords.add(detail.lower())  # Lowercase detail
        passwords.add(detail.upper())  # Uppercase detail
        passwords.add(detail.replace(' ', ''))  # Remove spaces
    
    # Add some common passwords
    common_passwords = {'password', '123456', 'qwerty', 'letmein', 'abc123'}
    passwords.update(common_passwords)
    
    return passwords

def main():
    print("Welcome to the Custom Password Generator (CUPG)")
    print("Please provide some personal details to generate passwords.")
    print("You can skip any question by pressing Enter.")
    print("")
    
    details = []
    questions = [
        "First name: ",
        "Last name: ",
        "Nickname: ",
        "Birthdate (YYYY-MM-DD): ",
        "Partner's name: ",
        "Partner's nickname: ",
        "Partner's birthdate (YYYY-MM-DD): ",
        "Child's name: ",
        "Child's nickname: ",
        "Child's birthdate (YYYY-MM-DD): ",
        "Pet's name: ",
        "Company name: ",
        "Special words (separated by spaces): ",
        "Key words (separated by spaces): ",
        "Random words (separated by spaces): "
    ]
    
    for question in questions:
        detail = input(question)
        if detail:
            details.append(detail)
    
    if not details:
        print("No details provided. Exiting.")
        return
    
    passwords = generate_passwords(details)
    
    print("\nGenerated Passwords:")
    for password in passwords:
        strength = calculate_password_strength(password)
        print(f"Password: {password} (Strength: {strength})")

if __name__ == "__main__":
    main()
