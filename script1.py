import sys
import math
import random

print(sys.platform)
title = "title"
for x in range(5):
    a = math.sqrt(random.randrange(1, 101))
    if a % 2 == 0:
        print(math.pi, a)

stroka = "Opan'ki"

for x in range(len(stroka)):
    print(x, x.__invert__())
    print(stroka[x.__invert__()])
stroka = 'S' + stroka[1:]
print(stroka)
L = list(stroka)
print(L)
L[0] = 'O'
stroka = ''.join(L)
print(stroka)

print(stroka.replace('an', 'kankan'))
print('%s eggs, and %s' % ('spam', 'SPAM!'))
print('{:,.2f} | {:+05d}'.format(244.424424, -4234))
#print(dir(stroka))
#help(stroka.replace)

print('spam', b'a\x01c', u'sp\u0410m')