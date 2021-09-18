import math

D = {'a': 1, 'b': 2, 'c': 3}
D['e'] = 99
print(D)

if not 'f' in D:
    print('Missing')

value = D.get('x', 0)
print(value)
value = D['x'] if 'x' in D else 4
print(value)

tmp_list = list(D.keys())
print(tmp_list)
tmp_list.sort()
print(tmp_list)

for key in tmp_list:
    print(f'{key} => {D[key]}')

for key in sorted(D):
    print(f'{key} => {D[key]}')

for c in 'spam':
    print(c.upper())

x = 4
while x > 0:
    print('spam!' * x)
    x -= 1

T = (1, 2, 3 ,4)
T += (5, 6)
print(T, T.index(4), T.count(3))
T = (2,) + T[1:]
print(T)

############Files############

f = open('data.txt', 'w')
f.write("First\ntext")
f.close()

file = open('data.txt')
txt_from_file = file.read()
print(txt_from_file.split())

for line in open('data.txt'): print(line, end="")

S = 'sp\x41m'
file = open('unidata.txt', 'w', encoding='utf-8')
file.write(S)
file.close()

text = open('unidata.txt', encoding="utf-8").read()
print("\n" + text)

raw = open('unidata.txt', 'rb').read()
text.encode("utf-8")
print(text, len(raw))

X = set('spam')
Y = {'h', 'a', 'm'}

print(f"{X, Y}\n{X & Y}\n{X | Y}\n{X - Y}\n")

print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])

class Worker:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

bob = Worker("Bobi Kark", 50000)
sue = Worker("Sue Jhons", 60000)

print(bob.lastName(), sue.lastName())
sue.giveRaise(.10)
print(sue.pay)

print(5 // 2, 5 // -2)