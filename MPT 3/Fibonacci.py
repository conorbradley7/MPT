d = {}
def fib(n):
    if n in d:
        return d [n]
    
    
    if n < 2:
        return n
        
    else:
        res = fib(n-1) + fib(n-2)

    d[n] = res

    return res
