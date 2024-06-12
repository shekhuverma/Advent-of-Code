DAY = 4
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x.strip() for x in f.readlines()]

result = 0


for n, card in enumerate(data, start=1):
    temp = 0
    temp1 = 0
    card = card.split(":")[1].split("|")
    winning_numbers = card[0].split()
    card = card[-1].split()
    for a in winning_numbers:
        if a in card:
            temp += 1
    if temp != 0:
        result += 2 ** (temp - 1)

print(result)


def number_of_winning_card(winning_numbers: list, card: list) -> int:
    card_copies = 0
    for a in winning_numbers:
        if a in card:
            card_copies += 1
    return card_copies


# part 2
result = 0
card_copies = [1] * len(data)
for n, card in enumerate(data):
    card = card.split(":")[1].split("|")
    winning_numbers = card[0].split()
    card = card[-1].split()
    for j in range(number_of_winning_card(winning_numbers, card)):
        card_copies[n + 1 + j] += card_copies[n]

result = sum(card_copies)
print(result)
