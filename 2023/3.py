DAY = 3
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x.strip() for x in f.readlines()]

result = 0

mat = []

for row, line in enumerate(data):
    for idx, c in enumerate(line[::]):
        if not c.isdigit() and c != "." and c != "\n":
            print(c)
            print(data[row + 1][idx])
            print(data[row - 1][idx])
            print(data[row][idx - 1])
            print(data[row][idx + 1])
            print(data[row - 1][idx - 1])
            print(data[row + 1][idx + 1])
            print(data[row + 1][idx - 1])
            print(data[row - 1][idx + 1])

            mat.append((row + 1, idx))
            mat.append((row - 1, idx))
            mat.append((row, idx - 1))
            mat.append((row, idx + 1))
            mat.append((row - 1, idx - 1))
            mat.append((row + 1, idx + 1))
            mat.append((row + 1, idx - 1))
            mat.append((row - 1, idx + 1))

print(mat)

# for a, b in mat:
#     if data[a][b].isdigit():
#         print(data[a][b])
#         result += int(data[a][b])

# print(result)
