# import modules
import math

#def solveEquation
def solveEquation():
    '''
        solveEquation is to solve quadratic equation.
        this always has 2 roots given by
        x1 =... and x2 = ...
    '''
    # input a, b, c
    a= float(input('a='))
    b= float(input('b='))
    c= float(input('b='))
    if b**2-4*a*c>=0 :

        #calculate x1, x2
        x1=(-b + math.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b - math.sqrt(b**2-4*a*c))/(2*a)
   
        #print x1, x2
        print('x1 = ', round(x1,2))
        print('x2 = ', round(x2,2))
    else :
        # equation with complex roots
        print('equation does not have real roots')
    
# end solveEquation
