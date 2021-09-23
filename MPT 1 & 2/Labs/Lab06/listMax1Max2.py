import math

#============================================================================================================================================================================================================================================

def toExecute():
    '''
    Find the two argest elements in a list.
    Inputs: a, n
    Outputs: max1 , max2
    How To Do It:
           (1) Read the inputs
           (2) Calculate max1 and position1
           (3) Change the list element on pos1 [No longer max]
           (4) Calculate max2 and pos2
    '''
    n = int(input('n='))
    print('List Elements:', end = ' ')
    a = listInput(n)

    #calculate max1, pos1
    max1, pos1 = listMaximum(a)

    #change a [pos1]
    a[pos1] = -1000000000

    # calculate max2, pos2
    max2, pos2 = listMaximum(a)

    #print max1, max2
    print('max1=' , max1, 'max2=', max2)
    
#end toExecute
#============================================================================================================================================================================================================================================

def listInput(n):
    a = []
    for i in range(n):
        elem =int(input())
        a.append(elem)
    #endfor

    return a

#end listInput

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

#end listMaximum

#============================================================================================================================================================================================================================================



