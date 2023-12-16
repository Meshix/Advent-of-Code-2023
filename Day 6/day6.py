with open("input.txt") as file:
    data = file.readlines()

# in each line extract all the numbers
# Splitting the strings and extracting numbers
time_values = [int(val) for val in data[0].split() if val.isdigit()]
distance_values = [int(val) for val in data[1].split() if val.isdigit()]

# for each key in the dictionary, calculate all products n * 0, n-1 * 1, n-2 * 2, ... 0 * n
# and store the results in a list
solutions = []
for i, time in enumerate(time_values):
    products = []
    for j in range(time):
        product = j * (time - j)
        if product >= distance_values[i]:
            products.append(i * (time - i))
    solutions.append(products)

# print the length of each sublist in the list
product = 1
for solution in solutions:
    product *= len(solution)
print("Part 1: ", product)

# Part 2
times = [x for x in data[0] if x.isdigit()]
# join the numbers into a string
times = int("".join(times))
print(times)
distances = [x for x in data[1] if x.isdigit()]
distances = int("".join(distances))
print(distances)

products = []
for i in range(times):
    product = i * (times - i)
    if product >= distances:
        products.append(i * (times - i))

print("Part 2: ", len(products))
