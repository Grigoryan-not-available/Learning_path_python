import sys

lunch = ham = 'spam'

nudge = 1
wink = 2
nudge, wink = wink, nudge
print(nudge, wink)

string = 'SPAM'
a, b, c, d = string
print(a, b, c ,d)

((a, b), c) = ('SP', 'AM')
print(a, b, c)

red, green, blue = range(3)
print(red, green, blue, type(red))

seq = [1, 2, 3, 4]
a, *b = seq
print(a, *b, b, sep=' | ')

L = [1, 2 ,3 ,4]
while L:
    front, *L = L
    print(front, L)
print('-' * 158)
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)

a = b = c = 1
b += 1
c += 2
print(a, b, c, sep=' | ')

a, b = [], []

sys.stdout.write('kek\n')

temp = sys.stdout
sys.stdout = open('log.txt', 'w')
print('spam', 1, 2, 3, sep='\n')
sys.stdout.close()
sys.stdout = temp
print('spam', 1, 3, 2, sep='\n')

log = open('log.txt', 'a')
print(1, 2, 3, file=log)
print(1, 2, 3)

