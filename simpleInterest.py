#!/usr/bin/python3.8
# Simple local interest. We give input interest in rupees.
print('Enter per month interest for 100 rupees')
interest_100=input()
print('Enter Amount')
amount=input()
print('Enter number of months')
months=input()
month_interest=float(amount)/100*float(interest_100)
print('One month interest is: ' +str(month_interest))
totalInterest=float(month_interest)*int(months)
print('Interest for ' +str(months)+ ' months: '+str(totalInterest))
totalAmount=float(amount)+float(totalInterest)
print('Total amount: ' +str(totalAmount))
