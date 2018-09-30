# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:15:44 2018

@author: David E
"""
numBobs = 0

s = 'azcbobobegghakl'

for word in s[1:100]:
    if word == 'bob':
        numBobs += 1
print('Number of times bob occurs is: ' + str(numBobs))