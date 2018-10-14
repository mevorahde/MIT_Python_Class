# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:14:01 2018

@author: Owner
"""
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthInterestRate = annualInterestRate/12

for i in range(1,13):

    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    updatedBalance = monthlyUnpaidBalance + monthInterestRate * monthlyUnpaidBalance
    balance = updatedBalance

print("Remaining balance:" + str(round(updatedBalance, 2)))