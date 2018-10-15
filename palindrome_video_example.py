# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:46:51 2018

@author: David E
"""

def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(toChars(s))

print("")
print('Is ever a palindrome?')
print(isPalindrome('eve'))

print("")
print('Is ever a palindrome?')
print(isPalindrome('Able was I, ere I saw Elba'))