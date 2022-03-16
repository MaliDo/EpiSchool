def is_prime(x):
    if x > 1 and x % 2 != 0:
        return True
    elif x == 2:
        return True
    else:
        return False
    
print(is_prime(5))
