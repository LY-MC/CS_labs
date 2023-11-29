import hashlib
from sympy import randprime
from math import gcd


def generate_primes(bits):
    p = randprime(2 ** (bits // 2), 2 ** (bits // 2 + 1))
    q = randprime(2 ** (bits // 2), 2 ** (bits // 2 + 1))
    return p, q


def generate_public_exponent(phi):
    e = randprime(10 ** 4, 10 ** 5)
    while e < phi:
        if gcd(e, phi) == 1:
            break
        else:
            e += 1

    return e


msg = "england, too, had its black chamber. it began with the cryptanalytic endeavors of john wallis, the greatest english mathematician before newton. after his death, it descended through his grandson to reach, on may 14, 1716, edward willes, a 22-year-old minister at oriel college, oxford. willes embarked at once upon a career unique in the annals of cryptology and the church. he not only managed to reconcile his religious calling with an activity once condemned by churchly authorities, but also went on to become the only man in history to use cryptanalytic talents to procure ecclesiastical rewards. within two years, he had been named rector of barton, bedfordshire, for solving more than 300 pages of cipher that exposed sweden's attempt to foment an uprising in england. he virtually guaranteed his future when he testified before the house of lords in 1723. here, francis atterbury, bishop of rochester, was being tried by his peers for attempting to set a pretender on the english throne. the pretender's cause exhorted the allegiance of many in england, and the nation's attention focused on atterbury's trial. most of the facts about the alleged conspiracy had come from his intercepted correspondence, and the most inculpatory evidence had been extracted from the portions in cipher by willes and by anthony corbiere, a former foreign service official in his mid-thirties who had also been appointed a decypherer in 1719. the lords 'thought it proper to call the decypherers before them, in order to their being satisfied of the truth of the ,decyphering.' to demonstrate this, willes and corbiere deposed, ,that several letters, written in this cypher, had been decyphered by them separately, one being many miles distant in the country, and the other in town; and yet their decyphering agreed;that facts, unknown to them and the government at the time of their decyphering, had been verified in every circumstance by subsequent discoveries; as, that a supplement of this cypher, having been found among dennis kelly's papers the latter end of july, agreed with the key they had formed of that cypher the april before; that the decyphering of the letters signed jones lllington and 1378, being afterwards applied by them to others written in the same cypher, did immediately make pertinent sense, and such as had an evident connexion and coherence with the parts of those letters that were out of cypher, though the words in cypher were repeated in different paragraphs, and differently combined. the two decypherers appeared before the lords on several occasions to swear to their solutions. attenbury twice objected and was twice overruled. but on may 7, as willes was testifying to the cryptanalysis of the three most incriminatory letters of all, and the bishop felt the noose tightening around him, he persisted in questioning willes on the validity of the reading though the house had supported willes' refusal to answer. he raised such a commotion that he and his counsel were ordered to withdraw, and the lords voted upon the proposition, \"that it is the opinion of this house that it is not consistent with the public safety, to ask the decypherers any questions, which may tend to discover the art or mystery of decyphering.\" it was resolved in the affirmative, the solutions were accepted, and atterbury, largely on this evidence, was found guilty, deprived of office, and banished from the realm."
print("Message:", msg)

hash_object = hashlib.sha3_256()
hash_object.update(msg.encode())
hashed_message = int.from_bytes(hash_object.digest(), byteorder='big')

hash_size = 256
hashed_message = hashed_message << (hash_size - hashed_message.bit_length())
print("Hashed message:", hashed_message)
print("Hashed message in bits:", hashed_message.bit_length())

bits = 1554
p, q = generate_primes(bits)

n = p * q
print(n)
phi = (p - 1) * (q - 1)

e = generate_public_exponent(phi)
print("e:", e)

d = pow(e, -1, phi)
print("d:", d)

signature = pow(hashed_message, d, n)
print("Signature:", signature)

verification = pow(signature, e, n)

if verification == hashed_message:
    print("Signature is valid.")
else:
    print("Signature is invalid.")
