# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 22:51:04 2018

@author: David E
"""
num = 19

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result  = ''

if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2
if isNeg:
    result = '-' + result
    
print(result)