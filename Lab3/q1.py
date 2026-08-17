import math

p = 61
q = 53
n = p * q
phi = (p - 1) * (q - 1)

e = 17
d = pow(e, -1, phi)

message = "Asymmetric Encryption"

encrypted = [pow(ord(ch), e, n) for ch in message]
decrypted = ''.join(chr(pow(c, d, n)) for c in encrypted)

print("Public Key:", (n, e))
print("Private Key:", (n, d))
print("Ciphertext:", encrypted)
print("Decrypted Message:", decrypted)