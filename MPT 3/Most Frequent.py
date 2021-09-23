def mostFrequent():
    word = input()

    d = {} 

    for c in input():
        if c in d:
            d[c] += 1 
        else:
            d[c] = 1


    bestKey, bestValue = None, None
    for key, value in d.items():
        if value > bestValue:
            bestValue = value
            bestKey = key

    print(bestKey, bestValue)









            
