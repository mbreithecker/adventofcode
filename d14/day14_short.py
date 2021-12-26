# decode input
polymer, instructions_string = open('input.txt', 'r').read().split("\n\n")
polymer = polymer.strip()
instructions = dict([tuple(p.strip().split(" -> ")) for p in instructions_string.split("\n")])

# count occurrences of every element
element_counter = {s: len([c for c in polymer if c == s]) for s in set(instructions.values()).union(set(polymer))}
parts_counter = {code:polymer.count(code) for code in instructions}

for step in range(40):
    next_counter = dict()
    for code in [c for c in parts_counter.keys() if parts_counter[c] > 0 and c in instructions]:
        # transform n*XY -> n*XR
        preCode = code[0] + instructions[code]
        next_counter.setdefault(preCode, 0)
        next_counter[preCode] += parts_counter[code]

        # transform n*XY -> n*RX
        postCode = instructions[code] + code[1]
        next_counter.setdefault(postCode, 0)
        next_counter[postCode] += parts_counter[code]

        # count newly inserted elements
        element_counter[instructions[code]] += parts_counter[code]

    parts_counter = next_counter
    if step == 9: print("Part 1: ", (max(element_counter.values()) - min(element_counter.values())))

print("Part 2: ", (max(element_counter.values()) - min(element_counter.values())))