# Caesar Cipher and Secure Encryption

This project includes a Caesar Cipher implementation and a secure encryption program using AES (Fernet). The Caesar Cipher is a simple substitution cipher, while the AES encryption ensures secure data encryption and decryption.

## Features

- **Caesar Cipher**: A basic implementation of the Caesar Cipher for educational purposes.
- **AES Encryption**: Secure encryption and decryption using the Fernet module from the `cryptography` library.
- **Logging**: Configurable logging with rotation to keep track of encryption and decryption operations.

## Implementation of AES Encryption

This project implements AES encryption using the Fernet module, following best practices for secure encryption. The encryption key is generated, and messages can be encrypted and decrypted securely. The program also includes logging to keep track of encryption and decryption operations.

## Usage

To use the Caesar Cipher and AES encryption program, run the script and follow the prompts.


# Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

# License
This project is licensed under the MIT License.

### Example Usage

```python
            
            # Process based on selected operation
            if operation == 'E':
                encrypted_data = secure.encrypt_aes(text)
                if encrypted_data:
                    print_result("Encrypted Data (AES)", encrypted_data)
                    logging.info("AES Encryption successful")
            else:
                decrypted_data = secure.decrypt_aes(text)
                if decrypted_data:
                    print_result("Decrypted Data (AES)", decrypted_data)
                    logging.info("AES Decryption successful")
            
            # Continue?
            if input("\nContinue? (Y/N): ").upper() != 'Y':
                break
                
    except Exception as e:
        logging.error(f"Critical error: {str(e)}")
        print("\nAn error occurred during operation.")
    finally:
        # Clean up
        logging.info("Program terminated")
        print("\nThank you for using the Secure Encryption Program!")

