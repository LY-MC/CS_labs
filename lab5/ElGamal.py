from random import randint
from sympy import mod_inverse


def generate_keys(p, g):
    private_a = randint(2, p - 2)
    public_a = pow(g, private_a, p)
    return public_a, private_a


def elgamal_encrypt(message, p, g, public_key):
    k = randint(1, p - 2)
    hex_message = message.encode('utf-8').hex()
    int_message = int(hex_message, 16)
    C1 = pow(g, k, p)
    C2 = (int_message * pow(public_key, k, p)) % p
    return C1, C2


def elgamal_decrypt(C1, C2, p, private_key):
    s = pow(C1, private_key, p)
    s_inv = mod_inverse(s, p)
    dec_int_message = (C2 * s_inv) % p
    return bytes.fromhex(hex(dec_int_message)[2:]).decode('utf-8')


def main():
    p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844903661304976978128542959586595975670512838521327844685229255045682728791137200989318739591433741758378268000278034973198552060607533234122603254684088121003994966956119696956248629032338072839127039
    g = 2

    public_a, private_a = generate_keys(p, g)

    message = "Maria Lesenco"
    C1, C2 = elgamal_encrypt(message, p, g, public_a)
    decrypted_message = elgamal_decrypt(C1, C2, p, private_a)

    print(f"Original Message: {message}")
    print("Public key:", public_a)
    print("Private key:", private_a)
    print(f"Encrypted Message (C1, C2): ({C1}, {C2})")
    print(f"Decrypted Message: {decrypted_message}")


if __name__ == "__main__":
    main()
