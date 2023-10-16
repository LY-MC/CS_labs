def generate_playfair_key(key):
    key = key.replace(" ", "").upper()
    key = key.replace("J", "I").upper()
    key_set = set()
    playfair_key = ""

    for char in key:
        if char not in key_set:
            key_set.add(char)
            playfair_key += char

    alphabet = "AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ"

    for char in alphabet:
        if char not in key_set:
            playfair_key += char

    key_matrix = [['' for _ in range(5)] for _ in range(6)]
    index = 0

    for i in range(6):
        for j in range(5):
            key_matrix[i][j] = playfair_key[index]
            index += 1

    print("Playfair Key Matrix:")
    for row in key_matrix:
        print(" ".join(row))
    print()

    return key_matrix


def find_coordinates(matrix, char):
    for i in range(6):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j


def playfair_encrypt(plain_text, key):
    playfair_key = generate_playfair_key(key)
    prepared_text = prepare_input(plain_text)
    encrypted_text = ""

    for i in range(0, len(prepared_text), 2):
        char1 = prepared_text[i]
        char2 = prepared_text[i + 1]

        if char1 == 'J':
            char1 = 'I'

        row1, col1 = find_coordinates(playfair_key, char1)
        row2, col2 = find_coordinates(playfair_key, char2)

        if row1 == row2:
            encrypted_char1 = playfair_key[row1][(col1 + 1) % 6]
            encrypted_char2 = playfair_key[row2][(col2 + 1) % 6]
        elif col1 == col2:
            encrypted_char1 = playfair_key[(row1 + 1) % 6][col1]
            encrypted_char2 = playfair_key[(row2 + 1) % 6][col2]
        else:
            encrypted_char1 = playfair_key[row1][col2]
            encrypted_char2 = playfair_key[row2][col1]

        encrypted_text += encrypted_char1
        encrypted_text += encrypted_char2

    return encrypted_text


def prepare_input(text):
    text = text.replace(" ", "").upper()
    prepared_text = ""
    i = 0

    while i < len(text):
        if i == len(text) - 1:
            prepared_text += text[i] + "X"
            break

        if text[i] == text[i + 1]:
            prepared_text += text[i] + "X"
            i += 1
        else:
            prepared_text += text[i] + text[i + 1]
            i += 2

    return prepared_text


def playfair_decrypt(cipher_text, key):
    playfair_key = generate_playfair_key(key)
    decrypted_text = ""

    for i in range(0, len(cipher_text), 2):
        char1 = cipher_text[i].upper()
        char2 = cipher_text[i + 1].upper()

        if char1 == 'J':
            char1 = 'I'
        if char2 == 'J':
            char2 = 'I'

        row1, col1 = find_coordinates(playfair_key, char1)
        row2, col2 = find_coordinates(playfair_key, char2)

        if row1 == row2:
            decrypted_char1 = playfair_key[row1][(col1 - 1) % 6]
            decrypted_char2 = playfair_key[row2][(col2 - 1) % 6]
        elif col1 == col2:
            decrypted_char1 = playfair_key[(row1 - 1) % 6][col1]
            decrypted_char2 = playfair_key[(row2 - 1) % 6][col2]
        else:
            decrypted_char1 = playfair_key[row1][col2]
            decrypted_char2 = playfair_key[row2][col1]

        decrypted_text += decrypted_char1
        decrypted_text += decrypted_char2

        i += 2

    return decrypted_text


def main():
    while True:
        key = input("Enter the key (at least 7 characters): ")
        if len(key) >= 7:
            break
        else:
            print("Key must be at least 7 characters long.")

    choice = input("Choose 'E' for encryption or 'D' for decryption: ").upper()

    if choice == 'E':
        plain_text = input("Enter the plaintext: ")
        cipher_text = playfair_encrypt(plain_text, key)
        print("Encrypted:", cipher_text)
    elif choice == 'D':
        cipher_text = input("Enter the ciphertext: ")
        decrypted_text = playfair_decrypt(cipher_text, key)
        print("Decrypted:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")


if __name__ == "__main__":
    main()
