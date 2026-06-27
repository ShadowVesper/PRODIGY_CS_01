# Get user input
message = input("Enter a message: ").upper()

# Get the shift value
shift = int(input("Enter shift value: "))
# Get user's choice (Encrypt or decrypt)
choice = input("Encrypt or Decrypt? (E/D): ").upper()
# Keep asking until a valid choice is entered
while choice not in ["E", "D"]:
    print("Invalid choice! Please enter E or D.")
    choice = input("Encrypt or Decrypt? (E/D): ").upper()

encrypted_message = ""

# Loop through every character in the message 
for letter in message:
    # Check if the character is a letter
    if letter.isalpha():
        # ord() returns the ASCII value of a letter.
        # We subtract 65 because 'A' has an ASCII value of 65.
        # This converts letters into a simpler alphabet position:
        # A = 0, B = 1, C = 2, ..., Z = 25.
        # Using positions makes it easy to shift letters with modulo arithmetic.

        position = ord(letter) - 65

        if choice == "E":
            new_position = (position + shift) % 26
        else:
            new_position = (position - shift) % 26
    
        # Convert the new position back to a letter
        # chr() then converts the ASCII value back into the corresponding letter.
        # Add 65 to convert the alphabet position back to its ASCII value.
         
        new_letter = chr(new_position + 65)
        encrypted_message += new_letter

    # Keep spaces and punctuations unchanged
    else:
        encrypted_message += letter

if choice =="E":
    print("Encrypted message:", encrypted_message)
else:
    print("Decrypted message:", encrypted_message)

    