lines = open("input.txt").read().splitlines()
d = [[c for c in line if c.isdigit()] for line in lines]
print(sum([int(x[0] + x[-1]) for x in d]))
def getFirst(line, reverse = False):
    r = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for k in range(len(line)):
        i = k if not reverse else len(line) - 1 - k
        for key in r.keys():
            if line[i:].startswith(key):
                return r[key]
        if line[i].isdigit():
            return line[i]

print(sum([int(getFirst(line) + getFirst(line, True)) for line in lines]))
