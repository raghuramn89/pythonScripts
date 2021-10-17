# This is a compound interest program of banks.
# Banks calculates interest in percentage.
print('Enter principle amount')
principle=input()
print('Enter per year interest rate in percent. i.e: 5, means 5 percent')
interest_percent=input()
print('Enter number of compounds per year')
compound=input()
print('Enter number of years')
years=input()
interest=float(interest_percent)/100
total_amount=float(principle)*(1+float(interest)/float(compound))**(float(compound)*float(years))
total_interest=float(total_amount)-float(principle)
print('Principle amount: '+str(principle))
print('Interest rate: '+str(interest_percent)+'%')
print('Number of compounds per year: '+str(compound))
print('Number of years '+str(years))
print('Total interest earned for '+str(years)+' years: '+str(total_interest))
print('Total amount '+str(total_amount))
