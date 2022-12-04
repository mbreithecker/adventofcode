def part1():
    answer = 0
    for rucksack in open("input.txt").read().splitlines():
        # first compartment
        c1 = rucksack[0: len(rucksack)//2]
        # second compartment
        c2 = rucksack[len(rucksack)//2:]
        d = set(c1)
        for c in c2:
            if c in d:
                if c.islower():
                    answer += ord(c) - ord("a") + 1
                else:
                    answer += ord(c) - ord("A") + 27
                break

    print("Part 1:", answer)


def part2():
    answer = 0
    lines = open("input.txt").read().splitlines()
    for i in range(0, len(lines), 3):
        group = [set(lines[i]), set(lines[i + 1]), set(lines[i + 2])]
        d = dict()
        for g in group:
            for e in g:
                if e not in d:
                    d[e] = 0

                d[e] += 1

                if d[e] == 3:
                    if e.islower():
                        answer += ord(e) - ord("a") + 1
                    else:
                        answer += ord(e) - ord("A") + 27
                    break

    print("Part 2:", answer)


part1()
part2()
