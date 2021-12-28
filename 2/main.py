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

for row in readFile('C:/Users/Alexandros/Documents/Code/AOC2021/2/input.txt'):
    inputArray.append(row.split(' '))

for row in inputArray:
    match row[0]:
        case 'forward':
            currentX+=int(row[1])
            currentY+=int(row[1])*currentAim
            
        case 'up':
            currentAim-=int(row[1])
        case 'down':
            currentAim+=int(row[1])
        case _:
            print("Can't match value to known cases")


print('X: ' + str(currentX) + ' Y: ' + str(currentY) + ' product: ' + str(currentX*currentY))