# import modules
import math
import cmath

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
    elif b**2-4*a*c==0 :
      #calculate x1 nd x2
      print('Equation with real and equal solutions')
      x1 = x2 = -b / (2*a)

      # print x1, x2
      print ('x1 = x2 =', x1)
    elif b**2-4*a*c<0:
        
        #calculate x1, x2
        print ('Eqution with complex solutions')
        x1=(-b + cmath.sqrt(b**2-4*a*c))/(2*a)
        x2=(-b - cmath.sqrt(b**2-4*a*c))/(2*a)
   
        #print x1, x2
        print('x1 = ',(x1))
        print('x2 = ',(x2))
   #endif
    
# end solveEquation
