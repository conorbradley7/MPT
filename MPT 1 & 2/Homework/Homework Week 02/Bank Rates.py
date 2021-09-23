# import modules
import math

# define functions

def investRate():

    # read inputs
    rate1 = float(input('Rate 1='))
    rate2 = float(input('Rate 2='))
    amount1 = float(input('Amount 1='))
    initAmount = float(input('initAmount='))
    if initAmount<amount1 :

        #calculate Profit
        Profit=(rate1*initAmount)

        #printProfit
        print('Profit=')
    else :
        # calculate Profit
        Profit=(rate2*initAmount)

        #printProfit
        print('Profit=')

# end investRate
        

    
    
