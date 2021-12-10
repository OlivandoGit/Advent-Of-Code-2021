lines = []
with open("Input.txt", "r") as f:
    lines = [line.strip("\n") for line in f]
    f.close()

brackets = {"(":")", "[":"]", "{":"}", "<":">"}
points = {")":1, "]":2, "}":3, ">":4}
totals = []
for line in lines:
    stack = []
    for char in line:
        if char in brackets:
            stack.append(char)

        elif brackets[stack[-1]] == char:
            stack.pop()

        elif brackets[stack[-1]] != char:
            break

    else:
        if len(stack) == 0:
            break

        total = 0
        for char in stack[::-1]:
            total = total * 5 + points[brackets[char]]

        totals.append(total)

totals.sort()
print(totals[len(totals) // 2])
