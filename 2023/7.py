import bisect
from collections import Counter

DAY = 7
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.read()

data = data.split("\n")

five = []
four = []
full = []
three = []
two = []
one = []
high = []

order = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def add_hands(hands_list: list, hand: str):
    bisect.insort(hands_list, hand, key=lambda x: tuple(order[char] for char in x))


total_hands = {}
for line in data:
    hand, bid = line.split(" ")
    total_hands[hand] = int(bid)
    # To find the type of hand
    hand_counter = Counter(hand)
    cards_combos = hand_counter.most_common()
    max_cards = cards_combos[0][1]
    if max_cards == 5:
        add_hands(five, hand)
    elif max_cards == 4:
        add_hands(four, hand)
    elif max_cards == 3 and len(cards_combos) == 2:
        add_hands(full, hand)
    elif max_cards == 3 and len(cards_combos) == 3:
        add_hands(three, hand)
    elif max_cards == 2 and len(cards_combos) == 3:
        add_hands(two, hand)
    elif max_cards == 2 and len(cards_combos) == 4:
        add_hands(one, hand)
    else:
        add_hands(high, hand)


result = 0
sorted_hands = high + one + two + three + full + four + five

n = 1
for hand in sorted_hands:
    result += total_hands[hand] * n
    n += 1

# Part 1
print(f"Part 1 Result = {result}")
# 248836197

# Part 2
# Joker Twist

five = []
four = []
full = []
three = []
two = []
one = []
high = []

order = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1,
}


def add_hands(hands_list: list, hand: str):
    bisect.insort(hands_list, hand, key=lambda x: tuple(order[char] for char in x))


total_hands = {}
for line in data:
    hand, bid = line.split(" ")
    total_hands[hand] = int(bid)

    hand_counter = Counter(hand)
    cards_combos = hand_counter.most_common()
    max_cards = cards_combos[0][1]
    jokers = hand_counter["J"]

    if max_cards == 5:
        add_hands(five, hand)
    elif max_cards == 4:
        if jokers == 1 or jokers == 4:
            add_hands(five, hand)
        else:
            add_hands(four, hand)

    elif max_cards == 3 and len(cards_combos) == 2:
        # Jokers can be either 2 or 3 in this case
        if jokers >= 2:
            add_hands(five, hand)
        else:
            add_hands(full, hand)

    elif max_cards == 3 and len(cards_combos) == 3:
        if jokers == 1 or jokers == 3:
            add_hands(four, hand)
        else:
            add_hands(three, hand)

    elif max_cards == 2 and len(cards_combos) == 3:
        if jokers == 1:
            add_hands(full, hand)
        elif jokers == 2:
            add_hands(four, hand)
        else:
            add_hands(two, hand)

    elif max_cards == 2 and len(cards_combos) == 4:
        if jokers >= 1:
            add_hands(three, hand)
        else:
            add_hands(one, hand)
    else:
        if jokers == 1:
            add_hands(one, hand)
        else:
            add_hands(high, hand)

result = 0
sorted_hands = high + one + two + three + full + four + five

n = 1
for hand in sorted_hands:
    result += total_hands[hand] * n
    n += 1

# Part 2
print(f"Part 2 Result = {result}")
# 251195607
