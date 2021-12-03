#part one
lines = open('input.txt', 'r').readlines()
print(sum([int(p.split(" ")[1]) for p in lines if p.split(" ")[0] == "forward"])
      * (sum([int(p.split(" ")[1]) for p in lines if p.split(" ")[0] == "down"]) - sum([int(p.split(" ")[1]) for p in lines if p.split(" ")[0] == "up"]))    )

#part two
depth = 0; position = 0; aim = 0
for line in open('input.txt', 'r').readlines():
    command, value = line.split(" ")
    if command == "up": aim -= int(value)
    if command == "down": aim += int(value)
    if command == "forward":
        position += int(value)
        depth += int(value)*aim

print(depth * position)
