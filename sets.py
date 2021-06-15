# set of integers
my_set = {1, 2, 4, 8}
print(my_set)
# set of mixed datatypes
my_set = {1.0, 'Hello world!', (2, 4, 6)}
print(my_set)
print()

# METHODS FOR SETS

# add(x) Method
topics = {'Python', 'Java', 'C#'}
topics.add('C++')
print(topics)
# union method returns a union of two set
print(topics)
team = {'Developer', 'COntent Writer', 'Editor', 'Tester'}
group = topics.union(team)
print(group)
# interset(s) methodn returns an intersection of two sets
inters = topics.intersection(team)
print(inters)
print()

# difference(s) method returns a set containing all the elements of
# invoking set but not of the 2nd set
safe = topics.difference(team)
print(safe)
diff = topics.difference(group)
print(diff)
# clear() method empties the whole set
group.clear()
print(group)
print()

# set operations
# creating two sets
set1 = set()
set2 = set()
# adding elements to se
for i in range(1, 5):
    set1.add(i)

for j in range(4, 9):
    set2.add(j)

print(set1)
print(set2)
print()

# union of set1 and set2
set3 = set1 | set2  # same as set.union(set2)
print('Union of set1 & set2: set3= ', set3)

# intersection of set1 and set2
set4 = set1 & set2  # same as set1.intersection(set2)
print('Intersection of set1 and set2: set4= ', set4)

# checking relationship between set3 and set4
if set3 > set4:  # set3.issuperset(set4)
    print('set3 is superset of set4')
elif set3 < set4:  # set3.issubset(set4)
    print('set3 is subset ot set4')
else:  # set3 == set4
    print('set3 is same as set4')

# diference between set3 and set4
set5 = set3 - set4
print('Elements in set3 and not in set4: set5= ', set5)

# check if set4 and set5 are disjoint sets
if set4.isdisjoint(set5):
    print('set4 and set5 have nothing in common\n')

# remove all values of set5
set5.clear()
print(set5)
