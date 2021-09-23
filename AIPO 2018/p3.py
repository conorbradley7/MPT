x = str(input())
y = list(x)
    

ans = []
    
for i in y:
        if i == 'A':
            ans.append('T')
        if i == 'T':
            ans.append('A')
        if i == 'G':
            ans.append('C')
        if i == 'C':
            ans.append('G')


print(''.join(ans))
