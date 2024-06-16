import sys
from collections import defaultdict

# part 1 credits
# https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day03p1.py

DAY = 3
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x.strip() for x in f.readlines()]

result = 0

mat = set()

for row, line in enumerate(data):
    for idx, c in enumerate(line[::]):
        if not c.isdigit() and c != "." and c != "\n":
            for dr in range(row - 1, row + 2):
                for dc in range(idx - 1, idx + 2):
                    if (
                        dr >= len(data)
                        or dr < 0
                        or dc >= len(line[::])
                        or dc < 0
                        or not data[dr][dc].isdigit()
                    ):
                        continue
                    while dc > 0 and data[dr][dc - 1].isdigit():
                        dc -= 1
                    mat.add((dr, dc))


ns = []

for r, c in mat:
    s = ""
    while c < len(data[r]) and data[r][c].isdigit():
        s += data[r][c]
        c += 1
    ns.append(int(s))

print(f"Part 1 result = {sum(ns)}")
# 525911

# Part 2
result = 0


def get_number(r, c):
    s = ""
    while c < len(data[r]) and data[r][c].isdigit():
        s += data[r][c]
        c += 1
    return int(s)


for row, line in enumerate(data):
    for idx, c in enumerate(line[::]):
        if c == "*":
            lis = set()
            for dr in range(row - 1, row + 2):
                for dc in range(idx - 1, idx + 2):
                    if (
                        dr >= len(data)
                        or dr < 0
                        or dc >= len(line[::])
                        or dc < 0
                        or not data[dr][dc].isdigit()
                    ):
                        continue
                    while dc > 0 and data[dr][dc - 1].isdigit():
                        dc -= 1
                    lis.add((dr, dc))

            if len(lis) == 2:
                lis = list(lis)
                result += get_number(lis[0][0], lis[0][1]) * get_number(
                    lis[1][0], lis[1][1]
                )

# Part 2 result
print(f"Part 2 result = {result}")
# 75805607
