from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
import time

plaintext = b"Performance Testing of Encryption Algorithms"

des_key = b"A1B2C3D4"

aes_key = bytes.fromhex(
    "0123456789ABCDEF0123456789ABCDEF"
    "0123456789ABCDEF"
)

des = DES.new(des_key, DES.MODE_ECB)

padded_des = pad(plaintext, DES.block_size)

start = time.perf_counter_ns()
des_ciphertext = des.encrypt(padded_des)
des_encryption_time = time.perf_counter_ns() - start

start = time.perf_counter_ns()
des_plaintext = unpad(des.decrypt(des_ciphertext), DES.block_size)
des_decryption_time = time.perf_counter_ns() - start



aes = AES.new(aes_key, AES.MODE_ECB)

padded_aes = pad(plaintext, AES.block_size)

start = time.perf_counter_ns()
aes_ciphertext = aes.encrypt(padded_aes)
aes_encryption_time = time.perf_counter_ns() - start

start = time.perf_counter_ns()
aes_plaintext = unpad(aes.decrypt(aes_ciphertext), AES.block_size)
aes_decryption_time = time.perf_counter_ns() - start


print("DES Encryption :", des_encryption_time, "ns")
print("DES Decryption :", des_decryption_time, "ns")

print("AES-256 Encryption :", aes_encryption_time, "ns")
print("AES-256 Decryption :", aes_decryption_time, "ns")

print("\nDES decrypted :", des_plaintext.decode())
print("AES decrypted:", aes_plaintext.decode())