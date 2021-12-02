#!/usr/bin/env python3

# Part 1

input_data = []
with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()
    input_data = [ tuple(x.split(' ')) for x in input_data ]
    input_data = [ (x,int(y)) for x,y in input_data ]

h_pos = 0
d_pos = 0

for control, units in input_data:
    if control == 'forward':
        h_pos += units
    if control == 'up':
        d_pos -= units
    if control == 'down':
        d_pos += units

print(h_pos, d_pos)
print(h_pos * d_pos)

# Part 2

h_pos = 0
d_pos = 0
aim = 0

for control, units in input_data:
    if control == 'forward':
        h_pos += units
        d_pos += aim * units
    if control == 'up':
        aim -= units
    if control == 'down':
        aim += units

print(h_pos, d_pos)
print(h_pos * d_pos)
