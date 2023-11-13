from random import randint
from sympy import mod_inverse


def generate_keys(p, g):
    private_b = randint(2, p - 2)
    public_b = pow(g, private_b, p)
    private_a = randint(2, p - 2)
    public_a = pow(g, private_a, p)
    return public_a, private_a, public_b, private_b


def encrypt_message(message: str, public_b, private_a, p) -> int:
    hex_message = message.encode('utf-8').hex()
    int_message = int(hex_message, 16)
    masking_key = pow(public_b, private_a, p)
    return (int_message * masking_key) % p


def decrypt_message(enc_message: int, public_a, private_b, p) -> str:
    masking_key = pow(public_a, private_b, p)
    masking_inverse = mod_inverse(masking_key, p)
    dec_int_message = (enc_message * masking_inverse) % p
    return bytes.fromhex(hex(dec_int_message)[2:]).decode('utf-8')

def main():
    p = 3231700607131100730015351347782516336248805713348907517458843413926980683413621000279205636264016468545855635793533081692882902308057347262527355474246124574102620252791657297286270630032526342821314576693141422365422094111134862999165747826803423055308634905063555771221918789033272956969612974385624174123623722519734640269185579776797682301462539793305801522685873076119753243646747585546071504389684490366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
    g = 2

    public_a, private_a, public_b, private_b = generate_keys(p, g)

    message = "Maria Lesenco"
    encrypted_message = encrypt_message(message, public_b, private_a, p)
    decrypted_message = decrypt_message(encrypted_message, public_a, private_b, p)

    print(f"Original Message: {message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
