import math

def primes():
      '''
          To develop a program to: (1) Input n.
                                                (2) Find all numbers less than or equal to n that are prime.
                                                (3) Find the numbers that have mirrors that are prime.
                                                (4) Print the numbers

          Input: n

          Outputs: The numbers that match the above requirements
      '''
      n = int(input('n='))

      #call isPrime (n) and reverse(n) 
      isPrime(n)
      reverse(n)
#end primes

def isPrime(n):
    # deal with straight cases
    if n == 0 or n == 1:
        print('Is Not Prime')
    #endif

    if n == 2 or n == 3:
        print('Is Pirme')
    #endif

    if n % 2 == 0:
        print('Is Not Prime')
    #endif
      
    # n is odd so we traverse odd divisors
    for d in range(3, int(math.sqrt(n))+1,2) :
        if n % d == 0:
            print('Is Not Prime')
        #endif
    #end for
    print('Is Prime')
#end isPrime


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


