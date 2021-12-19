# part one : decode input
polymer, instructions_string = open('input.txt', 'r').read().split("\n\n")
polymer = polymer.strip()
instructions = dict([tuple(p.strip().split(" -> ")) for p in instructions_string.split("\n")])

# evolve polymer
for step in range(10):
    next_polymer = ""
    for i in range(len(polymer)-1):
        next_polymer += polymer[i]
        if polymer[i] + polymer[i+1] in instructions:
            next_polymer += instructions[polymer[i]+polymer[i+1]]

    polymer = next_polymer + polymer[-1]

# count elements:
counter = dict()
for c in polymer:
    counter.setdefault(c, 0)
    counter[c] += 1

print("Part 1: ", (max(counter.values()) - min(counter.values())))

# Solution is too slow for part two. Maybe one should use dynamic programming (?). There are indeed repeating patterns in the string
