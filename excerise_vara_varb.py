# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 00:00:40 2018

@author: Owner
"""

varA = 'bonjour'
varB = 'bonjour'

if type(varA) is str or type(varB) is str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
elif varA < varB:
    print('smaller')