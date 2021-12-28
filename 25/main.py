from typing import List
import numpy as np 
import pandas as pd

totalMoves = 0
listoflists = []

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

def horizontalMove(inputX,variableToCheck):
    global totalMoves 
    y = np.array(inputX, copy=True) 

    'first move horizonally'
    rowCounter = 0

    for row in inputX:
        
        columnCounter = 0
        for elem in row:
            positionX = rowCounter
            positionY = columnCounter

            nextValue = 666
            nextX = 666
            nextY = 666
            
            if columnCounter != (row.size-1):
                'check next element'
                nextX = positionX
                nextY = positionY+1
                nextValue = inputX[nextX][nextY]

            else:
                'check first element'
                nextX = positionX
                nextY = 0
                nextValue = inputX[nextX][nextY]

            if nextValue == 0 and elem == variableToCheck:
                y[nextX][nextY] = variableToCheck
                y[positionX][positionY] = 0
                totalMoves+=1
            columnCounter+=1

        rowCounter+=1
    
    
    return y

def verticalMove(inputX):
    transposedX = inputX.transpose()
    return horizontalMove(transposedX,2).transpose()

for row in readFile('input.txt'):
    elemCounter = 0
    myList = np.array([])
    for elem in row:
        myList = np.append(myList, int(elem))
        elemCounter+=1
    listoflists.append(myList)

inputFile = listoflists

count = 1 #Starts at 1 to match the exercise result
numIter = 10000

while count < numIter:
    
    inputFile = horizontalMove(inputFile,1)
    inputFile = verticalMove(inputFile)
    print('Total Moves: ' + str(totalMoves) + ' Iteration: ' + str(count))
    
    if totalMoves == 0:
        break
    totalMoves = 0
    count = count + 1


print('Finished')