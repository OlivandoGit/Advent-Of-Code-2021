map = []

with open("Input.txt", "r") as f:
    map = [[int(char) for char in list(line.strip("\n"))] for line in f]
    f.close()

c = 0
for i in range(100):
    for y, row in enumerate(map):
        for x, r in enumerate(row):
            map[y][x] += 1

    flashed = []
    for y, row in enumerate(map):
        for x, r in enumerate(row):
            if not r > 9 or (x, y) in flashed:
                continue

            flashed.append((x, y))

    for flash in flashed:
        x, y = tuple(flash)
        c += 1
        
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if y + dy >= 0 and y + dy < len(map) and x + dx >= 0 and x + dx < len(row):
                    map[y + dy][x + dx] += 1

                    if map[y + dy][x + dx] > 9 and (x + dx, y + dy) not in flashed:
                        flashed.append((x + dx, y + dy))

    for y, row in enumerate(map):
        for x, r in enumerate(row):
            if r > 9:
                map[y][x] = 0

print(c)
