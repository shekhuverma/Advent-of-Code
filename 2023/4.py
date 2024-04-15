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
    # print("___________")
    for a in winning_numbers:
        if a in card:
            temp += 1
            # print(f"temp = {temp}")
    # print(f"Result = {result}")
    if temp != 0:
        result += 2 ** (temp - 1)

print(result)

# part 2
card_copies = {1: 1}
for n, card in enumerate(data, start=1):
    # card_copies[n + 1] = 0
    card = card.split(":")[1].split("|")
    winning_numbers = card[0].split()
    card = card[-1].split()
    j = 1
    for a in winning_numbers:
        if a in card:
            try:
                card_copies[n + j] += 1
            except KeyError:
                card_copies[n + j] = 1
            j += 1

    print(card_copies)
