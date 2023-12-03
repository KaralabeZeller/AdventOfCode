from collections import defaultdict
import re

max_red = 12
max_green = 13
max_blue = 14

power_of_minimums = 0

def read_file(file_path):
    global power_of_minimums 
    with open(file_path, 'r') as file:
        lines = file.readlines()
        games = defaultdict(list)
        for line in lines:
            game_id, rounds = line.split(":")
            game_id = re.search(r'\d+', game_id).group()
            rounds = rounds.strip().split(";")
            
            reds = []
            greens = []
            blues = []
            
            for round_data in rounds:
                round_data = round_data.strip()
                red_match = re.search(r'(\d+)\s*red', round_data)
                green_match = re.search(r'(\d+)\s*green', round_data)
                blue_match = re.search(r'(\d+)\s*blue', round_data)
                
                red = int(red_match.group(1)) if red_match else 0
                green = int(green_match.group(1)) if green_match else 0
                blue = int(blue_match.group(1)) if blue_match else 0
                
                reds.append(red)
                greens.append(green)
                blues.append(blue)
                               
            current_power = max(reds) * max(greens) * max(blues)
            power_of_minimums = power_of_minimums + current_power
    return games

file_path = "input.txt"
games = read_file(file_path)
    
print(power_of_minimums)
