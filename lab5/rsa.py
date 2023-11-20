from sympy import randprime, mod_inverse
from math import gcd


def generate_primes(bits):
    p = randprime(2**(bits//2), 2**(bits//2 + 1))
    q = randprime(2**(bits//2), 2**(bits//2 + 1))
    return p, q


def generate_public_exponent(phi):
    e = randprime(10**4, 10**5)
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1

    return e


def generate_private_key(public_exponent, phi):
    return mod_inverse(public_exponent, phi)


def encrypt_message(message: str, public_key) -> int:
    hex_message = message.encode('utf-8').hex()
    int_message = int(hex_message, 16)
    return pow(int_message, public_key[1], public_key[0])


def decrypt_message(enc_message: int, private_key, public_key) -> str:
    dec_int_message = pow(enc_message, private_key, public_key[0])
    return bytes.fromhex(hex(dec_int_message)[2:]).decode('utf-8')


def main():
    bits = 2048
    p, q = generate_primes(bits)
    phi = (p - 1) * (q - 1)
    public_key = (p * q, generate_public_exponent(phi))
    private_key = generate_private_key(public_key[1], phi)

    print("Prime 1:", p)
    print("Prime 2:", q)
    print("n:", public_key[0])
    print("Euler totient function φ(n) = (p − 1)(q − 1):", phi)
    print("Public Key (n, e):", public_key)
    print("Private Key (n, d):", (public_key[0], private_key))

    message = "Maria Lesenco"
    encrypted_message = encrypt_message(message, public_key)
    decrypted_message = decrypt_message(encrypted_message, private_key, public_key)

    print(f"\nOriginal Message: {message}")
    print(f"Encrypted Message (ciphertext): {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
