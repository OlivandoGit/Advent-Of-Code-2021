coords = []
maximum = 0
with open("Input.txt", "r") as f:
    for line in f:
        start, end = line.strip("\n").split(" -> ")
        start = [int(x) for x in start.split(",")]
        end = [int(x) for x in end.split(",")]

        maximum = max(max(max(start), max(end)), maximum)

        coords.append((start, end))
    f.close()

map = [[0 for j in range(maximum + 1)] for i in range(maximum + 1)]

for coord in coords:
    #Vertical
    if coord[0][0] == coord[1][0]:
        step = 1 if coord[0][1] < coord[1][1] else (-1)
        for y in range(coord[0][1], coord[1][1] + step, step):
            map[y][coord[0][0]] += 1

    #Horizontal
    elif coord[0][1] == coord[1][1]:
        step = 1 if coord[0][0] < coord[1][0] else (-1)
        for x in range(coord[0][0], coord[1][0] + step, step):
            map[coord[0][1]][x] += 1

    #Diagonal
    else:
        x_step = 1 if coord[0][0] < coord[1][0] else (-1)
        y_step = 1 if coord[0][1] < coord[1][1] else (-1)

        x_range = range(coord[0][0], coord[1][0] + x_step, x_step)
        y_range = range(coord[0][1], coord[1][1] + y_step, y_step)

        for i, x in enumerate(x_range):
            map[y_range[i]][x] += 1

count = 0
for row in map:
    for r in row:
        if r >= 2:
            count += 1

print(count)
