# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 23:20:18 2018

@author: David E
"""

epsilion = 0.01
y = 54.0
guess = y/2.0
numGuesses = 0

while abs(guess * guess - y) >= epsilion:
    numGuesses += 1
    guess = guess - (((guess ** 2) - y) / (2 * guess))
print('Number of guesses is: ' + str(numGuesses) + '.')
print('Square root of ' + str(y) + ' is about ' + str(guess) + '.')