from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'manager', pay)

    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
    bob = Person('Bob Jones')
    sue = Person('Sue Smith', 'dev', 100000)
    tom = Manager('Tom Manager', 50000)

    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(f'{sue.pay:.2f}')
    print(tom.lastName())
    for obj in bob, sue, tom:
        obj.giveRaise(.10)
        print(obj)

