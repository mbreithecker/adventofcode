lines = open("input.txt").read().splitlines()

s = 0
for line in lines:
    num = ""
    for c in line:
        try:
            _ = int(c)
            num += c
            break
        except:
            pass

    for c in line[::-1]:
        try:
            _ = int(c)
            num += c
            break
        except:
            pass
    s += int(num)

print(s)


s = 0
for line in lines:
    num = ""
    for i in range(len(line)):
        c = line[i]
        a = line[i:]
        if a.startswith("one"):
            num += "1"
            break
        if a.startswith("two"):
            num += "2"
            break
        if a.startswith("three"):
            num += "3"
            break
        if a.startswith("four"):
            num += "4"
            break
        if a.startswith("five"):
            num += "5"
            break
        if a.startswith("six"):
            num += "6"
            break
        if a.startswith("seven"):
            num += "7"
            break
        if a.startswith("eight"):
            num += "8"
            break
        if a.startswith("nine"):
            num += "9"
            break
        try:
            _ = int(c)
            num += c
            break
        except:
            pass

    for k in range(len(line)):
        i = len(line)-1-k
        c = line[i]
        a = line[i:]
        if a.startswith("one"):
            num += "1"
            break
        if a.startswith("two"):
            num += "2"
            break
        if a.startswith("three"):
            num += "3"
            break
        if a.startswith("four"):
            num += "4"
            break
        if a.startswith("five"):
            num += "5"
            break
        if a.startswith("six"):
            num += "6"
            break
        if a.startswith("seven"):
            num += "7"
            break
        if a.startswith("eight"):
            num += "8"
            break
        if a.startswith("nine"):
            num += "9"
            break
        try:
            _ = int(c)
            num += c
            break
        except:
            pass

    s += int(num)

print(s)
