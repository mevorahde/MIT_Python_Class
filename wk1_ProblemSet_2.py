# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:15:44 2018

@author: David E
"""
numBobs = 0
s = 'azcbobobegghakl'


for i in range(len(s)):
    if s[i:i+3] == 'bob':
        numBobs += 1    
print('Number of times bob occurs is: ' + str(numBobs)) 