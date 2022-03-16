def is_prime(x):
    if x > 1 and x % 2 != 0:
        return True
    elif x == 2:
        return True
    else:
        return False
    
l1 = list(range(10000, 100000))
l2 = []
l3 = []

for x in l1:
    if is_prime(x) == True:
        l2.append(x)

for y in l2:
    if list(str(y)) == list(reversed(str(y))):
        l3.append(y)

print(l3)