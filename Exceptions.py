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

