#!/usr/bin/env python3
import re

input_data = []
with open('input.txt', 'r', encoding="utf-8") as f:
    input_data = f.read().splitlines()

max_grid_column = 0
max_grid_row = 0
for line in input_data:
    pattern = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    # (x1, y1) -> (x2, y2)
    # x1 & x2: column coordinates
    # y1 & y2: line coordinates
    max_grid_column = max(int(pattern[1]), int(pattern[3]), max_grid_column)
    max_grid_row = max(int(pattern[2]), int(pattern[4]), max_grid_row)

max_grid_column += 1
max_grid_row += 1
print(f"Grid size: {max_grid_column}x{max_grid_row}")
grid = [[0] * (max_grid_column) for _ in range(max_grid_row)]


def line_array(point_a, point_b):
    """
    From two points return an array that represens a line between these
    two points
    points must be tuples: (x1, y1) and (x2, y2)
    """
    x1, y1 = point_a
    x2, y2 = point_b
    x_array = list(range(x1, x2 + 1) if x1 < x2 else reversed(range(x2, x1 + 1)))
    y_array = list(range(y1, y2 + 1) if y1 < y2 else reversed(range(y2, y1 + 1)))
    # Extend horizontal and vertical lines
    if len(x_array) == 1:
        x_array *= len(y_array)
    if len(y_array) == 1:
        y_array *= len(x_array)
    final_array = list(zip(x_array, y_array))
    return final_array


for line in input_data:
    pattern = re.search(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    coord_a = (int(pattern[1]), int(pattern[2]))
    coord_b = (int(pattern[3]), int(pattern[4]))
    # Uncomment for part 1
    # if coord_a[0] != coord_b[0] and coord_a[1] != coord_b[1]:
    #     continue
    a_line = line_array(coord_a, coord_b)
    for column, line in a_line:
        grid[line][column] += 1

count = 0
for line in grid:
    for cell in line:
        if cell > 1:
            count += 1
print(count)
