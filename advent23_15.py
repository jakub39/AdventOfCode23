file = open("advent23_15.txt", "r").read().split(",")

result = 0

for part in file:
    current_value = 0
    for char in part:
        current_value += ord(char)
        current_value = (current_value * 17) % 256 
    result += current_value

print(result)