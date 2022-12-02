score1, score2 = 0, 0
for g in open("input.txt").read().splitlines():
    o, m = g.split(" ")
    score1 += ((ord(m) - 22 - ord(o)) % 3) * 3 + ord(m) - 87
    score2 += (ord(m) - 87 - 1) * 3
    score2 += ord(o) - 64 if ord(m) - 87 == 2 else (ord(o) + 20 + ord(m)) % 3 + 1

print("Part 1: ", score1, 13682)
print("Part 2': ", score2, 12881)
