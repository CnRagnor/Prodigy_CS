# Password Strength Checker

## Overview
A sophisticated password strength checker that evaluates passwords based on NIST guidelines and provides detailed feedback with visual indicators. The tool includes rate limiting to prevent brute force attempts and offers personalized advice for password improvement.

## Features
- Real-time password strength evaluation
- Rate limiting protection
- Visual strength indicators
- Customized feedback and recommendations
- Common password detection
- NIST guideline compliance

## Security Features
- Rate limiting (5 attempts per second)
- Common password database
- Multiple strength criteria evaluation
- No password storage
- Local execution only

## Password Evaluation Criteria
The checker evaluates passwords based on:
- Minimum length (8 characters)
- Presence of uppercase letters
- Presence of lowercase letters
- Presence of numbers
- Special characters
- Common password check
- Context-specific patterns

## Scoring System
Total possible score: 8 points
- Length ≥ 8 characters: 2 points
- Not a common password: 2 points
- Contains uppercase: 1 point
- Contains lowercase: 1 point
- Contains numbers: 1 point
- Contains special characters: 1 point

Password Strength Classifications:
- Score 8: Very Strong
- Score 6-7: Strong
- Score 4-5: Medium
- Score 0-3: Weak

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/password-strength-checker.git
cd password-strength-checker
```

2. No additional dependencies required - uses Python standard library only.

## Usage
Run the script:
```bash
python password_checker.py
```

Example output:
```
Enter a password to check: MyPassword123!

Password Strength: Strong
Overall Rating: 7/8

Password Strength Visual Indicator: [X] [X] [X] [X] [X] [X] [X] [ ]

User-specific Advice:
- For extra security, consider using a longer password or passphrase.
```

## Visual Indicator
The strength indicator uses a simple visual representation:
- [X] = Point earned
- [ ] = Point not earned

Example: `[X] [X] [X] [X] [ ] [ ] [ ] [ ]` indicates a score of 4/8

## Rate Limiting
- Maximum 5 attempts per second
- Automatic cooldown period
- Prevents brute force attempts

## Code Structure
```
password_strength_checker/
│
├── password_checker.py    # Main program file
├── README.md             # This documentation
└── common_passwords.txt  # Database of common passwords
```

## Key Components
1. `check_password_strength()`: Main evaluation function
2. `rate_limited()`: Rate limiting implementation
3. `get_user_specific_advice()`: Personalized feedback generator

## Security Considerations
- Does not store or transmit passwords
- Runs locally only
- Includes rate limiting
- Checks against common password database
- Provides specific security advice

## Best Practices for Users
1. Use passwords of at least 12 characters
2. Combine uppercase, lowercase, numbers, and special characters
3. Avoid common words and patterns
4. Use unique passwords for different accounts
5. Consider using a password manager

## Contributing
Contributions are welcome! Areas for improvement:
1. Expanding the common password database
2. Adding more context-specific checks
3. Implementing additional security features
4. Improving the feedback system

## Future Enhancements
- Extended common password database
- Pattern recognition improvements
- Additional language support
- GUI interface
- Password generation suggestions

## License
[MIT license]

## Disclaimer
This tool is for educational and testing purposes only. Always follow security best practices and applicable security policies when handling passwords.

## Author
[NAVNEET]

---
*Note: This password strength checker is designed for educational purposes and local testing. For production systems, consider using established security libraries and frameworks.*
