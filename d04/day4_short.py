inputArr = "".join(open('input.txt', 'r').readlines()).split("\n\n")

fullBoards = []
for board in inputArr[1:]:
    board_arr = [""]*(5*2)
    board = board.replace("  ", " ")
    for k in range(5):
        board_arr[k] = " " + board.split("\n")[k]
        for i in range(5):
            board_arr[k+i] += " " + board.split("\n")[k].strip().split(" ")[i]

    fullBoards.append(" \n".join(board_arr))

winningScore = 0
losingScore = 0
for s in inputArr[0].split(","):
    for i in range(len(fullBoards)):
        fullBoards[i] = fullBoards[i].replace(" " + s + " ", " # ")
        if " # # # # # " in fullBoards[i]:
            remainingSum = sum([int(x) if x.strip() != "#" and x.strip() != '' else 0 for line in fullBoards[i].split("\n") for x in line.strip().split(" ")])
            fullBoards[i] = ""
            if winningScore != 0:
                winningScore = int(remainingSum / 2 * int(s))

            losingScore = int(remainingSum / 2 * int(s))

print("Part 1: ", winningScore, "   Part 2: ", losingScore)
