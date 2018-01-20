#Now write a program that calculates the minimum fixed monthly 
#payment needed in order pay off a credit card balance within 12 months. 

#Assume that the interest is compounded monthly according to the 
#balance at the end of the month (after the payment for that month is made). 
#The monthly payment must be a multiple of $10 and is the same for all months.

#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#
#balance: the outstanding balance on the credit card
#annualInterestRate: annual interest rate as a decimal


def payingDebtOff(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    
    def result(balance, guess):    
        for month in range(12):
            monthlyUnpaidBalance = balance - guess
            balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        return balance
    
    guess = 10
    while result(balance, guess) > 0:
        guess += 10
    
    return print('Lowest Payment: ' + str(guess))

payingDebtOff(balance, annualInterestRate)
