import math
import time
from generatingnumbers import is_prime, generate_prime, extended_gcd, generate_keys, euler_phi

def factorize(p, q, e):   
    start_time = time.perf_counter()  
    n = p * q
    euler_phi = (p - 1) * (q - 1)
    
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
    
    d = extended_gcd(e, euler_phi)[1] % euler_phi

    end_time = time.perf_counter() 
    runtime = (end_time - start_time) * 1000  

    return factors, d, runtime

def main():
    p = int(input("Enter the prime number (p): "))
    q = int(input("Enter the prime number (q): "))
    e = int(input("Enter the public exponent (e): "))

    factors, d, runtime = factorize(p, q, e)

    print(f"\nThe factors of {p*q} are: {factors}")
    print(f"Calculated private exponent d: {d}")
    print(f"Runtime: {runtime:.4f} milliseconds")

if __name__ == "__main__":
    main()
