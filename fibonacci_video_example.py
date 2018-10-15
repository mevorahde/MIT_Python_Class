# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:43:29 2018

@author: David E
"""

def fib(x):
    """assumes x an int >=0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else: 
        return fib(x - 1) + fib(x - 2)