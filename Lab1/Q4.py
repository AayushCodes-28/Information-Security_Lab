import numpy as np

K = np.array([[3, 3],
              [2, 7]])

def clean(text):
    text = "".join(c for c in text.upper() if c.isalpha())
    return text + ("X" if len(text) % 2 else "")

def inv_key(K):
    a, b = K[0]
    c, d = K[1]
    det = (a*d - b*c) % 26
    det_inv = next(i for i in range(26) if (det*i) % 26 == 1)
    return (det_inv * np.array([[d,-b],[-c,a]])) % 26

def convert(text, M):
    text = clean(text)
    out = ""
    for i in range(0, len(text), 2):
        v = np.array([[ord(text[i])-65],
                      [ord(text[i+1])-65]])
        r = (M @ v) % 26
        out += chr(r[0,0]+65) + chr(r[1,0]+65)
    return out

def main():
    text = input("Enter Plaintext: ")

    cipher = convert(text, K)
    plain = convert(cipher, inv_key(K))

    print("Ciphertext :", cipher)
    print("Plaintext  :", plain)

if __name__ == "__main__":
    main()