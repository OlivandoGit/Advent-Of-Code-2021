pos = []

with open("Input.txt", "r") as f:
    pos = f.readline().strip("\n").split(",")
    pos = [int(i) for i in pos]

    f.close()

fuel = []
for i in range(max(pos)):
    fuel.append(sum([abs(p - i) for p in pos]))

print(min(fuel))
