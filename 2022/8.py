DAY = 8
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [list(map(int, line)) for line in f.read().splitlines()]

row_length = len(data[1])
data_len = len(data)

edges = (row_length * data_len) - ((row_length - 2) * (data_len - 2))
res = 0

# Part 1
for row in range(1, len(data) - 1):
    for col in range(1, row_length - 1):
        k = data[row][col]
        # Row wise
        r1 = max(data[row][col + 1 :])  # Towards Right

        if k > r1:
            res += 1
            continue

        r2 = max(data[row][:col])  # Towards Left
        if k > r2:
            res += 1
            continue

        # Col wise
        l1 = max(list(data[row][col] for row in range(row + 1, data_len)))  # Downward
        if k > l1:
            res += 1
            continue

        l2 = max(list(data[row][col] for row in range(row - 1, -1, -1)))  # Upward
        if k > l2:
            res += 1
            continue

# Part 1 Answer
print("Part 1 Answer")
print(res + edges)
# 1717

# Part 2
# Scenic Score Calculation
scenic_score_max = 0
for row in range(1, len(data) - 1):
    for col in range(1, row_length - 1):
        scenic_score = 1
        k = data[row][col]
        # Row wise
        score = 0
        for tree in data[row][col + 1 :]:  # Towards Right
            if tree < k:
                score += 1
            else:
                score += 1
                break

        scenic_score *= score
        score = 0
        for tree in data[row][:col][::-1]:  # Towards Left
            if tree < k:
                score += 1
            else:
                score += 1
                break

        scenic_score *= score

        score = 0
        # Col wise
        for row_ in range(row + 1, data_len):  # Downward
            if data[row_][col] < k:
                score += 1
            else:
                score += 1
                break

        scenic_score *= score

        score = 0
        for row_ in range(row - 1, -1, -1):  # Upward
            if data[row_][col] < k:
                score += 1
            else:
                score += 1
                break

        scenic_score *= score

        scenic_score_max = max(scenic_score_max, scenic_score)

print("Part 2 Answer")
print(scenic_score_max)
