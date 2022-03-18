def is_prime(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False 
    
def primes_below(n):
    l1 = []
    first = 0
    while first < n:
        if is_prime(first) == True:
            l1.append(first)
        first = first + 1
    print(l1)
