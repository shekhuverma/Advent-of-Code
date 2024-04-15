DAY = 5
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x for x in f.readlines()]

result = ""

print(data[:10])

data = data[:10].split(" ")
for a in data:
    print(data)
