# Caesar Cipher Tool
# A simple encryption and decryption program

def caesar_cipher(text, shift, mode):
    """
    Encrypt or decrypt text using Caesar Cipher algorithm
    text: the input string to process
    shift: number of positions to shift letters
    mode: 'encrypt' or 'decrypt'
    """
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    # Process each character in the text
    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Determine the base (A for uppercase, a for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
            # Keep non-alphabet characters as they are
            result += char
    
    return result

def main():
    print("=== Caesar Cipher Tool ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            encrypted = caesar_cipher(message, shift, 'encrypt')
            print(f"Encrypted message: {encrypted}")
            
        elif choice == '2':
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value (1-25): "))
            decrypted = caesar_cipher(message, shift, 'decrypt')
            print(f"Decrypted message: {decrypted}")
            
        elif choice == '3':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# This ensures the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
