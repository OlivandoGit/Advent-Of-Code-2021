with open("Input.txt", "r") as f:
    lines = f.read().splitlines()
    bits = [[0, 0] for i in enumerate(lines[0])]

    for line in lines:
        for i, bit in enumerate(line):
            bit = int(bit)
            bits[i][bit] = bits[i][bit] + 1

    gamma, epsilon = "", ""
    for bit in bits:
        gamma += str(bit.index(max(bit)))
        epsilon += str(bit.index(min(bit)))

    print(int(gamma, 2) * int(epsilon, 2))

    f.close()
