#import modules
import math

#def intrestRate
def intrestRate():

    #read inputs
    rate1, rate2, amount1, initAmount0 = map(float, input('Read rate1 rate2 amount1 initAmount').split())
    if initAmount0<amount1:

        #calculate intrestYr1
        intrestYr1=(initAmount0*rate1)

        #print intrestYr1
        print('intrestYr1=',intrestYr1)
    #endif

    if initAmount0>amount1:

        #calculate intrestYr1
        intrestYr1=(initAmount0*rate2)

        #print intrestYr1
        print('intrestYr1=', intrestYr1)
    #endif

        #calculate out_amountYr1
        out_amountYr1=(intrestYr1+initAmount0)

        #print out_amountYr1
        print('out_amountYr1=', out_amountYr1)


    if out_amountYr1<amount1:
        
        #calculate intrestYr2
        intrestYr2=(out_amountYr1*rate1)

        #print intrestYr2
        print('intrestYr2=',intrestYr2)
    #endif

    if out_amountYr1>amount1:
        
        #calculate intrestYr2
        intrestYr2=(out_amountYr1*rate2)

        #print intrestYr2
        print('intrestYr2=',intrestYr2)
    #endif

        #calculate out_amountYr2
        out_amountYr2=(intrestYr2+out_amountYr1)

        #print out_amountYr2
        print('out_amountYr2=', out_amountYr2)

#end intrestRate
        
        

        
    
