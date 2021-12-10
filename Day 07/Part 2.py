pos = []

with open("Input.txt", "r") as f:
    pos = [int(i) for i in f.readline().strip("\n").split(",")]

    f.close()

fuel = []
for i in range(max(pos)):
    fuel.append(sum([(lambda p: ((p ** 2 + p) // 2)) (abs(p - i)) for p in pos]))

print(min(fuel))
