def matrix(key):
    key = "".join(dict.fromkeys((key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").upper().replace("J", "I")))
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def pos(m, ch):
    ch = "I" if ch == "J" else ch
    for i in range(5):
        for j in range(5):
            if m[i][j] == ch:
                return i, j

def prepare(text):
    text = text.upper().replace(" ", "").replace("J", "I")
    out, i = "", 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else "X"
        if a == b:
            out += a + "X"
            i += 1
        else:
            out += a + b
            i += 2
    return out if len(out)%2==0 else out+"X"

def process(text, m, d):
    text = prepare(text) if d==1 else text
    out = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        r1,c1 = pos(m,a)
        r2,c2 = pos(m,b)

        if r1 == r2:
            out += m[r1][(c1+d)%5] + m[r2][(c2+d)%5]
        elif c1 == c2:
            out += m[(r1+d)%5][c1] + m[(r2+d)%5][c2]
        else:
            out += m[r1][c2] + m[r2][c1]
    return out

def main():
    m = matrix("GUIDANCE")

    text = input("Enter Plaintext: ")

    cipher = process(text, m, 1)
    plain = process(cipher, m, -1)

    print("\nPlayfair Matrix")
    for row in m:
        print(*row)

    print("\nCiphertext :", cipher)
    print("Plaintext  :", plain)

if __name__ == "__main__":
    main()