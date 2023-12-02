lines = open("input.txt") .read().splitlines()
cubes = {"red": 12, "blue": 14, "green": 13}
ids, powers = [], []
for game in [line[5:].split(": ") for line in lines]:
    maxs = {}
    possible = True
    for r in game[1].split("; "):
        for entries in r.split(", "):
            m = entries.split(" ")
            if m[1] not in maxs:
                maxs[m[1]] = 0
            maxs[m[1]] = max(maxs[m[1]], int(m[0]))
            if int(m[0]) > cubes[m[1]]:
                possible = False

    powers.append(maxs["red"] * maxs["green"] * maxs["blue"])
    if possible:
        ids.append(int(game[0]))

print(sum(ids))
print(sum(powers))

