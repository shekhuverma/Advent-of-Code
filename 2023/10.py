from math import ceil
from time import perf_counter

DAY = 10
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.read().split()


def part1_old(data) -> None:
    """Used dictionary to visualuise the path and debug
    Less efficient
    """
    graph = {}
    for x, line in enumerate(data):
        for y, pipe in enumerate(line):
            if pipe == "S":
                print(x, y)
                break
        else:
            continue
        break

    coordinates = []

    # boundry conditions
    if x < 0:
        x = 0
    if y > len(data):
        y = len(data)

    # Coordinates of starting point
    # print(x, y)

    if data[x + 1][y] in "|LJ":
        coordinates.append((x + 1, y))
    if data[x - 1][y] in "|LJ":
        coordinates.append((x - 1, y))
    if data[x][y + 1] in "-J7":
        coordinates.append((x, y + 1))
    if data[x][y - 1] in "-FL":
        coordinates.append((x, y - 1))

    start_x, start_y = x, y
    x, y = coordinates[1]
    graph[(start_x, start_y)] = [(x, y)]
    print(graph)
    while True:
        if data[x][y] == "|":
            if graph.get((x - 1, y)) is None:
                graph[(x, y)] = [(x - 1, y), data[x - 1][y]]
                x -= 1
            else:
                graph[(x, y)] = [(x + 1, y), data[x + 1][y]]
                x += 1

        elif data[x][y] == "-":
            if graph.get((x, y + 1)) is None:
                graph[(x, y)] = [(x, y + 1), data[x][y + 1]]
                y += 1
            else:
                graph[(x, y)] = [(x, y - 1), data[x][y - 1]]
                y -= 1

        elif data[x][y] == "L":
            if graph.get((x, y + 1)) is None:
                graph[(x, y)] = [(x, y + 1), data[x][y + 1]]
                y += 1
            else:
                graph[(x, y)] = [(x - 1, y), data[x - 1][y]]
                x -= 1
        elif data[x][y] == "J":
            if graph.get((x - 1, y)) is None:
                graph[(x, y)] = [(x - 1, y), data[x - 1][y]]
                x -= 1
            else:
                graph[(x, y)] = [(x, y - 1), data[x][y - 1]]
                y -= 1
        elif data[x][y] == "7":
            if graph.get((x, y - 1)) is None:
                graph[(x, y)] = [(x, y - 1), data[x][y - 1]]
                y -= 1
            else:
                graph[(x, y)] = [(x + 1, y), data[x + 1][y]]
                x += 1

        elif data[x][y] == "F":
            if graph.get((x, y + 1)) is None:
                graph[(x, y)] = [(x, y + 1), data[x][y + 1]]
                y += 1
            else:
                graph[(x, y)] = [(x + 1, y), data[x + 1][y]]
                x += 1

        if (x, y) == coordinates[0] or (x, y) == coordinates[1]:
            break

    print(ceil(len(graph) / 2))


def part1(data) -> None:
    graph = set()
    # graph={}
    for x, line in enumerate(data):
        for y, pipe in enumerate(line):
            if pipe == "S":
                break
        else:
            continue
        break

    coordinates = []

    # boundry conditions
    if x < 0:
        x = 0
    if y > len(data):
        y = len(data)

    # Coordinates of starting point
    # print(x, y)

    if data[x + 1][y] in "|LJ":
        coordinates.append((x + 1, y))
    if data[x - 1][y] in "|LJ":
        coordinates.append((x - 1, y))
    if data[x][y + 1] in "-J7":
        coordinates.append((x, y + 1))
    if data[x][y - 1] in "-FL":
        coordinates.append((x, y - 1))

    start_x, start_y = x, y
    x, y = coordinates[1]
    graph.add((start_x, start_y))
    while True:
        if data[x][y] == "|":
            graph.add((x, y))
            if (x - 1, y) not in graph:
                x -= 1
            else:
                x += 1

        elif data[x][y] == "-":
            graph.add((x, y))
            if (x, y + 1) not in graph:
                y += 1
            else:
                y -= 1

        elif data[x][y] == "L":
            graph.add((x, y))
            if (x, y + 1) not in graph:
                y += 1
            else:
                x -= 1
        elif data[x][y] == "J":
            graph.add((x, y))
            if (x - 1, y) not in graph:
                x -= 1
            else:
                y -= 1
        elif data[x][y] == "7":
            graph.add((x, y))
            if (x, y - 1) not in graph:
                y -= 1
            else:
                x += 1

        elif data[x][y] == "F":
            graph.add((x, y))
            if (x, y + 1) not in graph:
                y += 1
            else:
                x += 1

        if (x, y) == coordinates[0] or (x, y) == coordinates[1]:
            graph.add((x, y))
            break

    return graph


graph = part1(data)
print(ceil(len(graph) / 2))
# 6690


# For second part, took help from
# https://github.com/savbell/advent-of-code-one-liners/blob/master/2023/day-10.py
def part2(data):
    graph = part1(data)
    result = set()
    within = False
    for x, line in enumerate(data):
        for y, pipe in enumerate(line):
            if (x, y) in graph:
                if data[x][y] in ["|", "L", "J"]:
                    within = not within
            elif within:
                result.add((x, y))
    print(len(result))


part2(data)
# 525
