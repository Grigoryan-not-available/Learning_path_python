import shelve
db = shelve.open('persondb')

for key in db:
    print(f'{key} => {db[key]}')

sue = db['Sue Smith']
sue.giveRaise(.10)
db['Sue Smith'] = sue
print(sue)

db.close()