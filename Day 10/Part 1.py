lines = []
with open("Input.txt", "r") as f:
    lines = [line.strip("\n") for line in f]
    f.close()

brackets = {"(":")", "[":"]", "{":"}", "<":">"}
points = {")":3, "]":57, "}":1197, ">":25137}
total = 0

for line in lines:
    stack = []
    for char in line:
        if char in brackets:
            stack.append(char)

        elif brackets[stack[-1]] == char:
            stack.pop()

        elif brackets[stack[-1]] != char:
            total += points[char]
            break

print(total)
