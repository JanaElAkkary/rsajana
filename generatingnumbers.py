# This Python code generates RSA public and private keys of specified bit length.

import random 
#importing all necessary modules 'random' and 'math'
import math 
#importing all necessary modules 'random' and 'math'
def is_prime(number):#0(c)
    if number < 2:#0(c)
        return False#0(c)
    for i in range(2, int(number**0.5) + 1):#o(n)
        if number % i == 0:#0(c)
            return False#0(c)
    return True#0(c)
#    """
#     Check if a number is prime.
    
#     Parameters:
#     number (int): The number to check
    
#     Returns:
#     bool: True if the number is prime, False otherwise
#     """

def generate_prime(bit_length):#0(c)
    # This function generates a random prime number of specified bit length.
    while True:#o(n)
        prime = random.getrandbits(bit_length)#0(c)
        if is_prime(prime):#0(c)
            return prime#0(c)
#   """
#     Generate a random prime number of a specified bit length.
    
#     Parameters:p
#     bit_length (int): The desired bit length of the prime number
    
#     Returns:
#     int: A random prime number with the specified bit length
#     """
def extended_gcd(a, b):#0(c)

    x0, x1, y0, y1 = 1, 0, 0, 1#0(c)
    while b:#o(n)
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0-q*x1 
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0#0(c)
#  """
#     Compute the extended greatest common divisor (GCD) of two integers a and b.
#     Additionally, compute the coefficients x and y such that ax + by = gcd(a, b).
    
#     Parameters:
#     a (int): The first integer
#     b (int): The second integer
    
#     Returns:
#     tuple: A tuple containing the GCD of a and b, and the coefficients x and y
#     """

def generate_keys(bit_length):#0(c)
    p = generate_prime(bit_length)#0(c)
    q = generate_prime(bit_length)#0(c)
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
    while p == q:#o(n)
        q = generate_prime(bit_length)#0(c)

    n = p * q#0(c)
    euler_phi = (p - 1) * (q - 1)#0(c)
    e = random.randint(3, euler_phi - 1)#0(c)

    while True:#o(n)
        gcd, x, y = extended_gcd(e, euler_phi)#0(c)
        if gcd == 1:#0(c)
            d = x % euler_phi#0(c)
            break#0(c)
        else:#0(c)
            e = random.randint(3, euler_phi - 1)#0(c)

    return p, q, e, euler_phi, n, (e, n), (d, n)#0(c)

bit_length = int(input("Choose bit length (8 or 16): "))#0(c)
p, q, e, euler_phi, n, public_key, private_key = generate_keys(bit_length)#0(c)

print("p:", p)#0(c)
print("q:", q)#0(c)
print("e:", e)#0(c)
print("n:", n)#0(c)
print("Euler's phi:", euler_phi)#0(c)
print("Public key (e, n):", public_key)#0(c)
print("Private key (d, n):", private_key)#0(c)