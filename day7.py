with open('input.txt', 'r') as file:
    hands = [(line.split(' ')[0], int(line.split(' ')[1])) for line in file.read().strip().split('\n')]

card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def is_higher(a, b, jokers):
    for i in range(5):
        card_a, card_b = a[i], b[i]
        if card_values[card_a] > card_values[card_b]:
            return True
        elif card_values[card_a] < card_values[card_b]:
            return False

def calculate_type(hand, jokers):
    card_counts = {}
    joker_count = 0
    
    if jokers:
        joker_count = hand.count('J')
    for card in hand:
        card_counts[card] = hand.count(card)
    
    if jokers and joker_count < 5:
        card_counts.pop('J', None)
    elif jokers and joker_count == 5:
        card_counts['J'] = 0
    
    for card in card_counts:
        if card_counts[card] == max(card_counts.values()):
            card_counts[card] = card_counts[card] + joker_count
    
    if max(card_counts.values()) == 5:
        return 7
    elif max(card_counts.values()) == 4:
        return 6
    elif 3 in card_counts.values() and 2 in card_counts.values():
        return 5
    elif max(card_counts.values()) == 3:
        return 4
    else:
        pair_sum = 0
        
        for card in card_counts:
            pair_sum = pair_sum + card_counts[card] if card_counts[card] == 2 else pair_sum
        if pair_sum == 4:
            return 3
        elif pair_sum == 2:
            return 2
        else:
            return 1

def is_lower(a, b, joker):
    if calculate_type(a, joker) < calculate_type(b, joker):
        return True
    elif calculate_type(a, joker) == calculate_type(b, joker):
        if not is_higher(a, b, joker):
            return True
    return False

def calculate_score(J):
    if J:
        card_values['J'] = 1
    for i in range(1, len(hands)):
        current_hand, current_value = hands[i]
        j = i - 1
        previous_hand, previous_value = hands[j]
        while j >= 0 and is_lower(current_hand, previous_hand, J):
            hands[j + 1] = hands[j]
            j -= 1
            previous_hand, previous_value = hands[j]
        hands[j + 1] = (current_hand, current_value)
    
    score = 0
    for i, hand in enumerate(hands):
        score += (i + 1) * hand[1]
    
    return score

print('Without Jokers')
print(calculate_score(False))
print('With Jokers')
print(calculate_score(True))
