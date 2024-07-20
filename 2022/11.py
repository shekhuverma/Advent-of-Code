DAY = 11
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.read()

monkeys = {}
result_p1 = {}
result_p2 = {}
N = 1

for data in data.split("\n\n"):
    data = data.split("\n")
    monkey_number = int(data[0][-2])
    result_p1[monkey_number] = 0
    result_p2[monkey_number] = 0
    items = data[1].split(":")[-1].split(",")
    items = list(map(int, items))
    op = [data[2].split()[-2], data[2].split()[-1]]
    test = int(data[3].split()[-1])
    N *= test
    true = int(data[4][-1])
    false = int(data[5][-1])

    monkeys[monkey_number] = [items, op, test, true, false]


all_items = [[value for value in monkeys[x][0]] for x in monkeys.keys()]


def money_process_p1(monkeys):
    for monkey_number in monkeys.keys():
        operation, operand = monkeys[monkey_number][1]
        items = all_items[monkey_number]
        result_p1[monkey_number] += len(items)
        for item in items:
            if operand == "old":
                item **= 2
            elif operation == "*":
                item *= int(operand)
            else:
                item += int(operand)
            item //= 3
            if item % monkeys[monkey_number][2] == 0:
                all_items[monkeys[monkey_number][3]].append(item)
            else:
                all_items[monkeys[monkey_number][4]].append(item)
        items.clear()


for _ in range(20):
    money_process_p1(monkeys)

result = sorted(result_p1.values())
print(result[-1] * result[-2])

# using the modulo trick from the following resources
# 1) https://www.youtube.com/watch?v=Pqjl5qhHdWc
# 2) https://www.youtube.com/watch?v=F4MCuPZDKog

all_items = [[value for value in monkeys[x][0]] for x in monkeys.keys()]


def money_process_p2(monkeys):
    for monkey_number in monkeys.keys():
        operation, operand = monkeys[monkey_number][1]
        items = all_items[monkey_number]
        result_p2[monkey_number] += len(items)
        for item in items:
            if operand == "old":
                item **= 2
            elif operation == "*":
                item *= int(operand)
            else:
                item += int(operand)
            item %= N
            if item % monkeys[monkey_number][2] == 0:
                all_items[monkeys[monkey_number][3]].append(item)
            else:
                all_items[monkeys[monkey_number][4]].append(item)
        items.clear()


for _ in range(10_000):
    money_process_p2(monkeys)

result = sorted(result_p2.values())
print(result[-1] * result[-2])
