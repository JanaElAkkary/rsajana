# This Python script implements a function to factorize a composite number using trial division and calculate the private exponent based on a given public exponent. It also measures the runtime of the factorization process.

import math
import time
from generatingnumbers import is_prime, generate_prime, extended_gcd, generate_keys ,euler_phi

def factorize(n, e):   
    start_time = time.perf_counter()  
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    if n > 2:
        factors.append(n)
    end_time = time.perf_counter() 
    runtime = (end_time - start_time) * 1000  

    euler_phi = (factors[0] - 1) * (factors[1] - 1)
    d = extended_gcd(e, euler_phi)[1] % euler_phi

    return factors, d, runtime
#   """
#     Factorize the modulus n and compute the private exponent d.
    
#     Parameters:
#     n (int): The modulus
#     e (int): The public exponent
    
#     Returns:
#     tuple: A tuple containing the prime factors of n, 
#            the private exponent d, and the runtime in milliseconds
#     """
def main():
    p = int(input("Enter the prime number (p): "))
    q = int(input("Enter the prime number (q): "))
    e = int(input("Enter the public exponent (e): "))
    message = int(input("Enter the message to encrypt: "))

    n=p*q
    factors, d, runtime = factorize(n, e)
    public=(n,e)
    private=(n,d)
    print("the public key is: ", public,"private is: ",private)
    encryption=pow(message, e, n)
    decryption=pow(encryption, d, n)
    print("encryption: ", encryption)
    print("decryption: ", decryption)
    print(f"\nThe factors of {n} are: {factors}")
    print(f"Calculated private exponent d: {d}")
    print(f"Runtime: {runtime:.4f} milliseconds")

        
    # Main function to factorize a composite number and compute the private exponent d.
    

if __name__ == "__main__":
    main()




