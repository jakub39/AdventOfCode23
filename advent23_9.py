file = open("advent23_9.txt", "r").read().splitlines()

def process_line(line):
    if all(x == 0 for x in line):
        return 0
    else:       
        differences = [y - x for x, y in zip(line, line[1:])]
        return line[0] - process_line(differences) #part 1 iba zmenit riadok: return line[-1] + process_line(differences)

lines = [list(map(int, line.split())) for line in file]

result = sum([process_line(line) for line in lines])

print(result)