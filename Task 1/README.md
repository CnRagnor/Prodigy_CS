# Caesar Cipher and Secure Encryption

## Overview
A robust encryption program implementing AES (Advanced Encryption Standard) encryption using the Fernet implementation from the cryptography library. The program provides secure encryption and decryption capabilities with comprehensive logging and error handling.

## Features
- AES encryption/decryption using Fernet
- Secure key generation
- Comprehensive error handling
- Detailed logging system
- User-friendly CLI interface
- Input validation
- Base64 encoded output

## Security Features
- Strong AES encryption (Fernet implementation)
- Secure key generation
- No key storage
- Session-based keys
- Input validation
- Detailed error logging

## Requirements
- Python 3.x
- cryptography library

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/secure-encryption.git
cd secure-encryption
```

2. Install required packages:
```bash
pip install cryptography
```

## Usage
Run the program:
```bash
python secure_encryption.py
```

### Interactive Menu Options:
- E: Encrypt text
- D: Decrypt text
- Y/N: Continue or exit program

### Example Usage:
```
=======================================
    SECURE ENCRYPTION PROGRAM
    AES Implementation
=======================================

Select operation (E)ncrypt or (D)ecrypt: E
Enter text: Hello, World!

Encrypted Data (AES):
----------------------------------------
gAAAAABl7X8J9X7v2X8J9X7v2X8J9X7v2X8J9X==
----------------------------------------

Continue? (Y/N): Y
```

## Code Structure
```
secure-encryption/
│
├── secure_encryption.py   # Main program file
├── encryption_log.txt     # Log file
├── requirements.txt       # Project dependencies
└── README.md             # This documentation
```

## Components
### SecureEncryption Class
- `__init__`: Generates AES key and initializes Fernet
- `encrypt_aes`: Encrypts text using AES
- `decrypt_aes`: Decrypts AES-encrypted text

### Utility Functions
- `print_banner`: Displays program header
- `print_result`: Formats output
- `main`: Main program loop

## Logging System
The program maintains detailed logs in `encryption_log.txt`:
- Program start/end
- Successful operations
- Error messages
- User interruptions

Log Format:
```
2025-02-13 14:30:45 - INFO - Program started
2025-02-13 14:30:50 - INFO - AES Encryption successful
2025-02-13 14:31:00 - INFO - Program terminated
```

## Security Considerations
1. Key Management:
   - Keys are generated per session
   - No persistent key storage
   - Keys are securely generated using cryptography library

2. Data Handling:
   - Input validation
   - Secure error handling
   - No data persistence
   - Memory cleanup

3. Logging:
   - No sensitive data in logs
   - Rotation-based logging
   - Detailed error tracking

## Best Practices
1. Use strong, unique inputs
2. Keep encrypted data secure
3. Don't share encryption keys
4. Regularly check logs
5. Update dependencies regularly

## Error Handling
The program handles various errors:
- Invalid input
- Encryption/decryption failures
- Key generation issues
- User interruptions

## Contributing
Contributions welcome! Areas for improvement:
1. Additional encryption algorithms
2. File encryption support
3. Key management system
4. GUI interface
5. Additional security features

## Future Enhancements
- Multiple encryption algorithms
- File encryption
- Key management system
- Configuration options
- Batch processing

## License
[MIT license]

## Security Disclaimer
This program is for educational and testing purposes. For production use:
- Review security requirements
- Use appropriate key management
- Follow security best practices
- Consider compliance requirements

## Author
[NAVNEET]

---
*Note: This encryption program implements basic security features. For production systems, consider using established cryptographic libraries and frameworks with proper security reviews.*

