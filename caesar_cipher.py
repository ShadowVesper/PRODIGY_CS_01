message = input("Enter a message: ").upper()
shift = int(input("Enter shift value: "))
choice = input("Encrypt or Decrypt? (E/D): ").upper()
while choice not in ["E", "D"]:
    print("Invalid choice! Please enter E or D.")
    choice = input("Encrypy or Decrypt? (E/D): ").upper()

encrypted_message = ""

for letter in message:
    if letter.isalpha():
        position = ord(letter) - 65

        if choice == "E":
            new_position = (position + shift) % 26
        else:
            new_position = (position - shift) % 26

        new_letter = chr(new_position + 65)
        encrypted_message += new_letter

    else:
        encrypted_message += letter

if choice =="E":
    print("Encrypted message:", encrypted_message)
else:
    print("Decrypted message:", encrypted_message)

    