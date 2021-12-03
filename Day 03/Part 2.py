def frequency(i, numbers):
    bits = [0, 0]
    for num in numbers:
        bits[int(num[i])] = bits[int(num[i])] + 1

    return bits

with open("Input.txt", "r") as f:
    lines = f.read().splitlines()

    oxygen = list(lines)
    for i, bit in enumerate(lines[0]):
        bits = frequency(i, oxygen)

        if bits[0] == bits[1]:
            oxygen = list(filter(lambda o: o[i] == "1", oxygen))
        else:
            oxygen = list(filter(lambda o: o[i] == str(bits.index(max(bits))), oxygen))

        if len(oxygen) == 1:
            break

    scrubber = list(lines)
    for i, bit in enumerate(lines[0]):
        bits = frequency(i, scrubber)

        if bits[0] == bits[1]:
            scrubber = list(filter(lambda s: s[i] == "0", scrubber))
        else:
            scrubber = list(filter(lambda s: s[i] == str(bits.index(min(bits))), scrubber))

        if len(scrubber) == 1:
            break
            
    print(int(oxygen[0], 2) * int(scrubber[0], 2))

    f.close()
