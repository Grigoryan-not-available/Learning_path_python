def times(x, y):
    return x * y

print(times(['Emma', 1, 8, 9, 'lol'], 4))

def intersect(seq1, seq2):
    return [c for c in seq1 if c in seq2]

print(intersect('SPAM', 'SCAM'))

y, z = 1, 2

def test_global():
    global x
    x = y + z
    return x


print(test_global(), x)

var = 99

def glob1():
    var = 0
    import Functions
    Functions.var += 1

def glob2():
    var = 0
    import sys
    glob = sys.modules['Functions']
    glob.var += 1

print(var)
glob1()
glob2()
print(var)

X = 99

def f1():
    X = 88

    def f2():
        print(X)

    return f2

action = f1()
action()

def maker(N):
    def action(X):
        return X ** N

    return action

f, g = maker(2), maker(3)
print(f(4), g(4))

def maker_with_lambda(N):
    return lambda X: X ** N

h = maker_with_lambda(2)
print(h(4))

def fun1():
    x = 88
    fun2(x)

def fun2(x):
    print(x)

fun1()

def makeAction():
    act = []
    for i in range(5):
        act.append(lambda x, i=i: i ** x)
    return act

acts = makeAction()

for x in acts:
    print(x(3), end=' | ')
print()

def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester(2)
G = tester(34)

F('asd')
G('fds')
F('qwe')
G('ewq')
F('zxc')
G('cxz')
print('-' * 158)

class testers:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):
        print(label, self.state)
        self.state += 1

Q = testers(0)
W = testers(53)

Q('asd')
W('fds')
Q('qwe')
W('ewq')
Q('zxc')
W('cxz')
print(Q.state, W.state)

def f(a, *pargs, **kargs):
    print(a, pargs, kargs)

f(1, 2, 3, x=1, b=2)

def func(a, b, c, d):
    print(a, b, c, d)

args = 1, 2
args += 3, 4
func(*args)

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)

def knowly(a, *, b = 'lol', c = 'kek'):
    print(a, b, c)

knowly(1, b = 2)

def func1(a, *b, c=6, **d):
    print(a, b, c, d)

func1(1, c = 7, *(2, 3), **dict(x=4, y=5))
func1(1, *(2, 3), **dict(x=4, y=5, c=7))
func1(1, *(2, 3), **dict(x=4, y=5), c=7)

def intersect(*args):
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else: res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res

def tester(func, items, trace = True):
    for i in range(len(items)):
        items = items[1:] + items[:1]
        if trace: print(items)
        print(sorted(func(*items)))

print('-' * 158)
tester(intersect, ('a', 'abcdefg', 'abdst', 'albmcnd'))
print('-' * 158)
tester(union, ('a', 'abcdefg', 'abdst', 'albmcnd'), False)
print('-' * 158)
tester(intersect, ('ba', 'abcdefg', 'abdst', 'albmcnd'), False)

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])
print(mysum([1, 2, 3, 4, 5]))

def sumtree(L):
    total = 0
    for x in L:
        if not isinstance(x, list):
            total += x
        else:
            total += sumtree(x)
    return total

L = [1, [2, [3, 4] , 5], 6, [7, 8]]
print(sumtree(L))
print(sumtree([1, [2, [3, [4, [5]]]]]))
print(sumtree([[[[[1], 2], 3], 4], 5]))

print('-' * 158)
def sumTreeWithoutRecursive_Horizontal(L):
    total = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            total += front
        else:
            items.extend(front)
    return total

print(sumTreeWithoutRecursive_Horizontal(L))
print(sumTreeWithoutRecursive_Horizontal([1, [2, [3, [4, [5]]]]]))
print(sumTreeWithoutRecursive_Horizontal([[[[[1], 2], 3], 4], 5]))

print('-' * 158)

def sumTreeWithoutRecursive_Vertical(L):
    total = 0
    items = list(L)
    while items:
        front = items.pop(0)
        if not isinstance(front, list):
            total += front
            #print(front, '*')
        else:
            items[:0] = front
    return total


print(sumTreeWithoutRecursive_Vertical(L))
print(sumTreeWithoutRecursive_Vertical([1, [2, [3, [4, [5]]]]]))
print(sumTreeWithoutRecursive_Vertical([[[[[1], 2], 3], 4], 5]))

print('-' * 158)

def func_Annotation(a: 'spam', b: (1, 10) = 5, c: {'a': 1} = 6) -> int:
    return a + b + c

print(func_Annotation(1))

f = lambda a, b, c='kek': a + " " + c + " " + b
print(f('lol', '4e6yRek'))
x = (lambda x: (lambda y: x + y))
print(x(1)(2))

print(list(map((lambda x: x + 10), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))

print(list(filter((lambda x: x > 0), range(-5, 5))))

print([x + y for x in 'little' for y in 'BIG'])

M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([M[x][len(M) - x - 1] for x in range(len(M))])

#----------------------------------------Generators---------------------------------------------

def gensquare(N):
    for i in range(N):
        yield i ** N

x = gensquare(5)
print(next(x), next(x), next(x), next(x), next(x), sep=' | ')

line = 'aa bbb c'

print(''.join(x.upper() for x in line.split(' ') if len(x) > 1))

def scramble(seq):
    for i in range(len(seq)):
        print(seq[i:] + seq[:i], ' | ', seq[i:], seq[:i])
        yield seq[i:] + seq[:i]

print(list(scramble('spam')))

G = lambda seq: (seq[i:] + seq[:i] for i in range(len(seq)))

print(list(G('spam')))

def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute1(rest):
                res.append(seq[i:i+1] + x)
        return res

for i in permute1('123'): print(i)

#print(permute1('1234'))


