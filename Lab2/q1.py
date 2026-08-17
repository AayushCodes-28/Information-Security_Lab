from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

plaintext = b"Confidential Data"
key = b"A1B2C3D4"

cipher = DES.new(key, DES.MODE_ECB)

padded_text = pad(plaintext, DES.block_size)
ciphertext = cipher.encrypt(padded_text)

print("Ciphertext (hex):", ciphertext.hex().upper())

cipher = DES.new(key, DES.MODE_ECB)

decrypted = unpad(cipher.decrypt(ciphertext), DES.block_size)

print("Decrypted text:", decrypted.decode())