# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:58:49 2018

@author: David E
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    if len(aStr) == 1:
      return aStr == char
    if char == aStr[int(len(aStr) // 2)]:
        return True
    else:
        if len(aStr) < 2:
            return False
        elif char > aStr[(len(aStr) // 2)]:
            return isIn(char, aStr[(len(aStr) // 2): ])
        elif char < aStr[(len(aStr) // 2)]:
            return isIn(char, aStr[ :(len(aStr) // 2)])
        else:
            return False
    
print(isIn('a', ''))
print(isIn('r', 'jmmrsvwy'))
print(isIn('t', 'dfhhjllmppqrvxxyzz'))
print(isIn('i', 'jknpx'))
print(isIn('x', 'acdikklmmnopqrsuxyy'))
print(isIn('b', 'abbcilrz'))