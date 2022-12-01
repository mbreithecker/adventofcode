# Part 1
counter = 0
for line in open('input.txt', 'r').readlines():
    # iterate output
    for entry in line.split(" | ")[1].split(" "):
        entry = entry.strip()
        # count trivial numbers
        if len(entry) == 2 or len(entry) == 3 or len(entry) == 4 or len(entry) == 7:
            counter += 1

print("Part 1", counter)


# Part 2
solution_sum = 0

for line in open('input.txt', 'r').readlines():
    sequence = sorted(line.split(" | ")[0].split(" "), key=lambda x: len(x))

    solution = dict()  # maps strings to numbers
    mapping = dict()  # maps chars to segments
    n1 = ""  # solution for "1" is unique (len = 2)
    n7 = ""  # solution for "7" is unique (len = 3)
    n4 = ""  # solution for "4" is unique (len = 4)
    n069 = list()  # have length 6
    n235 = list()  # have length 5
    n8 = list()  # unique (len = 7)

    for s in sequence:
        if len(s) == 2: n1 = s
        if len(s) == 3: n7 = s
        if len(s) == 4: n4 = s
        if len(s) == 5: n235.append(s)
        if len(s) == 6: n069.append(s)
        if len(s) == 7: n8 = s

    # map trivial solutions
    solution["1"] = n1
    solution["7"] = n7
    solution["4"] = n4
    solution["8"] = n8

    # Determine remaining

    # {a} = "7" \ "1"
    mapping["a"] = "".join([c for c in n7 if c not in n1])

    # "6" is element of n069 which doesnt contain both segments from "1"
    # determine element c and f
    for elem in n069:
        if len([c for c in n1 if c in elem]) == 1:
            # elem = "6"
            mapping["c"] = "".join([c for c in n1 if c not in elem])
            mapping["f"] = "".join([c for c in n1 if c in elem])
            solution["6"] = elem

    # find "3"
    # It's in 235 and contains "1"
    for elem in n235:
        if len([c for c in n1 if c in elem]) == 2:
            # elem = "3"
            solution["3"] = elem

    # b = {"4"} \ {"3"}
    mapping["b"] = "".join([c for c in solution["4"] if c not in solution["3"]])

    # e = {"8"} \ ({"3"} U {"4"})
    mapping["e"] = "".join([c for c in solution["8"] if c not in (solution["3"]+solution["4"])])

    # {a,b,c,e,f} C "0" and |"0"| = 6
    for elem in n069:
        if len([c for c in ["a","b","c","e","f"] if mapping[c] in elem]) == 5:
            solution["0"] = elem

    # g = "0" \ {a,b,c,e,f}
    mapping["g"] = "".join([c for c in solution["0"] if c not in [mapping["a"],mapping["b"],mapping["c"],mapping["e"],mapping["f"]]])

    # determine remaining 2,5,9
    remaining = [s for s in n069 + n235 if s not in solution.values()]

    # 2 contains e
    solution["2"] = "".join([r for r in remaining if mapping["e"] in r])

    # 9 is the one with length 6
    solution["9"] = "".join([r for r in remaining if len(r) == 6])

    # 5 is the remaining number
    solution["5"] = "".join(r for r in remaining if r not in solution.values())

    # decipher output
    output = line.split(" | ")[1].split(" ")
    out_number = ""
    for entry in output:
        entry = entry.strip()
        for key, val in solution.items():
            if sorted(entry) == sorted(val):
                out_number += key

    solution_sum += int(out_number)


print("Part 2: ", solution_sum)
