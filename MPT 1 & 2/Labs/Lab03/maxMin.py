'''
    this progrm is to find the maximum nd minimum of 4 float a, b, c, d.

    inputs: a,b,c,d
    outputs: min, max
    how to do it?

        1)find max1 and min1 of a nd b
        2)find max2 and min2 of c and d
        3)find the max of max 1 nd max 1 and max2
        4)find the min of min1 and min2

'''

import math

def maxMin():

    #red inputs
    a, b, c, d = map(float,input('Read a b c d:').split())

    #find max1, min1 of a, b
    if a>b :
        max1 = a
        min1 = b
    else :
        max1 = b
        min1 = a
    #endif

    #find max2, min2 of c, d
    if c>d :
        max2 = c
        min2 = d
    else :
        max2 = d
        min2 = c
    #endif

    #find max of max1, max2
    if max1>max2 :
        maximum = max1

    else :
        maximum = max2
    #endif
        
    #find min of min1, min2
    if min1>min2 :
        minimum = min2

    else :
        minimum = min1
    #endif

    # print maximum and minimum
    print('maximum=', maximum)
    print('minimum=', minimum)

# end maxMin
