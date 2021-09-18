bob1 = dict(name='Bobi', job='dev', age=40)
bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(f"{bob1}\n{bob2}")

employee = {'name': {'first': "Bob", "last": "Kekov"},
            'title': ['dev', 'mgr'],
            'age': 40.5}
print(employee['name']['last'])
print(employee['title'][-1])
employee['title'].append('janitor')
print(employee)
