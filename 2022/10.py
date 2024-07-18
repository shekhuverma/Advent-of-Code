DAY = 10
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = f.readlines()


def part1(input):
    X = 1
    cycle = 1
    res = {}
    for line in input:
        line = line.split()
        if line[0] == "noop":
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                res[cycle] = X * cycle
                # print(f"cycle = {cycle} {X} res= {X*cycle}")
        else:
            cycle += 1
            if cycle in [20, 60, 100, 140, 180, 220]:
                res[cycle] = X * cycle
                # print(f"cycle = {cycle} {X} res= {X*cycle}")
            X += int(line[1])
            cycle += 1

        if cycle in [20, 60, 100, 140, 180, 220]:
            res[cycle] = X * cycle
            # print(f"cycle = {cycle} {X} res= {X*cycle}")
        if cycle >= 220:
            break

    print(res)
    return sum(res.values())
    # return input


result = part1(data)
print(f"Part 1 Result = {result}")


def part2(input):
    X = 1
    cycle = 0
    current_row = ["."] * 40

    for line in input:
        line = line.split()

        if X - 1 <= cycle <= X + 1:
            current_row[cycle] = "#"

        cycle += 1
        if cycle == 40:
            cycle = 0
            print("".join(current_row))
            current_row = ["."] * 40

        if line[0] != "noop":
            if X - 1 <= cycle <= X + 1:
                current_row[cycle] = "#"

            X += int(line[1])
            cycle += 1
            if cycle == 40:
                cycle = 0
                print("".join(current_row))
                current_row = ["."] * 40


part2(data)
