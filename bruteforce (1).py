import time
from generatingnumbers import is_prime, generate_prime, extended_gcd, generate_keys

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def decrypt(encrypted_message, d, n):
    return ''.join([chr(pow(char, d, n) % 65536) for char in encrypted_message])

def brute_force(encrypted_message, e, n):
    start_time = time.perf_counter() 
    d = 2  # Start with the smallest possible prime exponent
    decrypted = False
    while not decrypted:
        if pow(e, d, n) == 1:  # Check if e*d is congruent to 1 modulo phi(n)
            decrypted = True
        else:
            d += 1
        if d >= 2**16:  # Limiting to 16 bits
            break
    end_time = time.perf_counter()  
    runtime = (end_time - start_time) * 1000  
    return d, runtime

def main():
    p = generate_prime(8)  # Generate 8-bit primes for demonstration
    q = generate_prime(8)
    e = int(input("Enter the public exponent (e): "))
    n = p * q

    message = input("Enter the message to encrypt and decrypt: ")
    encrypted_message = encrypt(message, e, n)

    d, runtime = brute_force(encrypted_message, e, n)

    print(f"Encrypted message: {encrypted_message}")
    print(f"Private exponent found: {d}")
    print(f"Runtime: {runtime:.4f} milliseconds")

if __name__ == "__main__":
    main()
