from math import gcd

cipher = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"

def inv(a):
    return next(i for i in range(26) if (a*i)%26==1)

for a in range(1,26):
    if gcd(a,26)==1:
        ai = inv(a)
        for b in range(26):
            text = ""
            for c in cipher:
                x = (ai*((ord(c)-65)-b)) % 26
                text += chr(x+65)
            print(f"a={a:2} b={b:2} -> {text}")