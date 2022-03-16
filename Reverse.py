def my_reverse(l1):
    l2 = []
    count = len(l1)
    while count > 0:
        x = l1[count - 1]
        l2.append(x)
        count = count - 1
    print(l2)

my_reverse([1, 2, 3, 4, 5])

def my_reverse2(l1):
    l2 = []
    while len(l1) > 0:
        x = l1.pop()
        l2.append(x)
    print(l2)

my_reverse2([1, 2, 3, 4, 5])