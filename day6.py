import math

# Bruteforce solution
with open('input.txt', 'r') as file:
    lines = file.readlines()
    time = int(''.join(lines[0].split(':')[1].split()))
    distance = int(''.join(lines[1].split(':')[1].split()))

sum_bests = sum(1 for second in range(1, time // 2) if second * (time - second) > distance)

final_sum = sum_bests * 2 + 1 if time % 2 == 0 else (sum_bests + 1) * 2

print("SUM:", final_sum)

# 'math' solution
x1 = (-time + math.sqrt(time ** 2 - 4 * (-1) * -distance)) / (2 * (-1))
x2 = (-time - math.sqrt(time ** 2 - 4 * (-1) * -distance)) / (2 * (-1))

final_sum = math.ceil(x2) - math.ceil(x1)

print("SUM:", final_sum)
