#!/usr/bin/env python3


input_data = []
with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()

# Part 1
gamma = [0 for i in range(len(input_data[0]))]
for line in input_data:
    pos = 0
    for bit in line:
        if bit == "1":
            gamma[pos] += 1
        else:
            gamma[pos] -= 1
        pos += 1

# Reverse the binary value to go through it in the correct order
gamma.reverse()
gamma_val = 0
for pos, acc in enumerate(gamma):
    if acc > 0:
        gamma_val += 2**pos

epsilon_val = 0
for pos, acc in enumerate(gamma):
    if acc < 0:
        epsilon_val += 2**pos

print(gamma_val, epsilon_val)
print(gamma_val * epsilon_val)

# Part 2


def str_bin_to_dec(a_str):
    """
    A string that represents a binary number.
    Returns the value in decimal
    """
    dec_val = 0
    for pos, bit in enumerate(a_str):
        if bit == "1":
            dec_val += 2**(len(a_str) - pos - 1)
    return dec_val


def find_rating(reduced_list, mcb=True, position=0):
    """
    Reduced_list: the list to go through finding the most or least common bit
    mcb: if True look for most common bit else for least common bit
    returns the last value remaining (string)
    """
    bit_count = {0: 0, 1: 0}
    zero_list = []
    one_list = []
    if len(reduced_list) == 1:
        return reduced_list.pop()
    for line in reduced_list:
        if line[position] == "0":
            bit_count[0] += 1
            zero_list.append(line)
        else:
            bit_count[1] += 1
            one_list.append(line)
    position += 1
    if bit_count[0] > bit_count[1]:
        return find_rating(zero_list if mcb else one_list, mcb=mcb, position=position)
    elif bit_count[1] > bit_count[0]:
        return find_rating(one_list if mcb else zero_list, mcb=mcb, position=position)
    else:
        # Number of ones and zeros are equal
        return find_rating(one_list if mcb else zero_list, mcb=mcb, position=position)


oxygen = find_rating(reduced_list=input_data)
oxygen_dec = str_bin_to_dec(oxygen)

co2 = find_rating(reduced_list=input_data, mcb=False)
co2_dec = str_bin_to_dec(co2)

print(oxygen_dec, co2_dec)
print(oxygen_dec * co2_dec)
