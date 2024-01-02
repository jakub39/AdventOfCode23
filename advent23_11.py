file = open('advent23_11.txt','r').read().splitlines()

empty_rows = []
for i in range(len(file)):
    if all(char == '.' for char in file[i]):
        empty_rows.append(i)

empty_cols = []
for i in range(len(file[0])):
    if all(char == '.' for char in [row[i] for row in file]):
        empty_cols.append(i)

galaxies = []
for row in range(len(file)):
    for col in range(len(file[row])):
        if file[row][col] == '#':
            galaxies.append((row, col))

distance = 0
for i in range(len(galaxies)):
    galaxy_row, galaxy_col = galaxies[i]
    for j in range(i):
        other_galaxy_row, other_galaxy_col = galaxies[j]
        for row in range(min(other_galaxy_row, galaxy_row), max(other_galaxy_row, galaxy_row)):
            distance += 2 if row in empty_rows else 1
        for col in range(min(other_galaxy_col, galaxy_col), max(other_galaxy_col, galaxy_col)):
            distance += 2 if col in empty_cols else 1

print(distance)

#part2

empty_rows2 = []
for i in file:
    if all(char == "." for char in i):
        empty_rows2.append(1000000)
    else:
        empty_rows2.append(1)

zipped = list(zip(*file))

empty_cols2 = []
for i in zipped:
    if all(char == "." for char in i):
        empty_cols2.append(1000000)
    else:
        empty_cols2.append(1)

new = set()
empty_rows2 = [i - 1 for i in empty_rows2]
empty_cols2 = [i - 1 for i in empty_cols2]
for i in range(len(file)):
    for char in range(len(file[0])):
        if file[i][char] == "#":
            new.add((i + sum(empty_rows2[:i]), char + sum(empty_cols2[:char])))

result = 0
for i in new:
    for r in new:
        result += abs(i[0] - r[0]) + abs(i[1] - r[1])

result //= 2

print(result)