# reversed(seq)
normal_list = [2, 4, 5, 7, 9]

class CustomSequence():
    def __len__(self):
        return 5
    def __getitem__(self, index):
        return "x{0}".format(index)

class funkyback():
    def __reversed__(self):
        return 'backwards!'

for seq in normal_list, CustomSequence(), funkyback():
    print('\n{}:'.format(seq.__class__.__name__), end="")
    for item in reversed(seq):
        print(item, end=", ")
print()

# enumertae()
names = ['Rajesh', 'Jhon', 'Billy', 'Mandy', 'Natasha']
print(enumerate(names))
print(list(enumerate(names)))
print()
#better used for keeping count in a for loop
for i,n in enumerate(names):
    print('Names number: ' +str(i))
    print(n)