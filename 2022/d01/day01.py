with open("input.txt") as infile:
    c = [sum([int(y) for y in x.split("\n")]) for x in "".join(infile.readlines()).split("\n\n")]
    print(max(c))  # 72602
    print(sum(sorted(c)[-3:]))  # 207410
