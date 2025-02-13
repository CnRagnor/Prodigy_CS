
# Password Complexity Checker

This project is a password complexity checker built in Python. It checks password strength based on several criteria and provides feedback to users. The project follows NIST guidelines for password security.

## Features

- **Minimum Length**: Passwords should be at least 8 characters, but longer passwords are recommended.
- **Blacklist Common Passwords**: Check against a list of common passwords and disallow them.
- **No Composition Rules**: Avoid mandating specific types of characters (e.g., special characters, numbers) but check for overall strength.
- **Allow Long Passphrases**: Encourage users to create long passphrases that are easy to remember but hard to guess.
- **Rate Limiting**: Implement rate-limiting to protect against brute force attacks.
- **User Guidance**: Provide clear feedback to users on how to create strong passwords.
- **Overall Rating**: Provide an overall rating out of 10 and classify the password as Weak, Medium, Strong, or Very Strong.
- **Visual Indicator**: Show a visual indicator for the password strength.

## Implementation of NIST Guidelines

This project implements the NIST (National Institute of Standards and Technology) guidelines for password security. The guidelines ensure that passwords are strong, unique, and resistant to common attacks.

## Usage

To use the password complexity checker, run the script and enter a password when prompted. The checker will evaluate the password's strength and provide feedback.

### Example Usage

```python
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
