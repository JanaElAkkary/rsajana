# This Python code generates RSA public and private keys of specified bit length.

import random
import math 
#importing all necessary modules 'random' and 'math'
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
#    """
#     Check if a number is prime.
    
#     Parameters:
#     number (int): The number to check
    
#     Returns:
#     bool: True if the number is prime, False otherwise
#     """

def generate_prime(bit_length):
    # This function generates a random prime number of specified bit length.
    while True:
        prime = random.getrandbits(bit_length)
        if is_prime(prime):
            return prime
#   """
#     Generate a random prime number of a specified bit length.
    
#     Parameters:p
#     bit_length (int): The desired bit length of the prime number
    
#     Returns:
#     int: A random prime number with the specified bit length
#     """
def extended_gcd(a, b):

    x0, x1, y0, y1 = 1, 0, 0, 1
    while b:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0-q*x1 
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0
#  """
#     Compute the extended greatest common divisor (GCD) of two integers a and b.
#     Additionally, compute the coefficients x and y such that ax + by = gcd(a, b).
    
#     Parameters:
#     a (int): The first integer
#     b (int): The second integer
    
#     Returns:
#     tuple: A tuple containing the GCD of a and b, and the coefficients x and y
#     """

def generate_keys(bit_length):
    p = generate_prime(bit_length)
    q = generate_prime(bit_length)
#    """
#     Generate RSA public and private keys.
    
#     Parameters:
#     bit_length (int): The desired bit length for the prime numbers
    
#     Returns:
#     tuple: A tuple containing the prime numbers p and q, 
#            public and private exponents e and d,
#            Euler's totient phi, modulus n,
#            and the public and private keys (e, n) and (d, n)
#      """
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