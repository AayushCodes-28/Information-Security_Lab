import random

p = 467
g = 2

x = random.randint(1, p - 2)
y = pow(g, x, p)

message = "Confidential Data"

encrypted = []

for ch in message:
    m = ord(ch)
    k = random.randint(1, p - 2)
    c1 = pow(g, k, p)
    c2 = (m * pow(y, k, p)) % p
    encrypted.append((c1, c2))

decrypted = ""

for c1, c2 in encrypted:
    s = pow(c1, x, p)
    m = (c2 * pow(s, -1, p)) % p
    decrypted += chr(m)

print("Public Key:", (p, g, y))
print("Private Key:", x)
print("Ciphertext:", encrypted)
print("Decrypted Message:", decrypted)