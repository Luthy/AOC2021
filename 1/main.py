from typing import List
import numpy as np 
import pandas as pd

inputArray = []

def readFile(fileName):
        fileObj = open(fileName, "r") #opens the file in read mode
        words = fileObj.read().splitlines() #puts the file into an array
        fileObj.close()
        return words

for row in readFile('C:/Users/Alexandros/Documents/Code/AOC2021/1/input.txt'):
    inputArray.append(int(row))


def countAmountOfDepthIncreases(inputData):
    rowCounter = 0
    higherThanLastCounter = 0   
    for row in inputData:
        if rowCounter>0 and row > lastRow:
            higherThanLastCounter+=1
        lastRow = row
        rowCounter+=1

    print(higherThanLastCounter)

rowCounter = 0
threePeriodAverage = []
for row in inputArray:
    if rowCounter > 1:
        threePeriodAverage.append((inputArray[rowCounter]+inputArray[rowCounter-1]+inputArray[rowCounter-2])/3)
    rowCounter+=1

countAmountOfDepthIncreases(threePeriodAverage)
