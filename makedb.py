from person import Person, Manager

bob = Person('Bob Jones')
sue = Person('Sue Smith', 'dev', 100000)
tom = Manager('Tom Manager', 50000)

import shelve

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

import glob
print(glob.glob('person*'))
print(open('persondb.dir').read())

db = shelve.open('persondb')
print(len(db))
bob = db['Bob Jones']
print(bob, bob.lastName())

for key in db:
    print(f'{key} => {db[key]}')


