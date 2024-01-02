file = open("advent23_12.txt", "r").readlines()
result = 0

for line in file:
    line = line.strip().split(" ")
    springs = line[0]
    numbers = line[1].split(",")

    condition = "."
    for nr in numbers:
        for i in range(int(nr)):
            condition += "#"
        condition += "."

    conditions_dict = {0: 1}
    dict2 = {}
    for char in springs:
        for condt in conditions_dict:
            if char == "?":
                if condt + 1 < len(condition):
                    dict2[condt + 1] = dict2.get(condt + 1, 0) + conditions_dict[condt]
                if condition[condt] == ".":
                    dict2[condt] = dict2.get(condt, 0) + conditions_dict[condt]

            elif char == ".":
                if condt + 1 < len(condition) and condition[condt + 1] == ".":
                    dict2[condt + 1] = dict2.get(condt + 1, 0) + conditions_dict[condt]
                if condition[condt] == ".":
                    dict2[condt] = dict2.get(condt, 0) + conditions_dict[condt]

            elif char == "#":
                if condt + 1 < len(condition) and condition[condt + 1] == "#":  
                    dict2[condt + 1] = dict2.get(condt + 1, 0) + conditions_dict[condt]

        conditions_dict = dict2
        dict2 = {}

    result += conditions_dict.get(len(condition) - 1, 0) + conditions_dict.get(len(condition) - 2, 0)

print(result)

