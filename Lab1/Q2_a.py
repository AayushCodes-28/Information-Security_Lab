Hellodef encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = key.upper()
    cipher = ""

    for i in range(len(text)):
        p = ord(text[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        cipher += chr((p + k) % 26 + ord('A'))

    return cipher


def decrypt(cipher, key):
    key = key.upper()
    plain = ""

    for i in range(len(cipher)):
        c = ord(cipher[i]) - ord('A')
        k = ord(key[i % len(key)]) - ord('A')
        plain += chr((c - k) % 26 + ord('A'))

    return plain


def main():
    plaintext = input("Enter Plaintext: ")

    key = "DOLLARS"

    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    print("\nOriginal Plaintext :", plaintext.upper().replace(" ", ""))
    print("Ciphertext         :", ciphertext)
    print("Decrypted Text     :", decrypted)


if __name__ == "__main__":
    main()