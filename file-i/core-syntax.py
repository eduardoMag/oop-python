class SumList(object):
    def __init__(self, my_list):
        self.mylist = my_list

    def __add__(self, other):
        new_list = [x + y for x, y in zip(self.mylist, other.mylist)]
        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)


aa = SumList([3, 6, 9, 12, 15])

bb = SumList([100, 200, 300, 400, 500])

cc = aa + bb
print(cc)
print()


# inheriting from built-in types
class MyDict(dict):
    def __setitem__(self, key, value):
        print('setting a key and value!')
        dict.__setitem__(self, key, value)


dd = MyDict()
dd['a'] = 10
dd['b'] = 20

for key in dd.keys():
    print('{0}={1}'.format(key, dd[key]))
print()


# MyList inherit from 'list' object but indexes from 1 instead of 0!
class MyList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError
        if index > 0:
            index = index - 1
            return list.__getitem__(self, index)

    # we access a value with subscript like x[1]
    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError
        if index > 1:
            index = index - 1
            list.__setitem__(self, index, value)


x = MyList(['a', 'b', 'c'])
print(x)

x.append('hello')
print(x)
print(x[1])
print(x[4])
print()
