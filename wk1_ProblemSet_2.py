# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 18:15:44 2018

@author: David E
"""
numBobs = 0
s = 'azcbobobegghakl'

for word in s:
    if "bob" in word[0:25]:
        print("success")
        numBobs += 1
print('Number of times bob occurs is: ' + str(numBobs))