def encrypt(text, key):
    text = text.upper().replace(" ", "")
    cipher = ""

    for ch in text:
        x = ord(ch) - ord('A')
        cipher += chr((x + key) % 26 + ord('A'))

    return cipher


def decrypt(cipher, key):
    plain = ""

    for ch in cipher:
        x = ord(ch) - ord('A')
        plain += chr((x - key) % 26 + ord('A'))

    return plain


def main():
    plaintext = input("Enter Plaintext: ")
    key = 20

    ciphertext = encrypt(plaintext, key)
    decrypted = decrypt(ciphertext, key)

    print("\nOriginal Plaintext :", plaintext.upper().replace(" ", ""))
    print("Ciphertext         :", ciphertext)
    print("Decrypted Text     :", decrypted)


if __name__ == "__main__":
    main()