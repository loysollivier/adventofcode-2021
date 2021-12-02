#!/usr/bin/env python3

# Part 1

input_data = []
with open('day1_input.txt', 'r') as f:
    input_data = f.read().splitlines()
    input_data = [ int(x) for x in input_data ]

increases = 0
for n_1, n in zip(input_data, input_data[1:]):
    if n > n_1:
        increases += 1

print(f"There was {increases} measurements larger than the previous one.")

# Part 2

increases = 0
window_1 = -1
for n0, n1, n2 in zip(input_data, input_data[1:], input_data[2:]):
    window = n0 + n1 + n2
    if window_1 == -1:
        window_1 = window
        continue
    if window > window_1:
        increases += 1
    window_1 = window

print(f"There was {increases} sums larger than the previous one.")
