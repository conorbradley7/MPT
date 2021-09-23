'''
input: numbers EG:                 1, 2, 3
output: selfDescribe number:       11 12 13  -> 1 one 1 two and 1 three
'''
def group(lst):
    acc = []
    for c in lst:
        if acc != [] and c == acc[-1][0]:
            acc[-1] += c
        else:
            acc.append(c)
    return acc

word = input('Thing To Be Grouped:')
x = group(word)
print(x)


def look_say(seed):
    while True:
        old = str(seed)
        new = int(''.join(str(len(g)) + g[0]for g in group(old)))
        yield new
        seed = new

num = int(input('Number:'))

i = 0
lim = 100
for x in look_say(num):
    print(x)
    if i>10:
        break
    i+=1
