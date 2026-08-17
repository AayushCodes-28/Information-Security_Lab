from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

plaintext = b"Classified Text"

# Given 3DES key
key_hex = "1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"

# Split into three 8-byte DES keys
K1 = bytes.fromhex(key_hex[0:16])
K2 = bytes.fromhex(key_hex[16:32])
K3 = bytes.fromhex(key_hex[32:48])

print("Plaintext :", plaintext.decode())
print("K1        :", K1.hex().upper())
print("K2        :", K2.hex().upper())
print("K3        :", K3.hex().upper())

padded = pad(plaintext, 8)

print("\nPadded Plaintext:")
print(padded.hex().upper())

# Step 1: DES Encryption with K1
des1 = DES.new(K1, DES.MODE_ECB)
step1 = des1.encrypt(padded)

print("\nAfter DES Encryption K1:")
print(step1.hex().upper())


# Step 2: DES Decryption with K2
des2 = DES.new(K2, DES.MODE_ECB)
step2 = des2.decrypt(step1)

print("\nAfter DES Decryption K2:")
print(step2.hex().upper())


# Step 3: DES Encryption with K3
des3 = DES.new(K3, DES.MODE_ECB)
ciphertext = des3.encrypt(step2)

print("\nFinal Ciphertext:")
print(ciphertext.hex().upper())


# Step 1: DES Decryption with K3
des3_dec = DES.new(K3, DES.MODE_ECB)
step1_dec = des3_dec.decrypt(ciphertext)

print("\nDecryption Step 1 - D(K3):")
print(step1_dec.hex().upper())


# Step 2: DES Encryption with K2
des2_dec = DES.new(K2, DES.MODE_ECB)
step2_dec = des2_dec.encrypt(step1_dec)

print("\nDecryption Step 2 - E(K2):")
print(step2_dec.hex().upper())


# Step 3: DES Decryption with K1
des1_dec = DES.new(K1, DES.MODE_ECB)
decrypted_padded = des1_dec.decrypt(step2_dec)

# Remove padding
decrypted = unpad(decrypted_padded, 8)

print("\nDecrypted Text:")
print(decrypted.decode())


if decrypted == plaintext:
    print("\nVerification: SUCCESS")
else:
    print("\nVerification: FAILED")