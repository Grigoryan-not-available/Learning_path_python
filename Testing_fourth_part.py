import math

def isInt(value):
    return int(value) == float(value)

def copyDict(oldDict):
    newDict = {}
    for x in oldDict:
        newDict[x] = oldDict[x]
    return newDict

def addDict(a, b):
    newDict = {}
    for x in a:
        newDict[x] = a[x]
    for x in b:
        newDict[x] = b[x]
    return newDict

d = {'a': 1, 'b': 2}


print(copyDict(d), addDict(d, {1: 2, 3: 4}))

def isPrime(y):
    if y <= 1:
        print(y, 'is not prime')
    else:
        х = y // 2
        while х > 1:
            if y % х == 0:
                print(y, 'has factor', х)
                break  # Пропуск else
            х -= 1
        else:
            print(y, 'is prime')

isPrime(1)

list1 = [x for x in range(100) if isInt(math.sqrt(x))]

def sqrtFor(list):
    newlist = []
    for i in list:
        newlist.append(math.sqrt(i))
    return newlist

def sqrtMap(list1):
    return list(map(math.sqrt, list1))

def sqrtLExep(list1):
    return [math.sqrt(x) for x in list1]

def sqrtGExep(list1):
    return (math.sqrt(x) for x in list1)

print(sqrtFor(list1))
print(sqrtMap(list1))
print(sqrtLExep(list1))
print(list(sqrtGExep(list1)))

def recursive(x):
    if x == 0:
        print('STOP')
    else:
        print(x, end=' | ')
        recursive(x - 1)
print(recursive(5))





