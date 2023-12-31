# read inputs from file input.txt

with open("input.txt") as file:
    data = file.readlines()

data_split = data[0].split("|")

# Part 1
win_sum = 0
for i in range(0, len(data)):
    counter = 0
    parts = data[i].split("|")
    winning_numbers = parts[0].split(":")[-1]
    winning_numbers_int = [int(i) for i in winning_numbers.split(" ") if i != ""]
    numbers = parts[1].split(" ")
    numbers_int = [int(i) for i in numbers if i.strip().isnumeric()]
    for x in numbers_int:
        if x in winning_numbers_int:
            counter += 1
    if counter > 1:
        win_sum += 2**(counter-1)
    elif counter == 1:
        win_sum += 1
print("Part 1: " + str(win_sum))

# Part 2
cards = {}
for i in range(0, len(data)):
    cards[i+1] = 1
i = 1
for i in range(1, len(data)):
    counter = 0
    parts = data[i-1].split("|")
    winning_numbers = parts[0].split(":")[-1]
    game = int(parts[0].split(":")[0].split(" ")[-1])
    winning_numbers_int = [int(i) for i in winning_numbers.split(" ") if i != ""]
    numbers = parts[1].split(" ")
    numbers_int = [int(i) for i in numbers if i.strip().isnumeric()]

    for x in numbers_int:
        if x in winning_numbers_int:
            counter += 1

    if counter > 1:
        for x in range(1, counter+1):
            cards[game+x] += cards[game]
    elif counter == 1:
        cards[game+1] += cards[game]

# print the sum of the values in the dictionary
print("Part 2: " + str(sum(cards.values())))    