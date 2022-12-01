inputArr = "".join(open('input.txt', 'r').readlines()).split("\n\n")

# extend board with columns
fullBoards = []
# add columns as additional rows. The algorithm then just checks for rows via string.replace()
for board in inputArr[1:]:
    newBoard = ""
    columns = [""]*5
    board = board.replace("  ", " ")
    for k in range(5):
        newBoard += " " + board.split("\n")[k] + " " + "\n"
        for i in range(5):
            columns[i] += " " + board.split("\n")[k].strip().split(" ")[i]

    for col in columns:
        newBoard += col + " " + "\n"

    fullBoards.append(newBoard)

winningScore = 0
losingScore = 0
wonBoards = 0

for s in inputArr[0].split(","):
    for i in range(len(fullBoards)):
        # mark numbers (strings) in board
        fullBoards[i] = fullBoards[i].replace(" " + s + " ", " # ")
        # check for win
        if " # # # # # " in fullBoards[i]:
            mySum = 0
            for line in fullBoards[i].split("\n"):
                for number in line.strip().split(" "):
                    if number.strip() != "#" and number.strip() != '':
                        mySum += int(number)

            # remove board
            fullBoards[i] = ""
            # calculate score
            if wonBoards == 0:
                winningScore = int(mySum / 2 * int(s))
            else:
                losingScore = int(mySum / 2 * int(s))

            wonBoards += 1

        # finish when all board are won
        if wonBoards == len(fullBoards):
            print(winningScore)
            print(losingScore)
            exit()
