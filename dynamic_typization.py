a = 3
b = a
print(a, b)
a += 2
print(a, b)

L = [1, 2, 3, 4]
L2 = L
L[0] = 'kek'
print(L, L2)
L = 24
print(L, L2)

##########

l = [1, 2, 3, 4]
l2 = l.copy()
l[0] = 24
print(l, l2)


