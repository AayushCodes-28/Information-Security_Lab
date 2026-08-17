from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

ephemeral_private = ec.generate_private_key(ec.SECP256R1())
ephemeral_public = ephemeral_private.public_key()

shared_key = ephemeral_private.exchange(ec.ECDH(), public_key)

key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b"ECC Encryption"
).derive(shared_key)

message = b"Secure Transactions"
nonce = os.urandom(12)

ciphertext = AESGCM(key).encrypt(nonce, message, None)

receiver_shared_key = private_key.exchange(ec.ECDH(), ephemeral_public)

receiver_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=None,
    info=b"ECC Encryption"
).derive(receiver_shared_key)

plaintext = AESGCM(receiver_key).decrypt(nonce, ciphertext, None)

print("Private Key:", private_key.private_numbers().private_value)
print("Public Key:", public_key.public_numbers())
print("Ciphertext:", ciphertext.hex())
print("Decrypted Message:", plaintext.decode())