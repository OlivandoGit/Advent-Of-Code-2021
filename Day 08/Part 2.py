from itertools import permutations

signals = []

with open("Input.txt", "r") as f:
    signals = [[x.split(" ") for x in line.strip("\n").split(" | ")] for line in f]
    f.close()

known = {2:"1", 3:"7", 4:"4", 7:"8"}
outputs = []
for s in signals:
    numbers = {known[ls]:s for s in s[0] if (ls := len(s)) in known}

    sixs = [i for i in s[0] if len(i) == 6]
    numbers["6"] = [i for i in sixs if len([j for j in i if j in numbers["1"]]) == 1][0]
    sixs.remove(numbers["6"])
    numbers["9"] = [i for i in sixs if len([j for j in i if j in numbers["4"]]) == 4][0]
    sixs.remove(numbers["9"])
    numbers["0"] = sixs[0]

    fives = [i for i in s[0] if len(i) == 5]
    numbers["3"] = [i for i in fives if len([j for j in i if j in numbers["1"]]) == 2][0]
    fives.remove(numbers["3"])
    numbers["5"] = [i for i in fives if len([j for j in i if j in numbers["6"]]) == 5][0]
    fives.remove(numbers["5"])
    numbers["2"] = fives[0]

    inverted = {"".join(sorted(list(v))):k for k,v in numbers.items()}
    output = ""
    for s2 in s[1]:
        s2 = "".join(sorted(list(s2)))
        output += inverted[s2]
    outputs.append(int(output))

print(sum(outputs))
