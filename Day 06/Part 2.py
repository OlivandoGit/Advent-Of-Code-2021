ages = [0 for i in range(9)]

with open("Input.txt", "r") as f:
    temp = temp = [int(i) for i in f.readline().strip("\n").split(",")]

    for tmp in temp:
        ages[tmp] += 1

    f.close()

for i in range(256):
    temp = ages.pop(0)
    ages[6] += temp
    ages.append(temp)

print(sum(ages))
