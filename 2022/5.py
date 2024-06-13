import regex as re

DAY = 5
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x for x in f.readlines()]


data_ = data[:8]

stack = {}
result = ""
for _ in range(1, 10):
    stack[str(_)] = []

# Reading the data
for a in data_[::-1]:
    for n, _ in enumerate(range(1, 36, 4), start=1):
        if a[_] != " ":
            stack[str(n)].append(a[_])

for a in data[10:]:
    qty, frm, to = re.findall(r"\d+", a)
    qty = int(qty)
    crates = stack[frm][-qty:]
    stack[to].extend(crates[::-1])
    stack[frm] = stack[frm][:-qty]

for a in range(1, 10):
    if stack[str(a)] != []:
        result += stack[str(a)][-1]

print(result)
# Answer = NTWZZWHFV

# part 2
stack = {}
result = ""
for _ in range(1, 10):
    stack[str(_)] = []

# Reading the data
for a in data_[::-1]:
    for n, _ in enumerate(range(1, 36, 4), start=1):
        if a[_] != " ":
            stack[str(n)].append(a[_])

for a in data[10:]:
    qty, frm, to = re.findall(r"\d+", a)
    qty = int(qty)
    stack[to].extend(stack[frm][-qty:])
    stack[frm] = stack[frm][:-qty]

for a in range(1, 10):
    if stack[str(a)] != []:
        result += stack[str(a)][-1]

print(result)
# BRZGFVBTJ
