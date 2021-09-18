from collections import namedtuple

print(123)
Rec = namedtuple('Rec', ['name', 'age', 'jobs'])
bob = Rec('Bob', 40.5, ['dev', 'mgr'])
name, age, jobs = bob
print(Rec)
print(bob)
print(name, age, jobs)

myfile = open('myfile.txt', 'w')
myfile.write('hello text file\ngoodbye text file\n')
myfile.close()

myfile = open('myfile.txt')
for x in myfile: print(x)

X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': [1, 2 ,3], 'b': 'kek'}
L = [1, 2 ,3]

F = open('datafile.txt', 'w')
F.write(S + "\n")
F.write(f'{X} | {Y} | {Z}\n')
F.write(str(L) + ' $ ' + str(D) + '\n')
F.close()

F = open('datafile.txt')
line = F.readline().rstrip()
print(line)

line = F.readline().split(' | ')
numbers = [int(x) for x in line]
print(numbers)

line = F.readline().split(' $ ')
obj = [eval(x) for x in line]
print(obj)

D = {'a': 0, 'b': 1}
F = open('just_sample.pk1', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('just_sample.pk1', 'rb')
E = pickle.load(F)
print(type(E), E)

name = dict(first='Bob', last='Smith',)
name['last'] = {1: 2, 3: 4}
rec = dict(name=name, job=['dev', ['check', 'view']], age=0.5)

import json
S = json.dump(rec, fp=open('jsontext.txt', 'w'), indent=4)
print(open('jsontext.txt').read())

P = json.load(open('jsontext.txt'))
print(P, "\n", rec)

a = (4, 5, 6)
a = (1,) + a[1:]
print(a)

L = [0, 1, 2, 3]
L[3:1] = ['?']
print(L[3])

X = 'spam'
Y = 'eggs'

X, Y = Y, X
print(X, Y)

d = {'a': 1, 'b': 2, "c": 3}
d['d'] = 4
print(d)

S = 's[am'
print(S[0][0][0])