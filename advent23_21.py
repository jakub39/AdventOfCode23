file = open("advent23_21.txt", "r")
test = file.read().split()
xy = ((-1, 0), (0, -1), (1, 0), (0, 1))
for y in range(len(test)):
    if "S" in test[y]:
        x = test[y].index("S")
        posz = {(y, x)}
        break
for i in range(64):
    positions=set()
    for pos in posz:
        for r in xy:
            if test[pos[0]+r[0]][pos[1]+r[1]]!="#":
                positions.add((pos[0]+r[0],pos[1]+r[1]))
        posz=positions
print(len(posz))