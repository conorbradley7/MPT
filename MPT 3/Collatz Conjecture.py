'''
Collatz Conjeture
'''

def collatz():

    n = int(input('Number:'))

    l = []
    
    if n == 1:
        l.append([1])

    while n != 1:
        if n % 2 == 0:
            n = n // 2
            l.append([n])

        elif n % 2 != 0:
            n = n*3 + 1
            l.append([n])

    return l

    
        

    



    
