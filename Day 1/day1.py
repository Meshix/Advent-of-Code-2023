import os
import re

# load all inputs by line in input.txt
with open('./input.txt') as f:
    my_input = f.readlines()

# Part 1
lines = my_input
lines = ["".join([i for i in line if not i.isalpha()]) for line in lines]
lines = [line.replace('\n', '') for line in lines]
finals = ["".join((line[0], line[-1])) for line in lines]
print(sum([int(line) for line in finals]))

# Part 2
# transform spelled out numbers to integers
lines = my_input
lines = [line.replace('\n', '') for line in lines]

def word_to_number(word):
  return {
      'zero': '0',
      'one': '1',
      'two': '2',
      'three': '3',
      'four': '4',
      'five': '5',
      'six': '6',
      'seven': '7',
      'eight': '8',
      'nine': '9'
  }.get(word, word)

lines = [re.sub(r'(?:zero|one|two|three|four|five|six|seven|eight|nine)', lambda m: word_to_number(m.group(0)), line) for line in lines]

lines = ["".join([i for i in line if not i.isalpha()]) for line in lines]
lines = ["".join((line[0], line[-1])) for line in lines]

print(sum([int(line) for line in lines]))