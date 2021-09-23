import math
#============================================================================================================================================================================================================================================
def maxFreq(a):

      '''
      To develop a program to find the maximum value in a list and how frequent it occurs.
      Inputs: (none)
      Outputs: max, freq
      How to do it:  (1): read a
                            (2): Find the maximum value of a
                            (3): initialise count = 0
                            (4): for each time the max number occurs, count + 1
                            (5): Print max, freq
      '''
      
      #find max number and its frequency
      
      print('max=', maximum)
      print('freq=', freq)

#============================================================================================================================================================================================================================================      
def listMaximum(a):
    '''
    This function calculates the maximum value and its position
    Initiaise max = a[0] pos = 0
    Traverse the list a
             test max gainst the current element
     maximum = a[0]
     '''
    
    n = len(a)
    for i in range(n):
        #test a[i] against max
        if a[i] > maximum:
            maximum = a[i]
        #endif
    #endfor

    print('max=', maximum)
#end listMaximum
#============================================================================================================================================================================================================================================      
def maxCount(a):
    '''
    This function counts how often the max value occurs in a.
    Use count to counting occurences
    (1) initialise count = 0
    (2) traverse the list
               test is max equal to the current element
                        count increases
    '''
    count = 0

    #traverse the list
    n = len(a)
    for i in range(n):
        if maximum == a [i] :
            count = count + 1
        #endif
    #endfor

    print('Frequency=', count)
#end listCount
#===========================================================================================================================================================================================================================================

      
