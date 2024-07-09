from math import pow

DAY = 9
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.readlines()


def part1(data: list[str]) -> None:
    result = 0
    for line in data:
        line = list(map(int, line.split()))
        temp = line[-1]
        res = []
        while res != [0] * len(line):
            res = []
            for x in range(1, len(line)):
                res.append(line[x] - line[x - 1])
            temp += res[-1]
            line = res

        result += temp
    print(result)


def part2(data: list[str]) -> None:
    result = 0
    for line in data:
        line = list(map(int, line.split()))
        temp = line[0]
        res = []
        n = 1
        while res != [0] * len(line):
            res = []
            for x in range(1, len(line)):
                res.append(line[x] - line[x - 1])
            temp += pow(-1, n) * res[0]
            line = res
            n += 1
        result += temp
    print(result)


# Part 1
part1(data)

# Part 2
part2(data)
