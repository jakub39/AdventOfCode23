file = open("advent23_4.txt", "r").readlines()
total_points = 0 
cards = [1] * len(file)

#part1
for i, line in enumerate(file):
    line = line.strip().split(":")
    nums = line[1].strip().split("|")
    winning_nums = nums[0].split()
    game_nums = nums[1].split()
    win_set = set()
    game_set = set()
    for num in winning_nums:
        if num.isdigit():
            win_set.add(num)
    for num in game_nums:
        if num.isdigit():
            game_set.add(num)

    same_nums = win_set.intersection(game_set)
    points = len(same_nums)

    if points > 0:
        multiplier = 1
        for _ in range(points - 1):
            multiplier *= 2

        total_points += multiplier

#part2
    n = len(same_nums)
    for j in range(i + 1, min(i + 1 + n, len(file))):
        cards[j] += cards[i]

print(total_points)
print(sum(cards))
