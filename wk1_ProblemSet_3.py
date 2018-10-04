# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:10:34 2018

@author: Owner
"""

s = 'azcbobobegghakl'

for i in range (1,len(s)):

    if (s[i-1] <= s[i]):
        #print(s[i:i-1])
        print("Longest substring in alphabetical order is:", s)
    else:
        print("Longest substring in alphabetical order is:", s[i-1])

        
        