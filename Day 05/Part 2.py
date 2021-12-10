coords = []
maximum = 0
with open("Input.txt", "r") as f:
    for line in f:
        coords = [[[int(c) for c in coord.split(",")] for coord in line.strip("\n").split(" -> ")] for line in f]
    f.close()

maximum = max([max([max(c) for c in coord]) for coord in coords])
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

print(sum([len([r for r in row if r >= 2]) for row in map]))
