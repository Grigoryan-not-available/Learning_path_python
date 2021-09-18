res = [c * 4 for c in 'SPAM']
print(res)
print(list(map(abs, [-1, 0, 1, 2, 3, 4])))

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

result = [matrix[i][len(matrix[i]) - i - 1] for i in range(len(matrix))]
print(result, type(result))

L = ['abc', 'ABD', 'аВе']
L.sort(key=str.lower, reverse=True)
print(L)

L.pop()
print(L)
print('-' * 158)

D = dict(zip(list(c * 3 for c in 'akd;asjdlajsda'), list(range(14))))
print(len(D), 'ham' in D, list(D.keys()))

D['aaa'] = ['ad', 'fh', 'jl']
del D[';;;']
D['brunch'] = 'Bacon'
print(D, '\n', D.values(), '\n', D.items())

D2 = {'toast': 4, 'muffin': 5}
D.update(D2)
print(D)
D.pop('muffin')
D.pop('toast')
print(D)

table = {1975: 'Holy Grail',
1979: 'Life of Brian',
1983: 'The Meaning of Life'}

for year in table:
    print(str(year) + "\t" + table[year])
rec = {'name' : 'Bob',
'jobs': ['developer', 'manager'],
'web': 'www.bobs.org/~Bob',
'home': {'state': 'Overworked', 'zip': 12345}}

print(rec['home']['state'])