import hashlib
from random import randint
from math import gcd
from sympy import mod_inverse


def hash_message(message):
    hash_object = hashlib.sha3_224()
    hash_object.update(message.encode())
    hashed_message = int.from_bytes(hash_object.digest(), byteorder='big')
    hash_size = 224
    hashed_message = hashed_message << (hash_size - hashed_message.bit_length())
    return hashed_message


def generate_key_pair(p, g):
    private_key = randint(1, p - 2)
    public_key = pow(g, private_key, p)
    return private_key, public_key


def sign_message(private_key, hashed_message, p, g):
    while True:
        k = randint(1, p - 2)
        gcd_value = gcd(k, p - 1)

        if gcd_value == 1:
            r = pow(g, k, p)
            s = (mod_inverse(k, p - 1) * (hashed_message - private_key * r)) % (p - 1)
            signature = (r, s)
            return signature


def verify_signature(public_key, received_signature, hashed_message, p, g):
    r_received, s_received = received_signature
    v1 = (pow(public_key, r_received, p) * pow(r_received, s_received, p)) % p
    v2 = pow(g, hashed_message, p)
    return v1 == v2


msg = "england, too, had its black chamber. it began with the cryptanalytic endeavors of john wallis, the greatest english mathematician before newton. after his death, it descended through his grandson to reach, on may 14, 1716, edward willes, a 22-year-old minister at oriel college, oxford. willes embarked at once upon a career unique in the annals of cryptology and the church. he not only managed to reconcile his religious calling with an activity once condemned by churchly authorities, but also went on to become the only man in history to use cryptanalytic talents to procure ecclesiastical rewards. within two years, he had been named rector of barton, bedfordshire, for solving more than 300 pages of cipher that exposed sweden's attempt to foment an uprising in england. he virtually guaranteed his future when he testified before the house of lords in 1723. here, francis atterbury, bishop of rochester, was being tried by his peers for attempting to set a pretender on the english throne. the pretender's cause exhorted the allegiance of many in england, and the nation's attention focused on atterbury's trial. most of the facts about the alleged conspiracy had come from his intercepted correspondence, and the most inculpatory evidence had been extracted from the portions in cipher by willes and by anthony corbiere, a former foreign service official in his mid-thirties who had also been appointed a decypherer in 1719. the lords 'thought it proper to call the decypherers before them, in order to their being satisfied of the truth of the ,decyphering.' to demonstrate this, willes and corbiere deposed, ,that several letters, written in this cypher, had been decyphered by them separately, one being many miles distant in the country, and the other in town; and yet their decyphering agreed;that facts, unknown to them and the government at the time of their decyphering, had been verified in every circumstance by subsequent discoveries; as, that a supplement of this cypher, having been found among dennis kelly's papers the latter end of july, agreed with the key they had formed of that cypher the april before; that the decyphering of the letters signed jones lllington and 1378, being afterwards applied by them to others written in the same cypher, did immediately make pertinent sense, and such as had an evident connexion and coherence with the parts of those letters that were out of cypher, though the words in cypher were repeated in different paragraphs, and differently combined. the two decypherers appeared before the lords on several occasions to swear to their solutions. attenbury twice objected and was twice overruled. but on may 7, as willes was testifying to the cryptanalysis of the three most incriminatory letters of all, and the bishop felt the noose tightening around him, he persisted in questioning willes on the validity of the reading though the house had supported willes' refusal to answer. he raised such a commotion that he and his counsel were ordered to withdraw, and the lords voted upon the proposition, \"that it is the opinion of this house that it is not consistent with the public safety, to ask the decypherers any questions, which may tend to discover the art or mystery of decyphering.\" it was resolved in the affirmative, the solutions were accepted, and atterbury, largely on this evidence, was found guilty, deprived of office, and banished from the realm."

hashed_message = hash_message(msg)
print("Hashed message:", hashed_message)

p = 32317006071311007300153513477825163362488057133489075174588434139269806834136210002792056362640164685458556357935330816928829023080573472625273554742461245741026202527916572972862706300325263428213145766931414223654220941111348629991657478268034230553086349050635557712219187890332729569696129743856241741236237225197346402691855797767976823014625397933058015226858730761197532436467475855460715043896844940366130497697812854295958659597567051283852132784468522925504568272879113720098931873959143374175837826000278034973198552060607533234122603254684088120031105907484281003994966956119696956248629032338072839127039
g = 2

private_key, public_key = generate_key_pair(p, g)
print("Private Key:", private_key)
print("Public Key:", public_key)

signature = sign_message(private_key, hashed_message, p, g)
print("Signature:", signature)

verification = verify_signature(public_key, signature, hashed_message, p, g)
if verification:
    print("Signature is valid.")
else:
    print("Signature is invalid.")
