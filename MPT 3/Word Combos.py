def combs(lst, n):
    if n >= len(lst):
        return[lst]
    elif n == 0:
        return[""]

    tail = lst[1:]
    head = lst[0]
    first_bit = [head + rec for rec in combs(tail, n-1)]
    second_bit = combs(tail, n)
    return first_bit + second_bit

lst = input('Word:')
n = int(input('Combo Number:'))
for x in combs(lst, n):
    print(x)

print('   ')


def subseq(lst):
    if len(lst) == 0:
        return [lst]
    else:
        head, tail = lst[0], lst[1:]
        rec = subseq(tail)
        first_bit = [head + t for t in rec]
        return first_bit + rec

lst = input('Word:')
for x in subseq(lst):
    print(x)

  
