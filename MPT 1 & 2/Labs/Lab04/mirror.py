import math

#define functions

def mirror():
    '''
    python program to find the mirror of an int number.

    n % 10 ==> the last digit of n
    n // 10 ==> removes the last number of the digit
    n*10 + digit ==> add digit to n

    input: n - int
    outputs: mirror
    how to do it:
       repeat while the number is not 0
         find the last digit and remove it
         add the last digit to mirror
    '''

    n = int(input('n='))
    mirror = 0

    # repeat while possible
    while n != 0:
        # find the last digit and remove it
        digit = n% 10
        n = n // 10
        
        # add digit to mirror
        mirror = mirror * 10 + digit
       
    #end while
    print(mirror)

# end mirror
