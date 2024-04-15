DAY = 2
FILE_NAME = "inputs/" + str(DAY) + ".txt"
with open(FILE_NAME) as f:
    data = [x.strip() for x in f.readlines()]

result = 0

for n, game in enumerate(data, start=1):
    game = game.split(":")[-1].strip().split(";")
    number_of_rounds = len(game)
    i = 0
    for round in game:
        dic = {
            "green": 0,
            "blue": 0,
            "red": 0,
        }
        for temp in round.split(","):
            temp = temp.strip().split(" ")
            dic[temp[-1]] += int(temp[0])
        if dic["green"] <= 13 and dic["blue"] <= 14 and dic["red"] <= 12:
            i += 1
    if i == number_of_rounds:  # all rounds are pass
        result += n

print(result)

result = 0
# part 2
for n, game in enumerate(data, start=1):
    game = game.split(":")[-1].strip().split(";")
    number_of_rounds = len(game)
    i = 0
    dic = {
        "green": [],
        "blue": [],
        "red": [],
    }
    for round in game:
        for temp in round.split(","):
            temp = temp.strip().split(" ")
            # print(temp)
            dic[temp[-1]].append(int(temp[0]))
    result += max(dic["green"]) * max(dic["blue"]) * max(dic["red"])
print(result)
