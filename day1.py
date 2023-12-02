import re

number_mappings = {
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
    numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            line = ' '.join([number_mappings.get(word, word) for word in line.split()])
            number = extract_number(line)
            if number:
                numbers.append(number)
    return numbers

def extract_number(line):
    numbers = re.findall(r'\d+', line)
    reduced_number = ""
    if numbers:
        number = numbers[0]
        reduced_number = number[:1] + number[-1:]
    return reduced_number

def calculate_sum(numbers):
    return sum(map(int, numbers))

file_path = 'input.txt'
numbers = read_file(file_path)
total_sum = calculate_sum(numbers)
print(total_sum)
