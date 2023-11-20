from random import randint
import hashlib


def generate_diffie_hellman_parameters():
    p = 3231700607131100730015351347782516336248805713348907517458843413926980683413621000279205636264016468545855635793533081692882902308057347262527355474246124574102620252791657297286270630032526342821314576693141422365422094111134862999165747826803423055308634905063555771221918789033272956969612974385624174123623722519734640269185579776797682301462539793305801522685873076119753243646747585546071504389684494036610497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
    g = 2
    private_a = randint(1, p - 1)
    private_b = randint(1, p - 1)
    public_a = pow(g, private_a, p)
    public_b = pow(g, private_b, p)
    common_secret_a = pow(public_b, private_a, p)
    common_secret_b = pow(public_a, private_b, p)

    return p, g, private_a, public_a, private_b, public_b, common_secret_a, common_secret_b


def derive_key(common_secret, salt):
    common_secret_bytes = common_secret.to_bytes((common_secret.bit_length() + 7) // 8, byteorder='big')
    key = hashlib.sha256(common_secret_bytes + salt).digest()
    return int.from_bytes(key, byteorder='big')


def xor_encrypt(message, key):
    key_bytes = key.to_bytes(32, byteorder='big')
    message_bytes = message.encode('utf-8')
    encrypted_blocks = [message_bytes[i] ^ key_bytes[i % 32] for i in range(len(message_bytes))]
    return encrypted_blocks


def xor_decrypt(encrypted_blocks, key):
    key_bytes = key.to_bytes(32, byteorder='big')
    decrypted_message = bytes([block ^ key_bytes[i % 32] for i, block in enumerate(encrypted_blocks)])
    return decrypted_message.decode('utf-8')


def main():
    p, g, private_a, public_a, private_b, public_b, common_secret_a, common_secret_b = generate_diffie_hellman_parameters()

    salt_a = b"AliceSalt"
    salt_b = b"BobSalt"

    key_a = derive_key(common_secret_a, salt_a)
    key_b = derive_key(common_secret_b, salt_b)

    message = "Hello, this is a secret message!"

    ciphertext_a = xor_encrypt(message, key_a)
    decrypted_message_a = xor_decrypt(ciphertext_a, key_a)

    ciphertext_b = xor_encrypt(message, key_b)
    decrypted_message_b = xor_decrypt(ciphertext_b, key_b)

    print("Alice Private Key:", private_a)
    print("Bob Private Key:", private_b)
    print("\nAlice Public Key:", public_a)
    print("Bob Public Key:", public_b)
    print("\nShared Secret Key (Alice):", common_secret_a)
    print("Shared Secret Key (Bob):", common_secret_b)

    print("\nOriginal Message:", message)
    print("Alice:")
    print("  Ciphertext:", ciphertext_a)
    print("  Decrypted Message:", decrypted_message_a)
    print("Bob:")
    print("  Ciphertext:", ciphertext_b)
    print("  Decrypted Message:", decrypted_message_b)

if __name__ == "__main__":
    main()
