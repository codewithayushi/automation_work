```python
# This script allows you to encode and decode a word using a simple "shift" method.
# It shifts each letter by a certain number, making it a basic secret message tool!

def encode_message(message, shift_amount):
    """
    Encodes a message by shifting each letter forward in the alphabet.
    Non-alphabetic characters (like spaces or numbers) are left unchanged.
    """
    encoded_chars = [] # A list to store our encoded letters
    
    # Loop through each character in the message
    for char in message:
        if 'a' <= char <= 'z': # Check if it's a lowercase letter
            # Calculate new position: (current position + shift) % 26 (for wrapping around A-Z)
            # ord() gets the numerical ASCII value of a character
            # chr() converts a numerical ASCII value back to a character
            shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            encoded_chars.append(shifted_char)
        elif 'A' <= char <= 'Z': # Check if it's an uppercase letter
            shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encoded_chars.append(shifted_char)
        else:
            # If it's not a letter, just add it as is
            encoded_chars.append(char)
            
    # Join all the encoded characters back into a single string
    return "".join(encoded_chars)

def decode_message(encoded_message, shift_amount):
    """
    Decodes a message by shifting each letter backward in the alphabet.
    It's the reverse of the encode_message function.
    """
    # To decode, we simply shift by the negative of the original shift_amount
    # (or 26 - shift_amount to keep it positive for the modulo operation)
    return encode_message(encoded_message, -shift_amount) # Reusing the encode logic with a negative shift

# --- Main part of the script ---
if __name__ == "__main__":
    print("Welcome to the Simple Secret Message Shifter!")
    print("---------------------------------------------")

    while True:
        # Give the user options
        print("\nChoose an option:")
        print("1. Encode a message")
        print("2. Decode a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # User wants to encode
            original_msg = input("Enter the message to encode: ")
            
            # Get the shift amount, making sure it's a number
            while True:
                try:
                    shift = int(input("Enter the shift amount (a whole number, e.g., 3 for 'A' -> 'D'): "))
                    break # Exit loop if input is a valid integer
                except ValueError:
                    print("Invalid input. Please enter a whole number for the shift.")
            
            encoded_msg = encode_message(original_msg, shift)
            print(f"Your encoded message is: {encoded_msg}")
        
        elif choice == '2':
            # User wants to decode
            encoded_msg_input = input("Enter the encoded message to decode: ")
            
            # Get the original shift amount used for encoding
            while True:
                try:
                    shift = int(input("Enter the original shift amount used for encoding: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number for the shift.")

            decoded_msg = decode_message(encoded_msg_input, shift)
            print(f"Your decoded message is: {decoded_msg}")
        
        elif choice == '3':
            # User wants to exit
            print("Exiting the Secret Message Shifter. Goodbye!")
            break # Breaks out of the 'while True' loop
        
        else:
            # Handle invalid choices
            print("Invalid choice. Please enter 1, 2, or 3.")
```
