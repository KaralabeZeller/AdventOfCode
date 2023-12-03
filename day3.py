import re
from functools import reduce

class NumberInfo:
    def __init__(self, number, start_index, end_index, row_index):
        self.number = number
        self.start_index = start_index
        self.end_index = end_index
        self.row_index = row_index

class SymbolInfo:
    def __init__(self, symbol, col_index, row_index):
        self.symbol = symbol
        self.col_index = col_index
        self.row_index = row_index

def extract_numbers(text):
    matrix = []
    numbers = {}
    symbols = {}

    rows = text.strip().split('\n')
    for row_idx, row in enumerate(rows):
        matrix.append(list(row))
        symbols[row_idx] = []

    for row_idx, row in enumerate(matrix):
        number_start = None
        row_numbers = []

        for col_idx, char in enumerate(row):
            if char.isdigit():
                if number_start is None:
                    number_start = col_idx
            else:
                if number_start is not None:
                    number = int(''.join(row[number_start:col_idx]))
                    row_numbers.append(NumberInfo(number, number_start, col_idx - 1, row_idx))
                    number_start = None

            if not char.isdigit() and char != '.':
                    symbols[row_idx].append(SymbolInfo(char, col_idx, row_idx))

        if number_start is not None:
            number = int(''.join(row[number_start:]))
            row_numbers.append(NumberInfo(number, number_start, len(row) - 1, row_idx))

        numbers[row_idx] = row_numbers

    return numbers, symbols

def find_numbers_for_symbol(symbol, row_idx, col_idx, numbers):
    matching_numbers = []

    for key in range(row_idx - 1, row_idx + 2):
        if key in numbers:
            row_numbers = numbers[key]

            for number in row_numbers:
                if key == row_idx:
                    if number.start_index < col_idx and number.end_index == col_idx-1:
                        matching_numbers.append(number)
                    if number.start_index == col_idx +1 and number.end_index > col_idx:
                        matching_numbers.append(number)
                else:
                    if number.start_index <= col_idx <= number.end_index:
                        matching_numbers.append(number)

                    if (number.end_index == col_idx - 1 or number.end_index == col_idx):
                        matching_numbers.append(number)
                    if (number.start_index == col_idx or number.start_index == col_idx + 1):
                        matching_numbers.append(number)

    return matching_numbers

with open('input.txt', 'r') as file:
    input_text = file.read()

numbers, symbols = extract_numbers(input_text)

unique_numbers_per_row = {id: set() for id in range(140)}
sum_gear_ratio = 0

for row_idx, row_symbols in symbols.items():
    for symbol in row_symbols:
        matching_numbers = find_numbers_for_symbol(symbol.symbol, symbol.row_index, symbol.col_index, numbers)
        my_neighbors = set()

        for number in matching_numbers:
            unique_numbers_per_row[number.row_index].add(number)
            if symbol.symbol == '*':
                my_neighbors.add(number)

        if len(my_neighbors) == 2:
            sum_gear_ratio += reduce(lambda x, y: x.number * y.number, my_neighbors)

print("SUM gear ratio: ", sum_gear_ratio)
