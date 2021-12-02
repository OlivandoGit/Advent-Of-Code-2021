c = 0
with open("Input.txt", "r") as f:
    lines = f.readlines()
    measurements = []

    lines = [int(line.strip("\n")) for line in lines]

    for i in range (0, len(lines) - 2):
        measurements.append(lines[i] + lines[i + 1] + lines[i + 2])

    for i in range(1, len(measurements)):
        if measurements[i] > measurements[i - 1]:
            c += 1

    f.close()

print(c)
