import heapq
from collections import Counter

DAY = 1
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME, encoding="utf-8") as f:
    data = [x.strip() for x in f.readlines()]


def part1() -> int:
    result = 0
    list1 = []
    list2 = []

    heapq.heapify(list1)
    heapq.heapify(list2)
    for line in data:
        element1, element2 = line.split()
        heapq.heappush(list1, int(element1))
        heapq.heappush(list2, int(element2))

    for line in data:
        result += abs(heapq.heappop(list1) - heapq.heappop(list2))

    return result


def part2() -> int:
    result = 0
    list1 = []
    list2 = []

    for line in data:
        element1, element2 = line.split()
        list1.append(int(element1))
        list2.append(int(element2))

    frequency = Counter(list2)

    for number in list1:
        result += number * frequency[number]

    return result


print(part1())
print(part2())
