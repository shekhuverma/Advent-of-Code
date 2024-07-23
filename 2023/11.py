DAY = 11
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x.strip() for x in f.readlines()]


def solve(data, expansion: int):
    res = []
    count = 1
    r_exp = 0
    c_exp = []
    temp = 0
    result = 0
    col_check = ""
    for i in range(len(data)):
        if col_check == "." * len(data):
            c_exp.append(i - 1)
        col_check = ""
        if temp == len(data[0]):
            r_exp += expansion
        temp = 0
        for j in range(len(data[0])):
            col_check += data[j][i]
            if data[i][j] == "#":
                res.append([i + r_exp, j])
                count += 1
            else:
                temp += 1

    # To expand the columns
    X = 0
    for val in res:
        X = 0
        for pt in c_exp:
            if val[1] > pt:
                X += expansion
        val[1] += X

    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            temp = abs(res[i][0] - res[j][0]) + abs(res[i][1] - res[j][1])
            result += temp

    print(result)


print("Part 1 Answer :")
solve(data, 1)
print("Part 2 Answer :")
solve(data, 999999)
