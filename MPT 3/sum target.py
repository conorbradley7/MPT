'''
discount all numbers bigger than the target
go through others and try to find a pair
if found:  return pair
if not: return None
'''


def sumTarget():
    ins = [1, 2, 3]
    t = 3

    i, j = 0, len(ins)-1
    while i > j:
        if ins[i] + ins[j] > t:
            j -= 1

        elif ins[i] + ins[j] > t:
            i += 1

        else:
            return (ins[i], ins[j])
