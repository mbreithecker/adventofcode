import re


def readInput():
    puzzle, moves = open("input.txt").read().split("\n\n")
    stacks = []

    # parse initial configuration into list of stacks
    for line in puzzle.split("\n")[-2::-1]:
        col = 0
        for value in re.findall(re.compile(r'(\[[A-Z]\]|   ) '), line + " "):
            if len(stacks) == col:
                stacks.append(list())
            if value != "   ":
                stacks[col].append(value[1:-1])
            col += 1

    return stacks, moves


# parse and perform commands
def part1():
    stacks, moves = readInput()
    for amount, org, dest in re.findall(re.compile(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)\n'), moves + "\n"):
        for i in range(0, int(amount)):
            stacks[int(dest) - 1].append(stacks[int(org) - 1].pop())
    return "".join([s[-1] for s in stacks])


def part2():
    stacks, moves = readInput()
    for amount, org, dest in re.findall(re.compile(r'move ([0-9]+) from ([0-9]+) to ([0-9]+)\n'), moves + "\n"):
        bulk = []
        for i in range(0, int(amount)):
            bulk.append(stacks[int(org) - 1].pop())
        stacks[int(dest) - 1].extend(bulk[::-1])
    return "".join([s[-1] for s in stacks])


print("Part1:", part1())
print("Part2:", part2())
