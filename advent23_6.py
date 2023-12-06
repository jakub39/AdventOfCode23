file = open("advent23_6.txt","r").readlines()

time = file[0].strip().split(": ")[1]
distance = file[1].strip().split(": ")[1]
dist = distance.strip().split(" ")
tim = time.strip().split(" ")
d,t = [], []
for a in dist:
    if a.isdigit():
        d.append(int(a))

for b in tim:
    if b.isdigit():
        t.append(int(b))

nums = []
for i in t:
    counter = 0
    for j in range(int(i)):
        x = (int(i) - j) * j
        if d[t.index(i)] < x:
            counter += 1
    nums.append(counter)

result = 1
for num in nums:
    result *= num

print(result)