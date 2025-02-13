from pynput import keyboard
import logging
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import sys

class EthicalKeylogger:
    def __init__(self):
        self.logging_active = False
        self.consent_given = False
        self.log_filename = None
        self.listener = None
        
    def setup_logging(self):
        """Configure logging with timestamp and appropriate format"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_filename = f"keylog_{timestamp}.txt"
        logging.basicConfig(
            filename=self.log_filename,
            level=logging.INFO,
            format='%(asctime)s: %(message)s'
        )
        
    def get_consent(self):
        """Display consent window and get user permission"""
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        
        consent_message = """
        Educational Keylogger Consent Form
        
        This program will record keyboard inputs for educational purposes.
        
        By clicking 'Yes', you acknowledge:
        1. This is for educational/research purposes only
        2. All keystrokes will be logged to a local file
        3. You can stop logging at any time by pressing 'ESC'
        
        Do you consent to keyboard logging?
        """
        
        consent = messagebox.askyesno("Consent Required", consent_message)
        root.destroy()
        return consent
    
    def on_press(self, key):
        """Handle key press events"""
        if not self.logging_active:
            return

        try:
            # Handle normal characters
            key_char = key.char
        except AttributeError:
            # Handle special keys
            key_char = str(key)

        # Check for ESC to stop
        if key == keyboard.Key.esc:
            self.stop_logging()
            return False

        # Log the key press
        key_info = f"Key pressed: {key_char}"
        logging.info(key_info)
        print(key_info)  # Optional: Show in console for educational purposes
    
    def start_logging(self):
        """Start the keylogger with consent check"""
        print("Initializing educational keylogger...")
        
        self.consent_given = self.get_consent()
        if not self.consent_given:
            print("Consent not given. Exiting program.")
            sys.exit()
            
        self.setup_logging()
        self.logging_active = True
        
        print(f"""
        Logging started:
        - Log file: {self.log_filename}
        - Press ESC to stop logging
        """)
        
        # Start keyboard listener
        with keyboard.Listener(on_press=self.on_press) as self.listener:
            self.listener.join()
    
    def stop_logging(self):
        """Stop the keylogger and clean up"""
        self.logging_active = False
        if self.listener:
            self.listener.stop()
        print(f"\nLogging stopped. Log file saved as: {self.log_filename}")
        sys.exit()

if __name__ == "__main__":
    keylogger = EthicalKeylogger()
    keylogger.start_logging()
    
