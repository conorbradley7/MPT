import math

def listSum(a) :
    '''
    This sum calculates the sum of the list elems.
    initalise sum = 0
    traverse the list a
         inccreas sum with current elem
    '''
    sum = 0
    n = len(a)
    for i in range(n):
        sum = sum + a[i]
    #endfor

    print('sum=', sum)
# end listSum

#============================================================================================================================================================================================================================================

def listProduct(a) :
    '''
    This sum calculates the product of the list elems.
    initalise prod = 1
    traverse the list a
         inccrease prod by current elem
    '''
    prod = 1
    n = len(a)
    for i in range(n):
        prod = prod * a[i]
    #endfor

    return prod
# end listProduct

#============================================================================================================================================================================================================================================

def listMaximum(a):
    '''
    This function calculates the maximum value and its position
    Initiaise max = a[0] pos = 0
    Traverse the list a
             test max gainst the current element
    '''
    max = a[0]
    pos = 0
    #max, pos =a[0], 0

    n = len(a)
    for i in range(n):
        #test a[i] against max
        if a[i] > max:
            max = a[i]
            pos = i
            # max, pos = a[i], i
        #endif
    #endfor

    print('max=', max)
    print('pos=', pos)
#end listMaximum

#============================================================================================================================================================================================================================================

def listMinimum(a):
    '''
    This function calculates the minimum value and its position
    Initiaise min = a[0] pos = 0
    Traverse the list a
             test min gainst the current element
    '''
    min = a[0]
    pos = 0
    #min, pos =a[0], 0

    n = len(a)
    for i in range(n):
        #test a[i] against min
        if a[i] < min:
            min = a[i]
            pos = i
            # min, pos = a[i], i
        #endif
    #endfor

    print('min=', min)
    print('pos=', pos)
#end listMaximum

#===========================================================================================================================================================================================================================================

def listCount(elem, a):
    '''
    This function counts how often elem occurs in a.
    Use count to counting occurences
    (1) initialise count = 0
    (2) traverse the list
               test is elem equal to the current element
                        count increases
    '''
    count = 0

    #traverse the list
    n = len(a)
    for i in range(n):
        if elem == a [i] :
            count = count + 1
        #endif
    #endfor

    print('Ocurence=', count)
#end listCount

#===========================================================================================================================================================================================================================================

    
    
