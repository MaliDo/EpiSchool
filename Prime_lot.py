def is_prime(x):
    if x > 1 and x % 2 != 0:
        return True
    elif x == 2:
        return True
    else:
        return False
    
def primes_below(n):
    l1 = []
    l2 = []
    first = 0
    while first < n:
        l1.append(first)
        first = first + 1
    for x in l1:
        if is_prime(x) == True:
            l2.append(x)
    print(l2)

primes_below(24)




