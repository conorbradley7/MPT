import math

# define functions
def toExecute():
    n = int(input('n='))

    #call allPrimes or other function.
    allPalindromePrimes(n)
#end toExecute

def isPalindrome(n):

    mirror = reverse(n)
    if n == mirror:
        return 1
    else:
        return 0
    #endif
    
#end isPalindrome

def reverse(n):
    '''
    This function is to mirror an intiger.
    It detects the digits and puts them in mirror
    '''
    mirror = 0
    while n != 0:
         # find the last digit and remove it
         digit = n % 10
         n = n//10

         #add the digit to mirror
         mirror = mirror * 10 + digit

    #endwhile

    return mirror

#end reverse

def allPalindromePrimes (n):
    '''
    Function to generate all palindrome primes
    '''
    for i in range (n+1) :
        if isPalindrome(i)  and isPrime(i):
            print(i)
        #endif
#end allPalindromePrimes

def allPrimes (n):
    '''
    Function to print all primes between 0 to n.
    It uses is Prime to test primality.
    '''
    # traverse all numbers and test primality
    for i in range (n+1) :
            if isPrime(i) :
                print(i)
            #endif
    #endfor
                
#end allPrimes


def isPrime(n):
    # deal with straight cases
    if n == 0 or n == 1:
        return 0
    #endif

    if n == 2 or n == 3:
        return 1
    #endif

    if n % 2 == 0:
        return 0
    #endif

    # n is odd so we traverse odd divisors
    for d in range(3, int(math.sqrt(n))+1,2) :
        if n % d == 0:
            return 0
        #endif
    #end for
    return 1
#end isPrime
