import re

def check_password_strength(password):
    score = 0

    # Check for length
    if len(password) >= 8:
        score += 1
    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    # Check for digits
    if re.search(r"[0-9]", password):
        score += 1
    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Determine password strength
    if score <= 2:
        return "Weak Password"
    elif score == 3:
        return "Moderate Password"
    else:
        return "Strong Password"

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(check_password_strength(password))