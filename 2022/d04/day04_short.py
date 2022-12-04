p1, p2 = 0, 0
for g in open("input.txt").read().splitlines():
    a1, a2, b1, b2 = [int(e) for x in g.split(",") for e in x.split("-")]
    s1 = set(range(a1, a2 + 1))
    s2 = set(range(b1, b2 + 1))
    p1 += len(s1 & s2) == min(len(s1), len(s2))
    p2 += len(s1 & s2) > 0

print("p1: ", p1)
print("p2: ", p2)
