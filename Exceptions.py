def fetcher(obj, index):
    return obj[index]

def catcher(func, obj, *args):
    try:
        print(func(obj, *args))
        #raise IOError
    except IndexError:
        print('got exceprion')
    finally:
        print('Finaly')
s = 'spam'
catcher(fetcher, s, 5)

def kaboom(x, y):
    return x + y

try:
    print(kaboom(['1', '2', '3'], 1))
except TypeError:
    print('Type Error')
print('resuming')

class MyError(Exception): pass

def f(x):
    assert x > 0, 'test x < 0'
    return x ** 2

print(f(3), '\n')

with open('Corp_Site_Sclad.png', 'rb') as file1, open('cp_Corp_Site_Sclad.png', 'wb') as file2:
    file2.write(file1.read())

