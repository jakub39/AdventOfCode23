with open("advent23_13.txt", "r") as file:
    content = file.read().strip()
    grid_list = [grid.split("\n") for grid in content.split("\n\n")]

total_score = [0, 0]

for original_grid in grid_list:
    for current_grid, multiplier in [(original_grid, 100), (list(zip(*original_grid)), 1)]:
        for y in range(1, len(current_grid)):
            differences = sum(sum(a != b for a, b in zip(current_grid[y - j - 1], current_grid[y + j]))for j in range(min(y, len(current_grid) - y))
            )
            if differences < 2:
                total_score[differences] += multiplier * y

print(total_score)
    