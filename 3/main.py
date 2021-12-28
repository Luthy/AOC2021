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
        gammaRate +=str(0)
    elif countOne>countZero:
        gammaRate +=str(1)
    else:
        print('No bueno')


epsilonRate =''
for digit in range(len(gammaRate)):
    if int(gammaRate[digit]) == 0:
        epsilonRate+='1'
    else:
        epsilonRate+='0'


print((int(gammaRate,2)*(int(epsilonRate,2))))
