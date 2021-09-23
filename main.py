#exec(open('script1.py').read())
from datetime import datetime

def timeit(name):
    print(name)
    def outer(func):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = func(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    return outer

@timeit('kek')
def loopGenlist(n):
    lists = []
    for i in range(n):
        if i % 2 == 0:
            lists.append(i)
    return lists

@timeit('lol')
def listGen(n):
    lists = [i for i in range(n) if i % 2 == 0]
    return lists

#f1loop = loopGenlist(10**7)
#f2glisten = listGen(10**7)

l = ['adadadodf', 'sfsfo', '123', 'dsfdgqeg']

print(list(map(lambda x, y: x + y, (1, 2), (3, 4))))

print(list(filter(lambda c: 'o' in c, l)))  
