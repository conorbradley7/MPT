import math

#define functions

def digits():
    '''
    python program to find the digits of an int number.

    n % 10 ==> the last digit of n
    n // 10 ==> removes the last number of the digit
    n*10 + digit ==> add digit to n

    input: n - int
    outputs: the digits
    how to do it:
       repeat while the number is not 0
         find the last digit and print it
         remove the last digit
    '''

    n = int(input('n='))

    # repeat while possible
    while n != 0:
        # find the last digit and print it
        digit = n% 10
        print(digit)
        # remove digit
        n= n // 10
    #end while
    print('Number of digits:',len(digitList))

# end digits
