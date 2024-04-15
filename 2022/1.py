DAY = 1
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.read()

data = data.split("\n")

sum = 0
result = 0

for i in data:
    if i == "":
        if sum > result:
            result = sum
        sum = 0
    else:
        sum += int(i)

print(result)

# part 2

sum = 0
result = 0
total = []
for i in data:
    if i == "":
        total.append(sum)
        # if sum > result:
        #     result = sum
        sum = 0
    else:
        sum += int(i)

total.sort()

print(total[-1] + total[-2] + total[-3])
