import logging
from cryptography.fernet import Fernet

# Configure logging with rotation
logging.basicConfig(
    filename='encryption_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a'
)

class SecureEncryption:
    def __init__(self):
        # Generate AES key
        self.symmetric_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.symmetric_key)
    
    def encrypt_aes(self, message: str) -> str:
        """Encrypt using AES (Fernet)"""
        try:
            encrypted_data = self.cipher_suite.encrypt(message.encode())
            return encrypted_data.decode()
        except Exception as e:
            logging.error(f"AES Encryption error: {str(e)}")
            return None

    def decrypt_aes(self, encrypted_data: str) -> str:
        """Decrypt using AES (Fernet)"""
        try:
            # Decode from base64
            encrypted_data = encrypted_data.encode()
            decrypted_data = self.cipher_suite.decrypt(encrypted_data)
            return decrypted_data.decode()
        except Exception as e:
            logging.error(f"AES Decryption error: {str(e)}")
            return None

def print_banner():
    """Print a simple banner"""
    print("""
=======================================
    SECURE ENCRYPTION PROGRAM
    AES Implementation
=======================================
""")

def print_result(title, content):
    """Print results in a clean format"""
    print(f"\n{title}:")
    print("-" * 40)
    print(content)
    print("-" * 40)

def main():
    secure = SecureEncryption()
    logging.info("Program started")
    
    try:
        while True:
            print_banner()
            
            # Choose operation
            operation = input("\nSelect operation (E)ncrypt or (D)ecrypt: ").upper()
            
            if operation not in ['E', 'D']:
                print("\nInvalid operation selected!")
                continue
            
            # Get input text
            text = input("\nEnter text: ").strip()
            if not text:
                print("\nInvalid input length!")
                continue
            
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

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
        logging.warning("Program interrupted by user")
    finally:
        logging.info("Program terminated")

