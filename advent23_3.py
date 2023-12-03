subor = open("advent23_3.txt", "r").read()

riadky = subor.split('\n')

grid = {}

for i, riadok in enumerate(riadky):
    for j, znak in enumerate(riadok):
        grid[i + 1j * j] = znak

cast1 = 0
gears = {}

for i in range(len(riadky)):
    num = ''
    valid = False
    gear_pos = None

    for j in range(len(riadky[i])):  
        znak = grid[i + 1j * j]

        if znak.isdigit():
            num += znak
            if not valid:
                for x1 in range(-1, 2):
                    for y2 in range(-1, 2):
                        neighbor_coord = i + x1 + 1j * (j + y2)
                        neighbor_char = grid.get(neighbor_coord, '.')
                        if not neighbor_char.isdigit() and neighbor_char != '.':
                            valid = True
                            if neighbor_char == '*':
                                gear_pos = neighbor_coord
        else:
            if valid:
                n = int(num)
                cast1 += n
                if gear_pos:
                    if gear_pos not in gears:
                        gears[gear_pos] = []
                    gears[gear_pos].append(n)
                valid = False
                gear_pos = None
            num = ''

    if valid:
        n = int(num)
        cast1 += n
        if gear_pos:
            if gear_pos not in gears:
                gears[gear_pos] = []
            gears[gear_pos].append(n)

print(cast1)

cast2 = sum(gn[0] * gn[1] for gn in gears.values() if len(gn) == 2)
print(cast2)