# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 21:24:52 2018

@author: David E
"""

x = 27
epsilon = 0.01
numGusses = 0
low = 0.0
high = x
ans = (high + low)/2.0

while abs(ans **3 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGusses += 1
    if ans ** 3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('Number of guesses is ' + str(numGusses))
print(str(ans) + ' is close to the square root of ' + str(x))