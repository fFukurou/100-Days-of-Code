#Caesar Cipher Project
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, message, shift):
    if shift < 0:
        shift = -shift

    if shift > 25:
        shift = shift % 25

        
    if direction == 'encode':
        encrypted_message = ""
        for letter in message:
            if letter in alphabet:
                if alphabet.index(letter) + shift > 25:
                    new_shift = alphabet.index(letter) + shift - 26
                    encrypted_message += alphabet[new_shift]
                else:
                    encrypted_message += alphabet[alphabet.index(letter) + shift]
            else:
                encrypted_message += letter

        print(f" The encrypted message is : {encrypted_message}\n")
                
    elif direction == "decode":
        decrypted_message = ""
        for letter in message:
            if letter in alphabet:
                if alphabet.index(letter) - shift < 0:
                    new_shift = alphabet.index(letter) - shift + 26
                    decrypted_message += alphabet[new_shift]
                else:
                    decrypted_message += alphabet[alphabet.index(letter) - shift]
            else:
                decrypted_message += letter

        print(f" The decrypted message is : {decrypted_message}\n")


print(logo)
while True:
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction != "encode" and direction != "decode":
            print("Invalid input, try again.\n")
        else:
            break
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, message, shift)
    repeat = input("Do you want to go again? (yes/no)\n")
    if repeat == 'yes':
        pass
    else:
        print("\nProgram ended.\n")
        break