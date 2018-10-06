# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 20:48:14 2018

@author: David E
"""

cube = 25
epsilion = 0.01
guess = 0.0
increment = 0.1
num_guesses = 0
while abs(guess**3 - cube) >= epsilion and guess <= cube:
    guess += increment
    num_guesses += 1
print('Number of guesses is: ', num_guesses)
if abs(guess**3 - cube) >= epsilion:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of ', cube)
    
# try with cube = 27, and a large step (e.g. 2.0)
    