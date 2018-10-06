# -*- coding: utf-8 -*-
"""
Guessing Game Excerise
Created on Fri Oct  5 21:33:39 2018

@author: David E
"""
# variables for the low, mid, and high numbers of the guessing game of 0-100.
low = 0
mid = 50
high = 100
# variable for the number of guess attepts
numGusses = 0

################Start of Program####################
# User is asked to think of a number between 0 and 100
print("Please think of a number between 0 and 100!")   
# Computer asks the user if the first guess of a number is correct.     
print ("Is your secret number: " + str(mid) + "?")
# Computer asks the user if the number is too high, too low, or if it's the correct number.
key = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
while key != 'c':
    # For each attempt that the computer is not correct, add 1 to the guess counter
    numGusses += 1
    # if the user enter 'h', the guess was too high
    if key == 'h':
        high = mid
        mid = int((mid + low)/2)
    # if the user enter 'l', the guess was too low
    elif key == 'l':
        low = mid
        mid = int((mid + high)/2)
    # if anything other than 'h', 'l', or 'c' is entered.
    else:
        print("Invalid input.")
    # show the last guess attempt
    print ("Is your secret number: " + str(mid) + "?")
    key = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
if key == 'c':
    # The computer guess the user's number, along with some suddle trash talk.
    print ("Game over. Your secret number was:" + str(mid) + "!")
    print("It took me, the smart computer: " + str(numGusses) + " guesses.")
    print("Make it more difficult on me next time, will ya.")