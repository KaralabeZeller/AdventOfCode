import math

with open('input.txt', 'r') as file:
    lines = file.readlines()

directions = list(lines[0].strip())
nodes = {line.split("=")[0].strip(): line.split("=")[1].strip()[1:-1].split(", ") for line in lines[2:]}

def get_branch(key):
    counter = 0
    direction_pointer = -1
    while True:
        direction_pointer = (direction_pointer + 1) % len(directions)
        direction = directions[direction_pointer]
        counter += 1
        next_key = nodes[key][0] if direction == 'L' else nodes[key][1]
        if next_key.endswith("Z"):
            return counter
        key = next_key

counter_list = [get_branch(key) for key in nodes if key.endswith("A")]
lcm = math.lcm(*counter_list)

print("LKKT: ", lcm)
