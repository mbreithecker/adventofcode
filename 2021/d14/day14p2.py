# part one : decode input
polymer, instructions_string = open('input.txt', 'r').read().split("\n\n")
polymer = polymer.strip()
instructions = dict([tuple(p.strip().split(" -> ")) for p in instructions_string.split("\n")])

# count occurrences of every element
element_counter = dict()
for c in polymer:
    element_counter.setdefault(c, 0)
    element_counter[c] += 1

# count occurrences of every 2-combination
parts_counter = dict()
for i in range(len(polymer)-1):
    code = polymer[i] + polymer[i+1]
    if code in instructions:
        parts_counter.setdefault(code, 0)
        parts_counter[code] += 1

for step in range(40):
    next_counter = dict()
    for code in [c for c in parts_counter.keys() if parts_counter[c] > 0]:
        if code in instructions:
            # transform n*XY -> n*XR
            preCode = code[0] + instructions[code]
            next_counter.setdefault(preCode, 0)
            next_counter[preCode] += parts_counter[code]

            # transform n*XY -> n*RX
            postCode = instructions[code] + code[1]
            next_counter.setdefault(postCode, 0)
            next_counter[postCode] += parts_counter[code]

            # count newly inserted elements
            element_counter.setdefault(instructions[code], 0)
            element_counter[instructions[code]] += parts_counter[code]

            # set occurrences of n*XY to 0 as they all have transformed into new combinations
            parts_counter[code] = 0

    parts_counter = next_counter

print("Part 2: ", (max(element_counter.values()) - min(element_counter.values())))