import re

data = {}

with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines[::]:
    parts = line.strip().split(":")
    card_id = re.search(r'\d+', parts[0]).group()
    groups = parts[1].strip().split("|")
    group1 = list(map(int, groups[0].strip().split()))
    group2 = list(map(int, groups[1].strip().split()))

    matches = []
    for number in group1:
        if number in group2:
            matches.append(number)

    data[card_id] = matches

match_lengths = {}

for card_id, matches in data.items():
    match_length = len(matches)
    match_lengths[card_id] = match_length

instances_total = {}

def add_or_init_instance(key):
    instances_total[key] = instances_total.get(key, 0) + 1
    
for card_id, length in match_lengths.items():
    card_id_num = int(card_id)

    add_or_init_instance(card_id_num)  
    
    for _ in range(instances_total[card_id_num]):
        for num in range(card_id_num + 1, card_id_num + length + 1):
            add_or_init_instance(num)

sum_instances = 0
for key, value in instances_total.items():
    sum_instances += value
    
print("SUM: ", sum_instances)
