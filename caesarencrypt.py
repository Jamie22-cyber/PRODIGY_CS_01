# Function to encrypt the text using Caesar Cipher
def encrypt(text, shift):
    result = ""
    
    # Traverse the text
    for i in range(len(text)):
        char = text[i]
        
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # Keep non-alphabetic characters unchanged
        else:
            result += char
            
    return result

# Function to decrypt the text using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main function to get user input and perform encryption/decryption
def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    
    # Get the message and shift value from the user
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))
    
    if choice == 'encrypt':
        print(f"Encrypted message: {encrypt(message, shift)}")
    elif choice == 'decrypt':
        print(f"Decrypted message: {decrypt(message, shift)}")
    else:
        print("Invalid choice!")

if _name_ == "_main_":
    main()
