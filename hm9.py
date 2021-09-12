import random
def randomNumberInFile(Number):
    f=open("HomeFile.txt", "w")
    numinLine = 0
    for i in range(Number):
        if numinLine>=10:
            f.write("\n")
            numinLine = 0
        f.write(str(random.randint(0, 10)) + " ")
        numinLine += 1
    f.write("\n")
    f.close()


def squareOfNumberInFile(countOfLine):
    f=open("HomeFile.txt", "r+")
    lines=f.readlines()
    cp = 0
    for line in lines:
        numbers=line.split()
        cp += len(line)
        for n in numbers:
            f.seek(0, 2)
            f.write(str(int(n) ** 2) + " ")
        f.write("\n")
        f.seek(cp)
    f.seek(0, 2)
    f.close()
randomNumberInFile(1000)
squareOfNumberInFile(100)