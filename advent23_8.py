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