def f(x, l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3, [3, 2, 1])
f(3)


'''When we call f(2), the function appends the squared values of 0 and 1 to the 
default list l, which is initially an empty list. Therefore, it prints [0, 1].'''
'''When we call f(3, [3, 2, 1]), we pass a different list [3, 2, 1] as an argument. 
The function appends the squared values of 0, 1, and 2 to this specific list l. Hence, it prints [3, 2, 1, 0, 1, 4].'''
'''When we call f(3) again without passing a list argument, the function uses 
the previously modified default list l, which now contains the values [0, 1, 0, 1, 4]. 
It then appends the squared values of 0, 1, and 2 to this same list. Consequently, it prints [0, 1, 0, 1, 4].'''