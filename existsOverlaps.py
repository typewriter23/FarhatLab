def existOverlaps(fileName):
    with open(fileName) as f:
        longString = f.read()
        listOfLines = f.split("\n")
        listOfStarts = []
        listOfEnds = []
        firstLine = listOfLines[0].split(" ")
        startCol = next(x for x in firstLine if x == 4174873)
        endCol = next(x for x in firstLine if x == 4178070)
        for line in listOfLines:
            thingsInLine = line.split(" ")
            listOfStarts.append(line[startCol])
            listOfEnds.append(line[endCol])
        startCol.sort()
        endCol.sort()
        
        for i in range(length(startCol)):
            if startCol(i)
            