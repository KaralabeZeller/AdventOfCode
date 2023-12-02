import re

replacements = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "th3ree",
    "four": "f4our",
    "five": "f5ive",
    "six": "s6ix",
    "seven": "se7ven",
    "eight": "ei8ght",
    "nine": "ni9ne"
}

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        numbers = []
        for line in lines:
            for key, value in replacements.items():
                line = line.replace(key, value)
            number = extract_number(line)
            if number:
                numbers.append(number)
    return numbers

def extract_number(line):
    number = re.sub(r'\D', '', line)
    reduced_number = ""
    if len(number) == 1:
        reduced_number = number + number
    elif len(number) <=2:
        reduced_number = number
    else:
        reduced_number = number[0] + number[-1]
    print(reduced_number)
    return reduced_number

def calculate_sum(numbers):
    return sum(map(int, numbers))

file_path = 'input.txt'
numbers = read_file(file_path)
total_sum = calculate_sum(numbers)
print(total_sum)
