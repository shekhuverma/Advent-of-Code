# Took help from
# https://www.youtube.com/watch?v=yeghi1Va1GI&ab_channel=neynt

from collections import defaultdict

DAY = 7
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x for x in f.readlines()]

result = defaultdict(int)
# To store the current directory
stack = []
for command in data:
    command = command.strip()
    if command[0] == "$":
        if command[2] == "c":
            directory = command[5:]
            if directory == "/":
                # Go to root and clear the stack
                stack = ["/"]
            elif directory == "..":
                stack.pop()
            else:
                stack.append(stack[-1] + f"{directory}/")
    else:
        x, y = command.split()
        if x != "dir":
            for path in stack:
                result[path] += int(x)

# Answer 1
print(sum(x for x in result.values() if x < 100000))

space_req = result["/"] - 40000000

# Answer 2
print(min(x for x in result.values() if x >= space_req))
