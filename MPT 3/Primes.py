from math import floor, sqrt

def primes(n):
    past_primes = [2]
    for p in range(n):
        if all(p % d != 0 for d in past_primes):
            past_primes.append(p)
        return past_primes

def prime(n):
    sieve = [m % 2 != 0 for m in range (n)]
    sieve[1] = False
    sieve[2] = True
    lim = floor(sqrt(n)) + 1
    for p in range(3,lim,2):
        if sieve[p]:
            yield p
            for mul in range(p*p,n,p):
                sieve[mul] = False
    for p in range(lim,n):
        if sieve[p]:
            yield p 
 
    
