# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:56:15 2018

@author: David E
"""
numVowels = 0

s = 'eghjuaforabauruorieoay'

for char in s:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
print('Number of vowels: ' + str(numVowels))