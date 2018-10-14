# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:00:51 2018

@author: Owner
"""
annualInterestRate = 0.18
balance = 999999

originalBalance = balance
lower = balance / 12
upper = (balance * (1 + (annualInterestRate/12))**12) / 12


while (balance > 0.001) or (balance < -0.001):
    balance = originalBalance
    rate = (upper + lower) / 2
    for month in range(12):
        balance -= rate
        balance += ((annualInterestRate/12) * balance)
    if balance > 0:
        lower = rate
    elif balance < 0:
        upper = rate


print("Lowest Payment:", round(rate, 2))