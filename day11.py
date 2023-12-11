import os
import sys

def read_input_file():
    with open('input.txt', 'r') as file:
        text = file.read().strip()
        lines = text.split("\n")
    return lines

def find_empty_rows_and_columns(lines):
    empty_rows = set(range(len(lines)))
    empty_columns = set(range(len(lines[0])))

    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == "#":
                empty_columns.discard(x)
                empty_rows.discard(y)

    return empty_rows, empty_columns

def calculate_galaxies(lines, empty_rows, empty_columns):
    galaxies = []
    current_additional_y = 0

    for y, row in enumerate(lines):
        if y in empty_rows:
            current_additional_y += 1
            continue
        current_additional_x = 0

        for x, cell in enumerate(row):
            if x in empty_columns:
                current_additional_x += 1
                continue
            if cell == "#":
                galaxies.append((x + current_additional_x * (1000000-1), y + current_additional_y * (1000000-1)))

    return galaxies

def calculate_sum_distances(galaxies):
    sum_distances = 0

    for i in range(len(galaxies)-1):
        for j in range(i+1, len(galaxies)):
            x, y = galaxies[i]
            x2, y2 = galaxies[j]
            sum_distances += abs(x2-x) + abs(y2-y)

    return sum_distances

lines = read_input_file()
empty_rows, empty_columns = find_empty_rows_and_columns(lines)
galaxies = calculate_galaxies(lines, empty_rows, empty_columns)
sum_distances = calculate_sum_distances(galaxies)

print("SUM: ", sum_distances)
