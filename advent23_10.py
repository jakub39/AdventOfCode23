file = open("advent23_10.txt", "r")

field = []
y = 0
for line in file:
    field.append(line)
    s_location = line.find('S')
    if s_location >= 0:
        x1, y1 = s_location, y
    y += 1

x, y, steps = x1, y1, 0
if x < len(field[0]) - 1 and field[y][x + 1] in {'-', 'J', '7'}:
    direction = 1
elif y < len(field) - 1 and field[y + 1][x] in {'|', 'J', 'L'}:
    direction = 2
if x > 0 and field[y][x - 1] in {'-', 'F', 'L'}:
    direction = 3
if y > 1 and field[y - 1][x] in {'|', 'F', '7'}:
    direction = 0

while True:
    if direction == 0:
        y -= 1
    elif direction == 1:
        x += 1
    elif direction == 2:
        y += 1
    elif direction == 3:
        x -= 1

    if field[y][x] == 'L':
        direction = 1 if direction == 2 else 0
    elif field[y][x] == 'J':
        direction = 3 if direction == 2 else 0
    elif field[y][x] == '7':
        direction = 2 if direction == 1 else 3
    elif field[y][x] == 'F':
        direction = 2 if direction == 3 else 1

    steps += 1
    if x1 == x and y1 == y:
        print(steps // 2 + (1 if steps % 2 == 1 else 0))
        quit()
    