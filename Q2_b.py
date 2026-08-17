def encrypt(text, key):
    text = text.upper().replace(" ", "")
    cipher = ""

    key_stream = [key]
    for ch in text[:-1]:
        key_stream.append(ord(ch) - ord('A'))

    for i in range(len(text)):
        p = ord(text[i]) - ord('A')
        c = (p + key_stream[i]) % 26
        cipher += chr(c + ord('A'))

    return cipher


def decrypt(cipher, key):
    cipher = cipher.upper()
    plain = ""

    current_key = key

    for ch in cipher:
        c = ord(ch) - ord('A')
        p = (c - current_key) % 26
        plain += chr(p + ord('A'))

        current_key = p

    return plain


def main():
    plaintext = input("Enter Plaintext: ")

    key = 7

    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    print("\nOriginal Plaintext :", plaintext.upper().replace(" ", ""))
    print("Ciphertext         :", ciphertext)
    print("Decrypted Text     :", decrypted)


if __name__ == "__main__":
    main()