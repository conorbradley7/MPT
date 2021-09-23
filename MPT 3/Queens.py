'''
write a program that will give the position of 8 queens on an 8x8 chess board
in positions where they cannot harm each other

store board as a set of co-ordinates
'''

def threat(x,y):
    return x[0] == y[0] or x[1] == y[1] or abs(x[0]-y[0]) == abs(x[1]-y[1])
    

def queens(c,p):
    if c == 8:
        print(p)
    else:
        for r in range(8):
            if not any(threat((c, r), x) for x in p):
                queens(c+1, p+[(c,r)])


#arguments are 0(coulmn 0) & [](no queens yet)
                
