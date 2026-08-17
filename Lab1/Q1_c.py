def encrypt(text, a, b):
    text = text.upper().replace(" ", "")
    cipher = ""

    for ch in text:
        if ch.isalpha():
            x = ord(ch) - ord('A')
            cipher += chr((a * x + b) % 26 + ord('A'))

    return cipher


def decrypt(cipher, a_inverse, b):
    plain = ""

    for ch in cipher:
        y = ord(ch) - ord('A')
        plain += chr((a_inverse * (y - b)) % 26 + ord('A'))

    return plain


def main():
    plaintext = input("Enter Plaintext: ")

    a = 15
    b = 20
    a_inverse = 7        # Inverse of 15 modulo 26

    ciphertext = encrypt(plaintext, a, b)
    decrypted = decrypt(ciphertext, a_inverse, b)

    print("\nOriginal Plaintext :", plaintext.upper().replace(" ", ""))
    print("Ciphertext         :", ciphertext)
    print("Decrypted Text     :", decrypted)


if __name__ == "__main__":
    main()