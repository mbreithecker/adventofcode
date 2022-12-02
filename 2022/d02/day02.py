def part1():
    score1 = 0
    for g in open("input.txt").read().splitlines():
        # rock: A, X = 1;  paper: B, Y = 2;  scissors: C, Z = 3
        # win = 6, draw = 3, lose = 0
        # CYCLE: (length 3)
        # 1 <- 2 <- 3 <- 1
        opponent, me = g.split(" ")
        # map to {1,2,3}
        me = ord(me) - ord("X") + 1
        opponent = ord(opponent) - ord("A") + 1

        # Calculate win / draw for part 1
        if opponent % 3 == me - 1:
            score1 += 6
        elif me == opponent:
            score1 += 3

        # add base score for part 1
        score1 += me

    print("Part 1: ", score1)


def part2():
    score2 = 0
    for g in open("input.txt").read().splitlines():
        # rock: A, X = 1;  paper: B, Y = 2;  scissors: C, Z = 3
        # win = 6, draw = 3, lose = 0
        # CYCLE: (length 3)
        # 1 <- 2 <- 3 <- 1
        opponent, result = g.split(" ")
        # map to {1,2,3}
        result = ord(result) - ord("X") + 1
        opponent = ord(opponent) - ord("A") + 1

        # result X,1 lose; Y,2 draw, Z,3 win

        # add base score for part 2 (win/draw)
        score2 += (result - 1) * 3

        if result == 2:
            # pick same
            score2 += opponent
        if result == 1:
            # needs to pick previous one ( keep in mind, that rock start at 1 not 0 )
            score2 += (opponent - 1 - 1) % 3 + 1
        if result == 3:
            # needs to pick next one
            # "+1" already "added" as opponent start at 1 not 0
            score2 += opponent % 3 + 1

    print("Part 2: ", score2)


part1()
part2()
