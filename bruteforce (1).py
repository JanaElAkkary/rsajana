import time
from generatingnumbers import is_prime, generate_prime, extended_gcd, generate_keys

def encrypt(message, e, n):
    #    """
    # Encrypt a message using RSA encryption.
    
    # Parameters:
    # message (str): The message to encrypt
    # e (int): The public exponent
    # n (int): The modulus
    
    # Returns:
    # list: List of encrypted integers representing the message
    # """
    return [pow(ord(char), e, n) for char in message]

def decrypt(encrypted_message, d, n):
    #   """
    # Decrypt a message using RSA decryption.
    
    # Parameters:
    # encrypted_message (list): List of encrypted integers
    # d (int): The private exponent
    # n (int): The modulus
    
    # Returns:
    # str: Decrypted message
    # """
    return ''.join([chr(pow(char, d, n) % 65536) for char in encrypted_message])

def brute_force(encrypted_message, e, n):
    #   """
    # Perform brute-force attack to find the private exponent d.
    
    # Parameters:
    # encrypted_message (list): List of encrypted integers
    # e (int): The public exponent
    # n (int): The modulus
    
    # Returns:
    # tuple: A tuple containing the found private exponent d and the runtime in milliseconds
    
    start_time = time.perf_counter() 
    d = 2  # Start with the smallest possible prime exponent
    
    decrypted = False
    while not decrypted:
        if pow(e, d, n) == 1:  # Check if end is congruent to 1 modulos phi(n)
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
