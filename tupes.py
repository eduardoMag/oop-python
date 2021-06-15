stock1 = 'MSFT', 95.00, 97.45, 92.45
stock2 = ('MSFT', 95.00, 97.45, 92.45)

print(type(stock1))
print(type(stock2))

print(stock1 == stock2)
print()

# defining tuples
tupl = ('tuple', 'is', 'an', 'IMMUTABLE', 'list')
print(tupl)

print(tupl[0])
print(tupl[-1])
print(tupl[1:3])
print('''Tuples are immutable and hence:
 You cannot add elements to a tuple.
 You cannot append or extend a method.
 You cannot remove elements from a tuple.
 Tuples have no remove or pop method.
 Count and index are the methods available in a tuple.''')

