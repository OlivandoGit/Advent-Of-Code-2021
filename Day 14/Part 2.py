polymer = ""
pairs = {}

with open("Input.txt", "r") as f:
    polymer = f.readline().strip("\n")
    pairs = dict(line.strip("\n").split(" -> ") for line in f if "->" in line)
    f.close()

chars = {}
for char in polymer:
    chars[char] = chars.get(char, 0) + 1

repeats = {}
splits = [polymer[i : i + 2] for i in range(len(polymer) - 1)]
for i, split in enumerate(splits):
    repeats[split] = repeats.get(split, 0) + 1

for i in range(40):
    copy = repeats.copy()

    for rep in [r for r in list(copy) if copy[r] > 0]:
        for n in [rep[0] + pairs[rep], pairs[rep] + rep[1]]:
            repeats[n] = repeats.get(n, 0) + copy[rep]

        chars[pairs[rep]] = chars.get(pairs[rep], 0) + copy[rep]
        repeats[rep] -= copy[rep]

print(max(chars.values()) - min(chars.values()))
