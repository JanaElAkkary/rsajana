# This Python code generates RSA public and private keys of specified bit length.

import random
import math 
#importing all necessary imports
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(bit_length):
    # This function generates a random prime number of specified bit length.
    while True:
        prime = random.getrandbits(bit_length)
        if is_prime(prime):
            return prime

def extended_gcd(a, b):
    
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

def generate_keys(bit_length):
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)

    while p == q:
        q = generate_prime(bit_length)

    n = p * q
    euler_phi = (p - 1) * (q - 1)
    e = random.randint(3, euler_phi - 1)

    while True:
        gcd, x, y = extended_gcd(e, euler_phi)
        if gcd == 1:
            d = x % euler_phi
            break
        else:
            e = random.randint(3, euler_phi - 1)

    return p, q, e, euler_phi, n, (e, n), (d, n)

bit_length = int(input("Choose bit length (8 or 16): "))
p, q, e, euler_phi, n, public_key, private_key = generate_keys(bit_length)

print("p:", p)
print("q:", q)
print("e:", e)
print("n:", n)
print("Euler's phi:", euler_phi)
print("Public key (e, n):", public_key)
print("Private key (d, n):", private_key)
