import math

#define functions

def palindrome():
    '''
    python program to find the mirror of an int number and then to see if it is palindrome..

    Finding The Mirror  
    n % 10 ==> the last digit of n
    n // 10 ==> removes the last number of the digit
    n*10 + digit ==> add digit to n

    inputs: n - int, confirm input - int
    outputs: mirror, answer of the question: is it palindrome?
    how to do it:
       repeat while the number is not 0
         find the last digit and remove it
         add the last digit to mirror
         if mirror = number: print palindrome
         else: print not palindrome
    '''

    n = int(input('Number='))
    confirmNumber = int(input('Confirm Number='))
    mirror = 0

    # repeat while possible
    while n != 0:
        # find the last digit and remove it
        digit = n% 10
        n = n // 10
        
        # add digit to mirror
        mirror = mirror * 10 + digit
    
       
    #end while

    if mirror == confirmNumber:
        print('This Number Is Palindrome')

    else:
        print('This Number Is Not Palindrome')
    #endif

# end palindrome
