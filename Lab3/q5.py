import random
import time

p = 23
g = 5

start = time.perf_counter()

alice_private = random.randint(2, p - 2)
bob_private = random.randint(2, p - 2)

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

key_generation_time = time.perf_counter() - start

start = time.perf_counter()

alice_shared = pow(bob_public, alice_private, p)
bob_shared = pow(alice_public, bob_private, p)

key_exchange_time = time.perf_counter() - start

print("Public Parameters:", (p, g))
print("Alice Private Key:", alice_private)
print("Alice Public Key:", alice_public)
print("Bob Private Key:", bob_private)
print("Bob Public Key:", bob_public)
print("Alice Shared Secret:", alice_shared)
print("Bob Shared Secret:", bob_shared)
print("Keys Match:", alice_shared == bob_shared)
print("Key Generation Time:", key_generation_time)
print("Key Exchange Time:", key_exchange_time)