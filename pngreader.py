import png, sys


def main():
    if len(sys.argv) == 1:
        print("Please provide a png file")
    elif len(sys.argv) < 4:
        inputFile = sys.argv[1]
        inF = open(inputFile, 'rb')
        r = png.Reader(inF)
        outputFile = 'out.txt'
        if len(sys.argv) == 3:
            outputFile = sys.argv[2]
        outF = open(outputFile, 'w')
        values = readFile(r)
        outF.write(values)
    else:
        print("Too many arguments")


def toHex(rgb):
    s = str(hex(rgb))[2:].upper()
    if len(s) < 2:
        s = "0" + s
    return s


def readFile(r):
    readerObj = r.read()
    arrayObjList = list(readerObj[2])
    allValues = ""
    for i in range(0,len(arrayObjList)):
        arrayObj = arrayObjList[i]
        rowRGBValues = arrayObj.tolist()
        j = 0
        for j in range(0,len(rowRGBValues),4):
            string = ""
            r = toHex(rowRGBValues[j])
            g = toHex(rowRGBValues[j+1])
            b = toHex(rowRGBValues[j+2])
            a = toHex(rowRGBValues[j+3])
            # string = r + " " + g + " " + b + " " + a + "\n"
            string = r + g + b + a + "\n"
            allValues = allValues + string
    return allValues


main()