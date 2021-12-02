c = 0
with open("Input.txt", "r") as f:
    prev = int(f.readline().strip("\n"))
    for line in f:
        new = int(line.strip("\n"))
        if new > prev:
            c += 1

        prev = new

    f.close()
print(c)
