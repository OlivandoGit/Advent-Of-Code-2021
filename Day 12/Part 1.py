caves = {}
with open("Input.txt", "r") as f:
    for line in f:
        start, end = line.strip("\n").split("-")

        if start not in caves:
            caves[start] = [end]
        else:
            caves[start].append(end)

        if end not in caves:
            caves[end] = [start]
        else:
            caves[end].append(start)

    f.close()

paths = []
for cave in caves["start"]:
    paths.append(["start", cave])

for path in paths:
    if path[-1] not in caves or path[-1] == "end":
        continue

    for cave in caves[path[-1]]:
        if cave.islower() and cave in path or cave == "start":
            continue

        new = path[:]
        new.append(cave)

        paths.append(new)

paths = [path for path in paths if path[-1] == "end"]
print(len(paths))
