class FirstClass():
    def setData(self, value):
        self.data = value
    def display(self):
        print(self.data)

class secondClass(FirstClass):
    def display(self):
        print(f'Current value = {self.data}')


class ThirdClass(secondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return f'[ThirdClass: {self.data}]'
    def mul(self, other):
        self.data *= other


firsobj = FirstClass()
firsobj.setData(3)
firsobj.display()
firsobj.data = "kek"
firsobj.display()
firsobj.torba = 'prekol'
print(firsobj.torba)

secobj = secondClass()
secobj.setData(5)
secobj.display()

thdobj = ThirdClass('zxc')
thdobj.display()
print(thdobj)
copies = thdobj + 'qwe'
copies.display()
thdobj.mul(3)
print(thdobj)
