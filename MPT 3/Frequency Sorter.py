'''
given a list of nums, put most frequent first.
If equal frequency, put numbers that first appear in origional list first

Input: Number of numbers, max number
       list

Output: Ordered List


EG:
    Input:                Input: 
           5 2                    9 3
           2 1 2 1 2              1 3 3 3 2 2 2 1 1 
    Output:               Output: 
           2 2 2 1 1              1 1 1 3 3 3 2 2 2 
    
'''

def frequencySorter():
    n , c = map(int, input().split())
    numbers = list(map(int, input().split()))

    return sorted(numbers, key = lambda n : (-numbers.count(n), numbers.index(n)))  
            
            


def frequencySorter2():
    _ , c = map(int, input().split())
    nums = [int(n) for n in input().split()]
    stor = [None for _ in range (c + 1)]

    for i, m in enumerate(nums):
        if stor[m] == None:
            stor[m] = [-1, i]
        else:
            stor[m][0] -= 1

    print(*sorted(nums, key= stor._getitem_))
