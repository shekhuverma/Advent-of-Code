DAY = 3
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x.strip() for x in f.readlines()]

result = 0
for rucksack in data:
    comp1, comp2 = rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    item = list(set(comp1).intersection(comp2))[0]
    if ord(item) < 97:
        result += ord(item) - 38
    else:
        result += ord(item) - 96

print(result)

# part 2
result = 0
for i in range(0, len(data), 3):
    e1 = data[i]
    e2 = data[i + 1]
    e3 = data[i + 2]
    item = list(set(e1).intersection(e2).intersection(e3))[0]
    if ord(item) < 97:
        result += ord(item) - 38
    else:
        result += ord(item) - 96

print(result)
