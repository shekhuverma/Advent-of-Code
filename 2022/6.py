DAY = 6
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.read()

# Part 1
for a in range(0, len(data)):
    if len(set(data[a : a + 4])) == 4:
        print(f"Part one result {a + 4}")
        # 1848
        break

# Part 2
for a in range(0, len(data)):
    if len(set(data[a : a + 14])) == 14:
        print(f"Part two result {a+14}")
        # 2308
        break
