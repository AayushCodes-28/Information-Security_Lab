from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

plaintext = b"Sensitive Information"

key = bytes.fromhex(
    "0123456789ABCDEF0123456789ABCDEF"
)

cipher = AES.new(key, AES.MODE_ECB)

padded_text = pad(plaintext, AES.block_size)
ciphertext = cipher.encrypt(padded_text)

print("Ciphertext (hex):", ciphertext.hex().upper())

cipher = AES.new(key, AES.MODE_ECB)

decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Decrypted text:", decrypted.decode())