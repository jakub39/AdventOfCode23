#part1
file = open("advent23_8.txt", "r").read().splitlines()
instructions = file[0]
maps = file[2:]
new_map = {}

for line in maps:
    casti = line.split("=")
    lavaprava = casti[1].split(",")
    kluc = casti[0].strip()
    new_map[kluc] = {
        "R": lavaprava[1][:-1].strip(),
        "L": lavaprava[0][2:5]
    }

value = "AAA"
steps = 0

while value != "ZZZ":
    value = new_map[value][instructions[steps % len(instructions)]]
    steps += 1

print(steps)

#part2
directions, currents = "", []

input_map = {}
with open("advent23_8.txt", "r") as file:
    file_input = file.read().splitlines()
    directions, currents = file_input[0], []

    for line in file_input[2:]:
        parts = line.split("=")
        sides = parts[1].split(",")
        node = parts[0].strip()
        input_map[node] = {"L": sides[0][2:5], "R": sides[1][:-1].strip()}
        if node.endswith("A"):
            currents.append(node)

loops = []
for current in currents:
    loop = []
    counter, first_goal = 0, None

    while True:
        while counter == 0 or not current.endswith("Z"):
            current = input_map[current][directions[counter % len(directions)]]
            counter += 1
        loop.append(counter)

        if not first_goal:
            first_goal = current
            counter = 0
        elif current == first_goal:
            break

    loops.append(loop)

loops = [loop[0] for loop in loops]

lcm = loops[0]
for i in range(1, len(loops)):
    a, b = lcm, loops[i]
    while b:
        a, b = b, a % b
    lcm = lcm * loops[i] // a

print(lcm)
