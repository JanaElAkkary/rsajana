import time
import math
from generatingnumbers import is_prime, generate_prime, extended_gcd, generate_keys, euler_phi


def brute_force(encrypted_message, e, n, phi):
    start_time = time.perf_counter() 
    d = 2  # Start with the smallest possible prime exponent
    attempts=0
    decrypted = False
    while not decrypted:
        if (e * d)% phi == 1:  # Check if end is congruent to 1 modulos phi(n)
            decrypted = True
        else:
            d += 1
            attempts+=1
        if d >= 2**16:  # Limiting to 16 bits
            break
    end_time = time.perf_counter()  
    runtime = (end_time - start_time) * 1000  
    return d, runtime, attempts

def main():
    message = int(input("Enter the message to encrypt: "))
    p = int(input("Enter the prime number (p): "))
    q = int(input("Enter the prime number (q): "))
    e = int(input("Enter the public exponent (e): "))
    n = p * q
    phi = euler_phi(n)
    encrypted_message =pow(message, e, n)
    d, runtime, attempts = brute_force(encrypted_message, e, n, phi)
    decrypted_message=pow(encrypted_message, d, n)
    public=(n,e)
    private=(n,d)
    print("the public key is: ", public,"private is: ",private)
    print(f"Encrypted message: {encrypted_message}")
    print(f"decrypted message is: {decrypted_message}")
    print(f"Private exponent found: {d}")
    print(f"Runtime: {runtime:.4f} milliseconds")
    print(f"attempts: ", attempts)

if __name__ == "__main__":
    main()
