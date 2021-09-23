import math
#===========================================================================================================================================
def pythagorasHyp():
    adj = int(input('Adjacent:'))
    opp = int(input('Opposite'))

    hyp = math.sqrt(adj**2 + opp**2)

    print(hyp)

def pythagorasOpp():
    adj = int(input('Adjacent:'))
    hyp = int(input('Hypotenuse'))

    opp = math.sqrt(hyp**2 - adj**2)

    print(opp)

def pythagorasAdj():
    hyp = int(input('Hypotenuse:'))
    opp = int(input('Opposite'))

    adj = math.sqrt(hyp**2 - opp**2)

    print(adj)

#===========================================================================================================================================

import math
def minusB():
    a = (int(input('a:')))
    b = (int(input('b:')))
    c = (int(input('c:')))

    desc = ((b**2) -4*a*c)

    if desc < 0:
        print('No Real Roots')

    if desc == 0:
        x1 = (-b+math.sqrt(b**2-4*a*c))/2*a
        print(('x:'), x1)

    if desc > 0:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        print('x1:', x1)
        print('x2:', x2)
        

