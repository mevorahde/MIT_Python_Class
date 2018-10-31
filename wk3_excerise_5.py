# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:34:18 2018

@author: David E
"""

def applyEachTo(L, x):
    result = []
    for f in L:
        result.append(f(x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

# Question 1
applyEachTo([inc, square, halve, abs], -3)
# Answer: [-2, 9, -1.5, 3]

# Question 2
applyEachTo([inc, square, halve, abs], 3.0)
# Answer: [4.0, 9.0, 1.5, 3.0]

# Question 3
#applyEachTo([inc, max, int], -3)
# Answer: error