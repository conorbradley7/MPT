def names():
    names = sorted(list(input().split()))
    rels = sorted(list(input().split()))
    names.pop(0)
    rels.pop(0)

    for i in names:
        for x in rels:
            print(i,', I am your', x, '.')
            
