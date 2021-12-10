segments = []

with open("Example.txt", "r") as f:
    lines = f.read().splitlines()

    for line in lines:
        tries, output = line.split(" | ")
        tries = tries.split(" ")
        output = output.split(" ")
        segments.append((tries, output))

    f.close()

total = 0
for s in segments:
    for s2 in s[1]:
        if len(s2) in [2,3,4,7]:
            total += 1

print(total)
