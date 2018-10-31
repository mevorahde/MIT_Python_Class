# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:26:43 2018

@author: David E
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
testList = [1, -4, 8, -9]

# Question 1
applyToEach(testList, abs)
print(testList)

# Question 2
def addOne(x):
    return x + 1
applyToEach(testList, addOne)
print(testList)

# Question 3
def squareNum(x):
    return x ** 2

applyToEach(testList, squareNum)
print(testList)
