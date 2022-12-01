import re

#part one
depth = 0
position = 0
for line in open('input.txt', 'r').readlines():
    for (command, value) in re.findall(re.compile(r'([a-z]*) ([0-9]+)'), line):
        if command == "up": depth -= int(value)
        if command == "down": depth += int(value)
        if command == "forward": position += int(value)

print(depth, position, depth * position)

#part two
depth = 0
position = 0
aim = 0
for line in open('input.txt', 'r').readlines():
    for (command, value) in re.findall(re.compile(r'([a-z]*) ([0-9]+)'), line):
        if command == "up": aim -= int(value)
        if command == "down": aim += int(value)
        if command == "forward":
            position += int(value)
            depth += int(value)*aim

print(depth, position, depth * position)
