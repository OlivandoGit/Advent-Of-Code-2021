horizontal, depth = 0, 0

with open("Input.txt", "r") as f:
    for line in f:
        direction, distance = line.strip("\n").split(" ")
        distance = int(distance)

        if direction == "forward":
            horizontal += distance

        elif direction == "up":
            depth -= distance

        elif direction == "down":
            depth += distance


    f.close()

print(horizontal, depth, horizontal*depth)
