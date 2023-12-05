import joblib

with open("input.txt", "r") as file:
    lines = file.readlines()

seeds = list(map(int, lines[0].strip().split(":")[1].split()))
current_category = ""
category_maps = []
category_map = {}

for line in lines[2:]:
    line = line.strip()
    if ":" in line:
        current_category = line.strip().split(" map:")[0]
        category_map[current_category] = []
    elif len(line) == 0:
        category_maps.append(category_map[current_category])
    else:
        category_map[current_category].append(list(map(int, line.split())))

print("Seeds:", seeds)

def check_interval(seed, iteration):
    return_seed = seed
    return_iteration = iteration + 1

    current_list = category_maps[iteration]
    for item in current_list:
        destination_start = item[0]
        source_start = item[1]
        range_value = item[2]

        if source_start <= seed <= source_start + range_value:
            diff = source_start + range_value - seed
            return_seed = destination_start + range_value - diff
            break

    if return_iteration >= len(category_maps) :
        return return_seed
    else:
        return check_interval(return_seed, return_iteration)

def seed_processor(from_value, to_value):
    min_location = 9999999999

    for seed in range(from_value, to_value):
        result = check_interval(seed, 0)
        if  result < min_location:
            min_location = result

    return min_location


seed_pairs = [seeds[i:i+2] for i in range(0, len(seeds), 2)]
allJobs = []

for seed_pair in seed_pairs:
    print("Pair:", seed_pair)
    from_value = seed_pair[0]
    to_value = from_value + seed_pair[1]
    allJobs.append(joblib.delayed(seed_processor)(from_value, to_value))

min_locations = joblib.Parallel(n_jobs=joblib.cpu_count(), verbose=10)(allJobs)
print("Min location:", min(min_locations))
