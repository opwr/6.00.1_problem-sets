epsilon = 0.001

def payingDebtOff(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    
    lowerBound = balance / 12
    upperBound = (balance * ((1 + monthlyInterestRate)**12)) / 12
    guess = (lowerBound + upperBound) / 2

    def result(balance, guess):    
        for month in range(12):
            monthlyUnpaidBalance = balance - guess
            balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance
        return balance
           
    while True:
        if result(balance, guess) <= 0 and abs(result(balance, guess)) <= epsilon:
            break
        elif result(balance, guess) > 0:
            lowerBound = guess
            guess = (lowerBound + upperBound) / 2
        else:
            upperBound = guess
            guess = (lowerBound + upperBound) / 2

    return print('Lowest Payment: ' + str(round(guess, 2)))
    
payingDebtOff(balance, annualInterestRate)
 
