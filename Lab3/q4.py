import os
import time
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

def rsa_test(data):
    start = time.perf_counter()

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    key_generation = time.perf_counter() - start

    start = time.perf_counter()

    aes_key = os.urandom(32)
    aes_encrypted = AESGCM(aes_key)
    nonce = os.urandom(12)
    encrypted_key = private_key.public_key().encrypt(
        aes_key,
        __import__("cryptography").hazmat.primitives.asymmetric.padding.OAEP(
            mgf=__import__("cryptography").hazmat.primitives.asymmetric.padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    ciphertext = aes_encrypted.encrypt(nonce, data, None)

    encryption_time = time.perf_counter() - start

    start = time.perf_counter()

    aes_key = private_key.decrypt(
        encrypted_key,
        __import__("cryptography").hazmat.primitives.asymmetric.padding.OAEP(
            mgf=__import__("cryptography").hazmat.primitives.asymmetric.padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    plaintext = AESGCM(aes_key).decrypt(nonce, ciphertext, None)

    decryption_time = time.perf_counter() - start

    return key_generation, encryption_time, decryption_time, plaintext


def ecc_test(data):
    start = time.perf_counter()

    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    key_generation = time.perf_counter() - start

    start = time.perf_counter()

    ephemeral_private = ec.generate_private_key(ec.SECP256R1())
    shared_key = ephemeral_private.exchange(
        ec.ECDH(),
        public_key
    )

    key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"File Transfer"
    ).derive(shared_key)

    nonce = os.urandom(12)
    ciphertext = AESGCM(key).encrypt(nonce, data, None)

    encryption_time = time.perf_counter() - start

    start = time.perf_counter()

    ephemeral_public = ephemeral_private.public_key()

    shared_key = private_key.exchange(
        ec.ECDH(),
        ephemeral_public
    )

    key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b"File Transfer"
    ).derive(shared_key)

    plaintext = AESGCM(key).decrypt(nonce, ciphertext, None)

    decryption_time = time.perf_counter() - start

    return key_generation, encryption_time, decryption_time, plaintext


for size in [1, 10]:
    data = os.urandom(size * 1024 * 1024)

    rsa_result = rsa_test(data)
    ecc_result = ecc_test(data)

    print("\nFile Size:", size, "MB")

    print("\nRSA 2048")
    print("Key Generation:", rsa_result[0])
    print("Encryption:", rsa_result[1])
    print("Decryption:", rsa_result[2])
    print("Correct:", rsa_result[3] == data)

    print("\nECC secp256r1")
    print("Key Generation:", ecc_result[0])
    print("Encryption:", ecc_result[1])
    print("Decryption:", ecc_result[2])
    print("Correct:", ecc_result[3] == data)