# This is a local compound interest program.
# We give input interest in rupess.
print('Enter per month interest for 100 rupees')
interest_100=input()
print('Enter Amount')
amount=input()
print('Enter number of Years')
years=input()
print('Enter number of Months')
months=input()
for i in range(int(years)):
    yearInterest=(float(amount)/100*float(interest_100))*12
    print('Interest of year ' +str(i)+ ': '+str(yearInterest))
    amount=float(amount)+float(yearInterest)
    print('Total amount of year ' +str(i)+': '+str(amount))
monthsInterest=(float(amount)/100*float(interest_100))*float(months)
totalAmount=float(amount)+float(monthsInterest)
print('Total amount for '+str(years)+ ' years and '+str(months)+' months: '+str(totalAmount))
