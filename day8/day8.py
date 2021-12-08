#!/usr/bin/env python3

input_data = []
with open('input.txt', 'r', encoding="utf-8") as f:
    input_data = f.read().splitlines()

series = []
output = []
for line in input_data:
    pattern, out = line.split(" | ")
    series.append(pattern.split(" "))
    output.append(out.split(" "))

# Count 1,4,7,8 digits (respectively 2,4,3,7 length strings)
count = 0
for out in output:
    for digit in out:
        if len(digit) >= 2 and len(digit) <= 4:
            count += 1
        elif len(digit) == 7:
            count += 1
print(f"Count of 1,4,7,8: {count}")


# Part 2
def find_code(code_series):
    """
    From a code series return a dict
    each number (0 to 8) is a key with a corresponding set encoding the number.
    code_series: must be a series of set representing the random encoding.
    """
    the_code = {0: set(), 1: set(), 2: set(), 3: set(),
                4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
    # Find the easy numbers that have a unique length
    # And classify the 5 segments and 6 segments
    five_segs = []
    six_segs = []
    for code in code_series:
        if len(code) == 2:
            the_code[1] = code
        if len(code) == 3:
            the_code[7] = code
        if len(code) == 4:
            the_code[4] = code
        if len(code) == 5:
            five_segs.append(code)
        if len(code) == 6:
            six_segs.append(code)
        if len(code) == 7:
            the_code[8] = code

    # Find 6
    # 6 is the only 6 segments not superset of 1
    for code in six_segs:
        if not code.issuperset(the_code[1]):
            the_code[6] = code
            six_segs.remove(code)
    # Find 5
    # 5 is the only 5 segments subset of 6
    for code in five_segs:
        if code.issubset(the_code[6]):
            the_code[5] = code
            five_segs.remove(code)
    # Find 9
    # 9 is the only 6 segments superset of 5
    for code in six_segs:
        if code.issuperset(the_code[5]):
            the_code[9] = code
            six_segs.remove(code)
    # Find 0
    # 0 is the last 6 segments
    the_code[0] = six_segs.pop()
    # Find 3
    # 3 is the only 5 segments subset of 9
    for code in five_segs:
        if code.issubset(the_code[9]):
            the_code[3] = code
            five_segs.remove(code)
    # Find 2
    # 2 is the last 5 segments
    the_code[2] = five_segs.pop()

    # Hooray
    return the_code


def decode_value(a_code, decoder):
    """
    Decode a code using the decoder dict
    and return the corresponding integer value
    """
    result = []
    for a_digit in a_code:
        for digit, a_decode in decoder.items():
            if a_decode == a_digit:
                result.append(digit)
    number = int(''.join(map(str, result)))
    return number

sum = 0
for line in input_data:
    pattern, out = line.split(" | ")
    series = [set(x) for x in pattern.split(" ")]
    output = [set(x) for x in out.split(" ")]
    code = find_code(series)
    sum += decode_value(output, code)

print(f"The sum of all the output is {sum}.")
