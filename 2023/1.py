DAY = 1
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x.strip() for x in f.readlines()]

result = 0

for a in data:
    calib = ""
    for c in a:
        if c.isdigit():
            calib += c
            break
    for c in a[::-1]:
        if c.isdigit():
            calib += c
            break

    result += int(calib)

print(result)

# part 2
sub_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

result = 0
for a in data:
    temp = []

    for i, c in enumerate(a):
        if c.isdigit():
            temp.append(c)

        for j, val in enumerate(sub_strings, start=1):
            if a[i:].startswith(val):
                temp.append(str(j))
    result += int(temp[0] + temp[-1])
print(result)
