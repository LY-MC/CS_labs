def create_new_alphabet(key2=None):
    new_alphabet = ""

    if key2:
        for char in key2:
            if char not in new_alphabet:
                new_alphabet += char

    for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if char not in new_alphabet:
            new_alphabet += char

    print('New alphabet:' + new_alphabet)
    return new_alphabet


def caesar_cipher(text, key1, key2, mode='encryption'):
    result = ""
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if key2 == '':
        new_alphabet = alphabet
    else:
        new_alphabet = create_new_alphabet(key2)

    for char in text:
        if char.isalpha():
            if char.isupper():
                index = alphabet.index(char)
            else:
                index = alphabet.index(char.upper())

            if mode == 'encryption':
                shifted_char = new_alphabet[(index + key1) % 26]
            else:
                shifted_index = (new_alphabet.index(char) - key1) % 26

                if shifted_index < 0:
                    shifted_index += 26

                shifted_char = alphabet[shifted_index]

            result += shifted_char
        else:
            result += char

    return result


def validate_key1(key):
    if key.isdigit():
        key = int(key)
        if 1 <= key <= 25:
            return key
    return None


def validate_key2(key):
    if len(key) == 0:
        return ''
    elif all(char.isalpha() for char in key) and len(key) >= 7:
        return key.upper()
    return None


def main():
    while True:
        mode = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
        if mode not in ('e', 'd'):
            print("Invalid input. Please enter 'e' or 'd'.")
            continue

        key1 = input("Enter the key (1-25): ")
        key1 = validate_key1(key1)

        if key1 is None:
            print("Invalid key. Key 1 must be an integer between 1 and 25.")
            continue

        key2 = input("(Optional) Enter Key 2 (a word or phrase, at least 7 characters): ")
        key2 = validate_key2(key2)

        if key2 is None:
            print("Invalid Key 2. Key 2 must contain only letters of the Latin alphabet and be at least 7 characters long.")
            continue

        message = input("Enter the message: ")
        message = message.upper().replace(" ", "")

        if mode == 'e':
            result = caesar_cipher(message, key1, key2, 'encryption')
        else:
            result = caesar_cipher(message, key1, key2, 'decryption')

        print(f"Result: {result}")

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break


if __name__ == "__main__":
    main()
