'''
Given a base
Givenn another base
Given n
Given n numbers in the first base
Return if they're palindromes in the second
'''
import math
def palindromeBases():

    b1 = int(input("Base 1:"))
    b2 = int(input("Base 2:"))
    n = int(input("Number:"))

    # Find the two bases of the number and check if they're palindromes

    x = math.log(n,b1)
    y = math.log(n,b2)


    if x == mirror(y):
        print('It Is Prime')


    else:
        print('It Is Not Prime')

        

    
