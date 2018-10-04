# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:34:21 2018

@author: Owner
"""

# A Pig Latin translator

#Imports and Variables
import re
pyg = 'ay'
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
original = input('Enter a word: ')

####Program######
# Checks if the user has entered a string and no special characters
def translator():
    if len(original) > 0 and original.isalpha() and (regex.search(original) == None):
        word = original.lower()
        first = word[0]
        new_word = word + first + pyg
        new_word = new_word[1:len(new_word)]
        print("In Pig Latin, " + word + " is: " + new_word)
# Validation for when the user enters a numeric value
    elif original.isnumeric():
        print("You enetered a number, please enter a word.")
# Validation for when the user enters any special characters
    elif not(regex.search(original) == None):
        print("You enetered a special character, please enter a word.")
# Validtion when the user does not enter anything.
    else:
        print("You didn't eneter anything, please enter a word.")
        
translator()

