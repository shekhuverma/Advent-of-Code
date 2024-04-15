DAY = 4
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x.strip() for x in f.readlines()]

result = 0

for a in data:
    sec1, sec2 = a.split(",")
    # print(sec1, sec2)
    x, y = sec1.split("-")
    i, j = sec2.split("-")
    x, y, i, j = int(x), int(y), int(i), int(j)
    if (x >= i and y <= j) or (i >= x and j <= y):
        result += 1

print("--- Part 1 ---")
print(result)

result = 0
print("--- Part 2 ---")

for a in data:
    sec1, sec2 = a.split(",")
    # print(sec1, sec2)
    x, y = sec1.split("-")
    i, j = sec2.split("-")
    x, y, i, j = int(x), int(y), int(i), int(j)
    if (x <= i <= y) or (i <= x <= j):
        result += 1

print(result)
