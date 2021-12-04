def checkwin(board, numbers):
    #Check rows
    for row in board:
        if set(row).issubset(set(numbers)):
            return True

    #Check columns
    for i, r in enumerate(board):
        if set([row[i] for row in board]).issubset(set(numbers)):
            return True

    return False

lines = []
with open("Input.txt", "r") as f:
    lines = f.readlines()
    f.close()

numbers = list(lines.pop(0).strip("\n").split(","))

boards = []
board = []
for i, line in enumerate(lines[1:]):
    if line != "\n":
        board.append(list(filter(lambda x: x != "", list(line.strip("\n").split(" ")))))

    if line == "\n" or i == len(lines) - 2:
        boards.append(board)
        board = []

for i, num in enumerate(numbers):
    for board in boards:
        if checkwin(board, numbers[:i + 1]):
            break
    else:
        continue
    break

total = 0
for row in board:
    for num in row:
        if num not in numbers[:i + 1]:
            total += int(num)

print(total)
print(total * int(numbers[i]))
