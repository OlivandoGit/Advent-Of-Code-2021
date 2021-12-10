from math import prod

def checkNeighbours(x, y):
    checked.append((x, y))

    size = 0
    if y - 1 >= 0 and map[y - 1][x] != 9 and (x, y - 1) not in checked:
        size += 1 + checkNeighbours(x, y - 1)
    if y + 1 < len(map) and map[y + 1][x] != 9 and (x, y + 1) not in checked:
        size += 1 + checkNeighbours(x, y + 1)
    if x - 1 >= 0 and map[y][x - 1] != 9 and (x - 1, y) not in checked:
        size += 1 + checkNeighbours(x - 1, y)
    if x + 1 < len(row) and map[y][x + 1] != 9 and (x + 1, y) not in checked:
        size += 1 + checkNeighbours(x + 1, y)

    return size

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
            lowest.append((x, y))

checked = []
sizes = []
for low in lowest:
    checked.append(low)
    x, y = tuple(low)
    sizes.append(1 + checkNeighbours(x, y))

sizes.sort(reverse = True)

print(prod(sizes[0:3]))
