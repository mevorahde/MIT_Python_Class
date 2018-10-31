# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 20:10:22 2018

@author: David E
"""

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
        
L = [1, -2, 3.4]  
      
applyToEach(L, abs)
print(L)

applyToEach(L, int)
print(L)

