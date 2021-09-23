import math

'''
allPrimes:
Function to print all primes between 0 to n
It uses inPrime to test primality
'''

def Welcome():
    print('==============================')
    print('To begin, type:')
    print(' ')
    print(' 1) To list all prime numbers')
    print('    between 1 and your number.')
    print(' ')
    print(' 2) To check if your number is')
    print('    a prime number or not.')
    print(' ')
    print(' 3) To check if your number is')
    print('    a palindrome prime number.')
    print(' ')
    print(' 4) To list all palindrome prime')
    print('    numbers between 1 and your number')
    print('==============================')
    a_b = int(input('Pick which program to run: '))
    
    if a_b == 1:
        toExecute()

    elif a_b == 2:
        isPrime()

    elif a_b == 3:
        print('Still working on that :)')

    elif a_b == 4:
        toExecutePalindrome()
    else:
        print('Your answer was not 1 or 2')

def toExecute_Welcome():
    print(' ')
    print('===================================')
    print('To begin enter any number between 1')
    print('and 2.5 billion, and the ')
    print('Mr. Amazing Number Machine ^2 will')
    print('list all primes below your number')
    print('===================================')

def allPrimes_Welcome():
    print(' ')
    print('===================================')
    print('To begin enter any number between 1')
    print('and 2.5 billion, and the ')
    print('Mr. Amazing Number Machine ^2 will')
    print('check if it is a prime number or not')
    print('===================================')

def toExecutePalindrome_Welcome():
    print(' ')
    print('===================================')
    print('To begin enter any number between 1')
    print('and 2.5 billion, and the Mr. Amazing')
    print('Number Machine ^2 will list all')
    print('palindrome primes below your number')
    print('===================================')

def toExecutePalindrome():
    #input n
    toExecutePalindrome_Welcome()
    n = int(input('Pick you number:'))

    #Call allPrimes
    allPalindromePrimes(n)
#end toExecute
    
#==========================================================================

def toExecute():
    #input n
    toExecute_Welcome()
    n = int(input('Pick you number:'))

    #Call allPrimes
    allPrimes(n)
#end toExecute
    
#==========================================================================
    
def isPalindrome(n):
    if n == mirror(n):
        return 1

    else:
        return 0
    #endif
#end isPalindrome
    
#==========================================================================
    
def mirror(n):
    mirror = 0

    while n != 0:
        #Find the last digit and remove it from n
        digit = n % 10
        n = n // 10

        #add the digit to the mirror
        mirror = mirror * 10 + digit

        #endWhile
    return mirror
#end Reverse

#==========================================================================

def allPalindromePrimes(n):

    for i in range (n+1):
        if isPalindrome(i) and isPrime(i):
            print(i)
        #endif
    #end isPalindromePrime

#===========================================================================

def allPrimes(n):
    #traverse all numbers and test primality
    for i in range (n+1):
        if isPrime(i):
            print(i)
#===========================================================================
            
def isPrime(n):
    #Deal with straight cases
    if n == 0 or n== 1:
        return 0
        #endIf

    elif n == 2 or n== 3:
        return 1
        #endElif

    elif n%2 == 0:
        return 0
        #endElif

    #n is odd so we traverese odd devisiors
    for d in range (3, int(math.sqrt(n))+1, 2):
        if n%d == 0:
            return 0

    else:
        return 1

Welcome()
