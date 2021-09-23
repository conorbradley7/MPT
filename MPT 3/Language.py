class Factor:
    def __init__(self):
        pass

class Quot:
    def __init__(self):
        pass

def to_closing(iterator, opener, closer):
    res = []
    count = 1

    while count > 0:
        x = next(iterator)
        if x == '[':
            count += 1
        elif x == closer:
            count -= 1
        else:
            res.append(x)
    return res
names = {}
stack = []

i = iter(input().split())
while True: 
    try:
        v = next(i)
    except StopIteraton:
        break
    if v == 'drop':
        stack.pop()
    elif v == 'over':
        stack.append(stack[-1])
        stack[-2], stack[-3] = stack [-3], stcak [-2]
    elif v == '[':
        stack.append(to_closing(i))
    else:
        stack.append(v)
