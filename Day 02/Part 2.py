horizontal, depth, aim = 0, 0, 0

with open("Input.txt", "r") as f:
    for line in f:
        direction, distance = line.strip("\n").split(" ")
        distance = int(distance)

        if direction == "forward":
            horizontal += distance
            depth -= aim * distance

        elif direction == "up":
            aim += distance

        elif direction == "down":
            aim -= distance


    f.close()

print(horizontal, depth, horizontal*depth)
