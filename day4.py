import re

instances_total = {}
sum_instances = 0

def add_or_init_instance(key, num):
    instances_total[key] = instances_total.get(key, 0) + num
    
with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines[::]:
    parts = line.strip().split(":")
    card_id = re.search(r'\d+', parts[0]).group()
    groups = parts[1].strip().split("|")
    group1 = list(map(int, groups[0].strip().split()))
    group2 = list(map(int, groups[1].strip().split()))

    matches = [number for number in group1 if number in group2]
    match_length = len(matches)
    
    card_id_num = int(card_id)

    add_or_init_instance(card_id_num, 1)  
    
    for num in range(card_id_num + 1, card_id_num + match_length + 1):
        add_or_init_instance(num, instances_total[card_id_num])

    sum_instances += instances_total[card_id_num]

print("SUM: ", sum_instances)
