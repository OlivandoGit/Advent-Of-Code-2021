signals = []

with open("Input.txt", "r") as f:
    signals = [[x.split(" ") for x in line.strip("\n").split(" | ")] for line in f]
    f.close()

total = 0
for s in signals:
    for s2 in s[1]:
        if len(s2) in [2,3,4,7]:
            total += 1

print(total)
