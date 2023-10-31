pc1_key = int("11110000110011001010101011110101010101100110011110001111", 2)

# Split the key into C0 and D0
c0 = (pc1_key >> 28) & 0xFFFFFFF
d0 = pc1_key & 0xFFFFFFF

# Initialize C0 and D0
c_round, d_round = c0, d0


def next_round(c_current, d_current, round_number):
    # Define the number of left shifts for this round
    if round_number in [1, 2, 9, 16]:
        shift_count = 1
    else:
        shift_count = 2

    # Perform circular left shifts on C and D
    c_next = ((c_current << shift_count) | (c_current >> (28 - shift_count))) & 0xFFFFFFF
    d_next = ((d_current << shift_count) | (d_current >> (28 - shift_count))) & 0xFFFFFFF

    return c_next, d_next


for round_number in range(1, 17):
    print(f"Round {round_number}:")
    print(f"C{round_number}:", bin(c_round)[2:].zfill(28))
    print(f"D{round_number}:", bin(d_round)[2:].zfill(28))
    print()

    # Update c_round and d_round for the next round
    c_round, d_round = next_round(c_round, d_round, round_number)
