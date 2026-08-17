def decrypt(text, key):
    return "".join(chr((ord(c)-65-key)%26+65) for c in text)

def main():
    plain = "YES"
    cipher = "CIW"

    key = (ord(cipher[0])-ord(plain[0])) % 26

    print("Attack Type : Known Plaintext Attack")
    print("Key         :", key)
    print("Plaintext   :", decrypt("XVIEWYWI", key))

if __name__ == "__main__":
    main()