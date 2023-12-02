# load inputs.txt
with open('input.txt', 'r') as f:
    inputs = f.readlines()

games = {}

for input in inputs:
    # split input at :
    split_input = input.split(':')
    # split first part at space
    split_first_part = split_input[0].split(' ')
    configs = split_input[1].split(";")
    cubes = [s.split(",") for s in configs]
    games[split_first_part[-1]] = cubes

# for each game count the number of colors and print the result
counter_p1 = 0
counter_p2 = 0
for game in games:
    color_count = {"red": 0, "green": 0, "blue": 0}
    for config in games[game]:
        for item in config:
            parts = item.split()
            number = int(parts[0])
            color = parts[1]
            color_count[color] = number if number > color_count[color] else color_count[color]
    if color_count["red"] <= 12 and color_count["green"] <= 13 and color_count["blue"] <= 14:
        counter_p1 += int(game)
    counter_p2 += color_count["red"] * color_count["green"] * color_count["blue"]

print("Part 1: ", counter_p1)
print("Part 2: ", counter_p2)