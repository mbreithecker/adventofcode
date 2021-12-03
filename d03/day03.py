# part one
lines = open('input.txt', 'r').readlines()
gammaRate = ""
for pos in range(len(lines[0].strip())):
    oneCount = len([p for p in lines if p[pos] == "1"])
    gammaRate += "1" if 2 * oneCount > len(lines) else "0"

print(int(gammaRate, 2) * int(gammaRate.replace("1", "#").replace("0", "1").replace("#", "0"), 2))

# part two
oxygen = [entry.strip() for entry in open('input.txt', 'r').readlines()]
co2 = [entry for entry in oxygen]
for pos in range(len(oxygen[0])):
    if len(oxygen) != 1:
        oneCount = len([p for p in oxygen if p[pos] == "1"])
        keepNumber = "1" if 2 * oneCount >= len(oxygen) else "0"
        oxygen = [entry for entry in oxygen if (entry[pos] == keepNumber)]

    if len(co2) != 1:
        zeroCount = len([p for p in co2 if p[pos] == "0"])
        keepNumber = "0" if 2 * zeroCount <= len(co2) else "1"
        co2 = [entry for entry in co2 if entry[pos] == keepNumber]

print(int(oxygen[0], 2) * int(co2[0], 2))