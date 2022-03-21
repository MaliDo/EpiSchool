def is_prime(x):
    if x > 1:
        for i in range(2, (int(x**0.5)+1)):
            if x % i == 0:
                return False
        else:
            return True
    else:
        return False 
    
l1 = []    
for num in range(10000, 100000):
    if (list(str(num)) == list(reversed(str(num)))):
        if (is_prime(num) == True):
            l1.append(num)
print(l1)
