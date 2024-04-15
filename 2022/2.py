DAY = 2
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.readlines()

total_score = 0
score = 0
for round in data:
    i, j = round.split()
    if i == "A":  # rock
        if j == "Y":
            score += 6
        elif j == "X":
            score += 3

    elif i == "B":  # paper
        if j == "Z":
            score += 6
        elif j == "Y":
            score += 3

    else:  # scissor
        if j == "X":
            score += 6
        elif j == "Z":
            score += 3

    score += ord(j) - 87
    total_score += score
    score = 0
print(total_score)

# part 2
total_score = 0
score = 0
for round in data:
    i, j = round.split()
    if j == "X":  # loose
        if i == "A":
            score += 3
        elif i == "B":
            score += 1
        else:
            score += 2

    elif j == "Y":  # draw
        if i == "A":
            score += 1 + 3
        elif i == "B":
            score += 2 + 3
        else:
            score += 3 + 3

    else:  # win
        if i == "A":
            score += 2 + 6
        elif i == "B":
            score += 3 + 6
        else:
            score += 1 + 6

    total_score += score
    score = 0
print(total_score)
