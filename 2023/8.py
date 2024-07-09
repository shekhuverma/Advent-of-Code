from math import lcm

import regex as re

DAY = 8
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.read()

data = data.split("\n")
instructions = data[0]
data = data[2:]

nodes = {}
a_nodes = []
for node in data:
    node = re.findall(r"\w{3}", node)
    if node[0][2] == "A":
        a_nodes.append(node[0])
    nodes[node[0]] = [node[1], node[2]]

steps = 0
starting = "AAA"


def follow_instructions(starting, steps):
    for instruction in instructions:
        if instruction == "L":
            starting = nodes[starting][0]
        else:
            starting = nodes[starting][1]

        steps += 1
        if starting == "ZZZ":
            return steps

    return follow_instructions(starting, steps)


## Part 1
print("Part 1 Answer")
print(follow_instructions(starting, steps))
# 16697

# part 2
# Taking LCM as reddit suggests
result = []
steps = 0


def follow_instructions_p2(starting, steps):
    for instruction in instructions:
        if instruction == "L":
            starting = nodes[starting][0]
        else:
            starting = nodes[starting][1]

        steps += 1
        if starting[2] == "Z":
            return steps

    return follow_instructions_p2(starting, steps)


steps = 0
for node in a_nodes:
    result.append(follow_instructions_p2(node, steps))

print("Part 2 Answer")
print(lcm(*result))
