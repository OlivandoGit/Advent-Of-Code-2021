dots = []
folds = []

with open("Input.txt", "r") as f:
    for line in f:
        if "fold along" in line:
            folds.append(line.strip("\n").strip("fold along ").split("="))

        elif line != "\n":
            dots.append([int(i) for i in line.strip("\n").split(",")])

    f.close()

maxx = max([dot[0] for dot in dots])
maxy = max([dot[1] for dot in dots])
paper = [["." for x in range(maxx + 1)] for y in range(maxy + 1)]

for dot in dots:
    paper[dot[1]][dot[0]] = "#"

for fold in folds:
    if fold[0] == "y":
        paper2 = paper[int(fold[1]) + 1:]
        paper = paper[:int(fold[1])]

        for y, row in enumerate(paper2):
            for x, r in enumerate(row):
                if r == "#":
                    paper[int(fold[1]) - 1 - y][x] = "#"

    elif fold[0] == "x":
        paper2 = [row[int(fold[1]) + 1:] for row in paper]
        paper = [row[:int(fold[1])] for row in paper]

        for y, row in enumerate(paper2):
            for x, r in enumerate(row):
                if r == "#":
                    paper[y][int(fold[1]) - 1 - x] = "#"

for row in paper:
    print(*row)
