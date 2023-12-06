with open('input.txt', 'r') as file:
    lines = file.readlines()
    time = int(''.join(lines[0].split(':')[1].split()))
    distance = int(''.join(lines[1].split(':')[1].split()))

sum_bests = sum(1 for second in range(1, time // 2) if second * (time - second) > distance)

final_sum = sum_bests * 2 + 1 if time % 2 == 0 else (sum_bests + 1) * 2

print("SUM:", final_sum)
