lines = open("input.txt") .read().splitlines()

a = [line[5:].split(": ") for line in lines]

red = 12
green = 13
blue = 14

ids = []
for game in a:
    id = int(game[0])
    series = game[1].split("; ")
    rc, bc, gc = 0,0,0
    for round in series:
        for entries in round.split(", "):
            m = entries.split(" ")
            amount = int(m[0])
            type = m[1]

            if type == "red" and amount > red:
                rc += amount

            if type == "blue" and amount > blue:
                bc += amount

            if type == "green" and amount > green:
                gc += amount

    if rc <= red and bc <= blue and gc <= green:
        ids.append(id)

print((ids))


result = []
for game in a:
    id = int(game[0])
    series = game[1].split("; ")
    rm,bm,gm = 0,0,0
    for round in series:
        for entries in round.split(", "):
            m = entries.split(" ")
            amount = int(m[0])
            type = m[1]

            if type == "red":
                rm = max(rm, amount)

            if type == "blue":
                bm = max(bm, amount)

            if type == "green":
                gm = max(gm, amount)

    result.append(bm*gm*rm)

print(sum(result))