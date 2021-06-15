# CFREATION AND INSTANTIANTION
class MyClass(object):
    pass


# create first instance of MyClass
this_obj = MyClass()
print(this_obj)

# another instance of MyClass
that_obj = MyClass()
print(that_obj)
print()


# define one variable inside class MyClass()
class MyClass(object):
    var = 9


# create first instance of MyClass
this_obj = MyClass()
print(this_obj.var)
# another instance of MyClass
that_obj = MyClass()
print(that_obj.var)
print()


# INSTANCE METHODS
class MyClass(object):
    var = 9

    def firstM(self):
        print("Hello World!")


obj = MyClass()
print(obj.var)
obj.firstM()
print()


# encapsulation
class MyClass(object):
    def setAge(self, num):
        self.age = num

    def getAge(self):
        return self.age


zack = MyClass()
zack.setAge(45)
print(zack.getAge())

zack.setAge('Fourty-five')
print(zack.getAge())
print()


# init constructor
class myclass(object):
    def __init__(self, aaa, bbb):
        self.a = aaa
        self.b = bbb


x = myclass(4.5, 3)
print(x.a, x.b)
print()


# class attributes
class myclass(object):
    classy = 'class value'


dd = myclass()
print(dd.classy)

dd.classy = 'Instance Value'
print(dd.classy)

del dd.classy
print(dd.classy)


# class and instance data
class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val

        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(9)
b = InstanceCounter(18)
c = InstanceCounter(27)

for obj in (a, b, c):
    print('val of obj: %s' %(obj.get_val()))
    print('count: %s' %(obj.get_count()))