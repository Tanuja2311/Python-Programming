# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:51:41 2019

@author: tanuj
"""

inputFile = "D:\\_MCA\\$Sem 5\\Python\\File Handling\\class_scores.txt"
outputFile = "D:\\_MCA\\$Sem 5\\Python\\File Handling\\new_scores.txt"

def addScore(n):
    n += 5
    return n

fileRead = open(inputFile,'r')
fileWrite = open(outputFile,'a')


for i in fileRead:
    uname,score = i.split(' ')
    score = addScore(int(score))
    print(uname,' ',score,file=fileWrite)

fileRead.close()
fileWrite.close()