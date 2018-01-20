balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
	      

def balanceAfterAYear(balance, annualInterestRate, monthlyPaymentRate):
    monthlyInterestRate = annualInterestRate / 12.0
    
    for month in range(12):
        minimumPayment = balance * monthlyPaymentRate
        unpaidBalance = balance - minimumPayment
        interest = unpaidBalance * monthlyInterestRate
        balance = unpaidBalance + interest
    print (round(balance, 2))
    
balanceAfterAYear(balance, annualInterestRate, monthlyPaymentRate)
