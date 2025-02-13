import re
import time

# List of common passwords (this should be more comprehensive in a real application)
common_passwords = ["123456", "password", "123456789", "12345678", "12345", "qwerty", "abc123"]

# Rate limiting variables
attempts = 0
last_attempt_time = time.time()

def rate_limited():
    global attempts, last_attempt_time
    current_time = time.time()
    if current_time - last_attempt_time > 1:  # Reset after 1 second
        attempts = 0
    attempts += 1
    last_attempt_time = current_time
    if attempts > 5:
        return True
    return False

def check_password_strength(password):
    if rate_limited():
        return "Too many attempts. Please wait and try again later.", [], 0, []
    
    # Criteria based on NIST guidelines
    length_criteria = len(password) >= 8  # Minimum 8 characters
    not_common_password = password not in common_passwords  # Password is not a common password
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    number_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()-_+=<>?/" for char in password)

    # Feedback
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not not_common_password:
        feedback.append("Password is too common. Choose a more unique password.")
    
    # Overall strength
    score = 0
    if length_criteria:
        score += 2
    if not_common_password:
        score += 2
    if uppercase_criteria:
        score += 1
    if lowercase_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1

    # Classification based on score
    if score == 8:
        strength = "Very Strong"
    elif score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"
    
    # Password Strength Visual Indicator
    strength_visual = ["[ ]"] * 8
    for i in range(score):
        strength_visual[i] = "[X]"

    return strength, feedback, score, strength_visual

def get_user_specific_advice(password):
    advice = []
    if len(password) < 12:
        advice.append("For extra security, consider using a longer password or passphrase.")
    if password in common_passwords:
        advice.append("Avoid using common passwords.")
    if "password" in password.lower():
        advice.append("Avoid using 'password' in your password.")
    # Add more specific advice as needed
    return advice

# Example usage
password = input("Enter a password to check: ")

strength, feedback, score, strength_visual = check_password_strength(password)
advice = get_user_specific_advice(password)

print(f"\nPassword Strength: {strength}")
print(f"Overall Rating: {score}/10")
if feedback:
    print("\nFeedback:")
    for comment in feedback:
        print(f"- {comment}")
if advice:
    print("\nUser-specific Advice:")
    for comment in advice:
        print(f"- {comment}")

print(f"\nPassword Strength Visual Indicator: {' '.join(strength_visual)}")
