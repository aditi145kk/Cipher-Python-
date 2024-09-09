import string

def caesar_encrypt(message, key, direction='right'):
    if direction == 'left':
        key = -key

    shift = key % 26

    lower_cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    )
    upper_cipher = str.maketrans(
        string.ascii_uppercase,
        string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    )

    encrypted_message = message.translate(lower_cipher).translate(upper_cipher)

    return encrypted_message


def caesar_decrypt(encrypted_message, key, direction='right'):
    if direction == 'left':
        key = -key

    shift = 26 - (key % 26)

    lower_cipher = str.maketrans(
        string.ascii_lowercase,
        string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
    )
    upper_cipher = str.maketrans(
        string.ascii_uppercase,
        string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
    )

    message = encrypted_message.translate(lower_cipher).translate(upper_cipher)
    return message

def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            key = input("Enter the key (an integer): ")
            direction = input("Shift direction (right/left): ").lower()

            try:
                key = int(key)
                encrypted_message = caesar_encrypt(message, key, direction)
                print(f'Encrypted Message: {encrypted_message}')
            except ValueError:
                print("Invalid key. Please enter an integer.")
            print()

        elif choice == '2':
            encrypted_message = input("Enter the message to decrypt: ")
            key = input("Enter the key (an integer): ")
            direction = input("Shift direction (right/left): ").lower()

            try:
                key = int(key)
                decrypted_message = caesar_decrypt(encrypted_message, key, direction)
                print(f'Decrypted Message: {decrypted_message}')
            except ValueError:
                print("Invalid key. Please enter an integer.")
            print()

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
            print()

if __name__ == "__main__":
    main()
