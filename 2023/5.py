DAY = 5
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.read()

seeds = data.split("\n")[0].split(":")[-1].split()
seeds = [int(x) for x in seeds]

print(seeds)

result = {79: 79, 14: 14, 55: 55, 13: 13}
data = data.split("\n\n")[1:]
for a in data:
    a = a.split(":")[-1].strip()
    for line in a.split("\n"):
        destination, source, rng = [int(x) for x in line.split(" ")]
        source = source + (rng - 1)
        destination = destination + (rng - 1)
        for temp in result:
            if temp>=source:
                