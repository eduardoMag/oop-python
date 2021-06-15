# empty dictionary
my_dict = {}
print(my_dict)
# dictionary with integer keys
my_dict = {1: 'msft', 2: 'IT'}
print(my_dict)
# dictionary with mixed keys
my_dict = {'name': 'Aarav', 1: [2, 4, 10]}
print(my_dict)
# using built-in function dict()
my_dict = dict({1: 'msft', 2: 'it'})
print(my_dict)
# from sequence having each item as a pair
my_dict = dict([(1, 'msft'), (2, 'IT')])

# accessing elements of a dictionary
print(my_dict[1])
print(my_dict[2])
print()

print('Modifing Dictionary')
print(my_dict)
my_dict[2] = 'Software'
print(my_dict)
my_dict[3] = 'Microsoft Tecnologies'
print(my_dict)
print()

print('Mixing data types in a dictionary')
print(my_dict)
my_dict[4] = 'Operating System'
print(my_dict)
my_dict['Bill Gates'] = 'Owner'
print(my_dict)
print()

print('Deleting items from dictionary')
print(my_dict)
del my_dict['Bill Gates']
print(my_dict)
my_dict.clear()
print(my_dict)
