map = []

with open("Input.txt", "r") as f:
    map = [[int(char) for char in list(line.strip("\n"))] for line in f]
    f.close()

lowest = []
for y, row in enumerate(map):
    for x, e in enumerate(row):
        lower = 0
        if y - 1 >= 0 and map[y - 1][x] <= e:
            lower += 1
        if y + 1 < len(map) and map[y + 1][x] <= e:
            lower += 1
        if x - 1 >= 0 and map[y][x - 1] <= e:
            lower += 1
        if x + 1 < len(row) and map[y][x + 1] <= e:
            lower += 1

        if lower == 0:
            lowest.append(e)

print(sum([x + 1 for x in lowest]))
