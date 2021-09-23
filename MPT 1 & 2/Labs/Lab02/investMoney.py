# import modules
import math

# define functions

def investMoney():
    
    #read inputs
    amount0 = float(input('Amount to invest: '))
    rate = float(input('Invest Rate: '))

    # Year 1 profit and amount
    profit1 = amount0 * rate
     amount1= amount0 + profit1
    print('Year 1: ', profit1, amount1)

    # Year 2 proft and amount
    profit2 = amount1 * rate
    amount2 = amount1 + profit2
    print('Year 2: ', profit2, amount2)

    # Year 3 profit and amount
    profit3 = amount2 * rate
    amount3 = amount2 + profit3
    print('Year 3: ', profit3, amount3)

# end investMoney
