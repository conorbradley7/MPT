#Pythagoras=================================================================================================================================================================================
import math
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

#Roots======================================================================================================================================================================================
import math
def roots():
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

def descriminent():
    a = (int(input('a:')))
    b = (int(input('b:')))
    c = (int(input('c:')))

    desc = ((b**2) -4*a*c)
    print('Descriminent:',desc)

#Factors====================================================================================================================================================================================
import math
def factors():
   x = int(input('Enter A Number:')) 
   print("The factors of",x,"are:")
   for i in range(1, int(math.sqrt(x)) + 1):
       if x % i == 0:
           print(x//i ,i)
            
#Primes=====================================================================================================================================================================================
def isPrime():
    num = int(input('Your Number:'))

    if num > 1:
       # check for factors
       for i in range(2,num):
           if (num % i) == 0:
               print(num,"Is Not Prime")
               print(i,"times",num//i,"is",num)
               break
        
       else:
           print(num,"Is Prime")
       
    else:
       print(num,"Is Not Prime")


def allPrimes():
    n = int(input('Number To Go Up To:'))
    for i in range (n+1):
        if AllPrimesIsPrime(i):
            print(i)
            
def AllPrimesIsPrime(n):
    if n == 0 or n== 1:
        return 'Not Prime'

    elif n == 2 or n== 3:
        return 'Prime'

    elif n%2 == 0:
        return 'Not Prime'
    
    for d in range (3, int(math.sqrt(n))+1, 2):
        if n%d == 0:
            return 'Not Prime'
    else:
        return 'Prime'
#===========================================================================================================================================================================================

        

    
    




















#def allPrimes():

