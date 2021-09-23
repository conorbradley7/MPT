'''
A self referential number is a number where each digit describes the number
ie: the first digit represents how many zeros
    the second digit represennts how many ones there are
and so on

EG: 21200
2 zeros
1 one
2 twos
0 threes
0 fours
'''
def is_self_ref(n):
    digs = [int(dig) for dig in str(n)]
    for i, dig in enumerate(digs):
        if digs.count(i) != dig:
            return False
    return True

from itertools import count

for i in count(1):
    if is_self_ref(i):
        print(i)

        
    
