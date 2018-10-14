# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:10:23 2018

@author: Owner
"""
balance = 4773
annualInterestRate = 0.2

minFixedPayment = round(balance//13, -1)

def payCardOff(balance, annualInterestRate, minFixedPayment): 
    monthlyInterestRate = annualInterestRate/12.0   
    unpaidBal = balance

    for i in range (12):
        unpaidBal = unpaidBal - minFixedPayment
        increase = monthlyInterestRate * unpaidBal
        unpaidBal = unpaidBal + increase

    if unpaidBal <= 0:
        return minFixedPayment
    else:
        minFixedPayment += 10
        unpaidBal = balance
        return payCardOff(unpaidBal, annualInterestRate, minFixedPayment)

min = payCardOff(balance, annualInterestRate, minFixedPayment)
print (min)