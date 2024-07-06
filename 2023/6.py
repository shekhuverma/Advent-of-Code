import regex as re

DAY = 6
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.read()

data = data.split("\n")

ip_time = map(int, re.findall(r"\d+", data[0]))
ip_distance = map(int, re.findall(r"\d+", data[1]))

result = 1

# Part 1
for time, distance in zip(ip_time, ip_distance):
    ways = 0
    print(time, distance)
    for x in range(1, time):
        if (time - x) * x > distance:
            ways += 1
    result *= ways
print(result)

# part 2 (Brute Force Approach)
ip_time = int("".join(re.findall(r"\d+", data[0])))
ip_distance = int("".join(re.findall(r"\d+", data[1])))

ways = 0
for x in range(1, ip_time):
    if (ip_time - x) * x > ip_distance:
        ways += 1
print(ways)
# 40651271

## Part 2 Can also be solved by using quadratic equation
