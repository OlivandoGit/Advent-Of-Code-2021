with open("Input.txt", "r") as f:
    map = [[int(x) for x in line.strip("\n")] for line in f]
    f.close()

risk = {}
dist = {}
for y, row in enumerate(map):
    for x, r in enumerate(row):
        risk[(x, y)] = r
        dist[(x, y)] = float("inf")

dist[(0, 0)] = 0
queue = [(0, 0)]
while len(queue) > 0:
    node = queue.pop(0)
    x, y = tuple(node)

    neighbours = [(x, y - 1) if y - 1 >= 0 else None,
                  (x, y + 1) if y + 1 < len(map) else None,
                  (x - 1, y) if x - 1 >= 0 else None,
                  (x + 1, y) if x + 1 < len(map[0]) else None]

    for n in neighbours:
        if n == None:
            continue

        new = dist[node] + risk[n]
        if new < dist[n]:
            dist[n] = new
            queue.append(n)

print(dist[(len(map[0]) - 1, len(map) - 1)])
