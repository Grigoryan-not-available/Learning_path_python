import os

x = 'spam!' * 2
while x:
    print(x, end=' | ')
    x = x[:-1]

print()
a = 0; b = 10
while a < b:
    print(a, end=' | ')
    a += 1

print()

y = 12
x = y // 2
print(x)
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    x -= 1
else:
    print(y, 'is prime')

D = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in D.items(): print(key, '=>', value)

items = ["ааа", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]

for key in tests:
    if key in items:    print(key, 'was found')
    else:               print(key, 'wasn\'t found')

S = 'abcdefghijk'
for c in S[::2]: print(c, end=' | ')
print()

S1 = 'abc'
S2 = 'def123'
print(list(zip(S1, S2)))

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
print(dict(zip(keys, vals)))

S = 'spam'
for (offset, item) in enumerate(S):
    print(item, 'appears at offset', offset)

# for i, line in enumerate(os.popen('systeminfo')):
#     if i == 4: break
#     print(line.rstrip())

for f in open('script2.py'):
    print(f, end='')

print()

file = open('script2.py')
print(file)
print(next(file))
print(next(file))

L = [1, 2, 3, 4, 5, 6, 7, 8]

I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print(X ** 2)

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, D[key])

lines = [line.rstrip() for line in open('script2.py') if line[0] == 'p']
print(lines)

#Tasks after chapter

s = 'spam!'
o = 0
for c in s:
    o += ord(c)
print(o)

L = [ord(c) for c in s]
print(L, list(map(ord, s)))

for i in range (50):
    print('hello %d\n\a' % i)

D = dict(zip(range(100, 1, -2), range(2, 101, 2)))
sorted(D)
for x in D:
    print(f'{x}: {D[x]}')
print()

L = [1, 2, 4, 8, 16, 32, 64]
X = 5; i = 0

while i < len(L):
    if 2 ** X == L[i]:
        print(f'{2 ** X} found in list at position {i}')
        break
    i += 1
else:
    print('Not found')

for i in range(len(L)):
    if 2 ** X == L[i]:
        print(f'{2 ** X} found in list at position {i}')
        break
else:
    print('Not found')

if 2 ** X in L:
    print(f'{2 ** X} found in list at position {L.index(2 ** X)}')
else:
    print('Not found')

