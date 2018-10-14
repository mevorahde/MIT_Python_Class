# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:10:34 2018

@author: Owner
"""

s = 'azcbobobegghakl'

print('Longest substring in alphabetical order is:',
        max([s[i:x] 
            for i in range(len(s)-1) 
                for x in range(i+1, len(s)+1) 
                    if s[i:x] == ''.join(sorted(s[i:x]))], key=len)
            )

        
        