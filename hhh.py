import time
from generatingnumbers import is_prime, generate_prime, extended_gcd, generate_keys, euler_phi

def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

def decrypt(encrypted_message, d, n):
    return ''.join([chr(pow(char, d, n) % 65536) for char in encrypted_message])

def brute_force(encrypted_message, e, n):
    start_time = time.perf_counter() 
    d = 2
    attempts = 0
    decrypted = False

    while not decrypted:
        if (e * d) % euler_phi == 1 and d != e:  # Check if e*d is congruent to 1 mod euler_phi and d is not equal to e
            decrypted = True
        else:
            d += 1
            attempts += 1
        if d >= 2**16:
            break
    end_time = time.perf_counter()  
    runtime = (end_time - start_time) * 1000  
    return d, runtime, attempts

def main():
    p = int(input("Enter the prime number (p): "))
    q = int(input("Enter the prime number (q): "))
    e = int(input("Enter the public exponent (e): "))
    n = p * q
    euler_phi = (p - 1) * (q - 1)

    message = input("Enter the message to encrypt: ")
    encrypted_message = encrypt(message, e, n)

    d, runtime, attempts = brute_force(encrypted_message, e, n)
    decrypted_message = decrypt(encrypted_message, d, n)
    
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")
    print(f"Private exponent found: {d}")
    print(f"Runtime: {runtime:.4f} milliseconds")
    print(f"Attempts: {attempts}")

if __name__ == "__main__":
    main()
