#import modules
import math

def investMoney():
    '''
    Pyton program to invest money over some years.
    Inputs: amount, nrYears
    Output: amount, profit and cummulated amount for each year
    How to do it:
         repeat for each year
           calculate profit and cummulated amount print them
           ???about next year amount?
    '''
    #inputs
    amount= float(input('Initial Amount'))
    rate = float(input('Invest Rate'))
    nrYears = int(input('Nr of Years'))

    # repeat calculation
    for i in range(nrYears):
        # calculate profit, cummulate amount
        profit = amount*rate
        newAmount = amount+profit

        print('Year:', i,)
        print('Amount', round(amount,2))
        print('Profit', round(profit,2))
        print('New Amount', round(newAmount,2))
        print(' ')
        
        # prepare calculation for next year
        amount = newAmount
    #end for
# end investMoney
 
