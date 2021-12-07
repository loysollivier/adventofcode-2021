#!/usr/bin/env python3

input_data = []
with open('input.txt', 'r', encoding="utf-8") as f:
    input_data = f.read().splitlines()

fish_school = [int(number) for number in input_data.pop().split(',')]

sorted_school = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
for fish in fish_school:
    sorted_school[fish] += 1
print(f"Fishs in order: {sorted_school}")

number_days = 256
for day in range(number_days):
    # The solution is dependent on the dict order. Not very nice but OK...
    new_school = {8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0, 1: 0, 0: 0}
    for fish in sorted_school:
        next_fish = fish - 1
        if next_fish < 0:
            # Spawn new fish and reset the parents
            new_school[6] += sorted_school[0]
            new_school[8] = sorted_school[0]
        else:
            new_school[next_fish] = sorted_school[fish]
    sorted_school = new_school

print(sorted_school)
number_fish = 0
for value in sorted_school.values():
    number_fish += value
print(f"Day: {number_days} - # fish {number_fish}")
