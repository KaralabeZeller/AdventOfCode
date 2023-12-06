with open('input.txt', 'r') as file:
    lines = file.readlines()
    time_list = [int(''.join(lines[0].split(':')[1].split()))]
    distance_list = [int(''.join(lines[1].split(':')[1].split()))]
    
sum_bests = 0
time = time_list[0]
distance = distance_list[0]

for second in range(1, time):
    theoretical_best = second * (time - second)
    if(theoretical_best > distance):
        sum_bests += 1

print("SUM: ", sum_bests)
