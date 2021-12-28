from typing import List
import numpy as np 
import pandas as pd

currentX = 0
currentY = 0
currentAim = 0

inputArray = []


def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words


inputArray = readFile('C:/Users/Alexandros/Documents/Code/AOC2021/3/input.txt')
newInputArray = np.zeros((len(inputArray),len(str(inputArray[0]))))

rowCounter = 0
for row in inputArray:
    for digit in range(len(str(row))):
        newInputArray[rowCounter,digit]=int(str(row)[digit])
    rowCounter+=1

gammaRate = ''
for row in newInputArray.transpose():
    countZero=0
    countOne=0
    for elem in row:
        if elem == 0:
            countZero+=1
        else:
            countOne+=1
    if countZero>countOne:
        gammaRate +='0'
    elif countOne>countZero:
        gammaRate +='1'
    else:
        print('No bueno')

epsilonRate =''

def invertBinary(inputData):
    result = ''
    for digit in range(len(gammaRate)):
        if int(gammaRate[digit]) == 0:
            result+='1'
        else:
            result+='0'
    return result

epsilonRate = invertBinary(gammaRate)
powerConsumption = (int(gammaRate,2)*(int(epsilonRate,2)))
print(powerConsumption)

oxygenRating = []



def filterDownBasedOnPopularity(inputFile,columnNumber):
    inputFile = np.array(inputFile)
    countZero=0
    countOne=0
    outputFile = []
    transposedinput = inputFile.transpose()
    firstColumn = transposedinput[columnNumber]
    a = 1
    for elem in firstColumn:
        if elem == 0:
            countZero+=1
        else:
            countOne+=1
    print('Count zero: ' + str(countZero))
    print('Count one: ' + str(countOne))

    if countZero>countOne:
        for rowProper in newInputArray:
            if rowProper[0] == 0:
                outputFile.append(rowProper)
    elif countOne>countZero:
        for rowProper in newInputArray:
            if rowProper[0] == 1:
                outputFile.append(rowProper)
    elif countOne == countZero:
        print('zeros and ones match, do something')
    return outputFile

oxygenRating = filterDownBasedOnPopularity(newInputArray,0)
oxygenRating = filterDownBasedOnPopularity(oxygenRating,1)
oxygenRating = filterDownBasedOnPopularity(oxygenRating,2)
oxygenRating = filterDownBasedOnPopularity(oxygenRating,3)
oxygenRating = filterDownBasedOnPopularity(oxygenRating,4)
oxygenRating = filterDownBasedOnPopularity(oxygenRating,5)
oxygenRating = filterDownBasedOnPopularity(oxygenRating,6)

#Day 3 part 2. Not done