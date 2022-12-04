p1, p2 = 0, 0
for g in open("input.txt").read().splitlines():
    range1, range2 = g.split(",")
    set1 = set(list(range(int(range1.split("-")[0]), int(range1.split("-")[1]) + 1)))
    set2 = set(list(range(int(range2.split("-")[0]), int(range2.split("-")[1]) + 1)))

    if len(set1.intersection(set2)) == min(len(set1), len(set2)):
        p1 += 1
    if len(set1.intersection(set2)) > 0:
        p2 += 1

print("Part 1: ", p1)
print("Part 2: ", p2)