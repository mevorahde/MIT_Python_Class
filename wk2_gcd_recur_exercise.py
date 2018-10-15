# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:16:04 2018

@author: David E
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b, a % b)

""" Test Cases:
gcdRecur(51, 3)
gcdRecur(357, 289)
gcdRecur(288, 192)
gcdRecur(40, 30)
gcdRecur(209, 198)
"""