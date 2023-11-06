

set1 = set()
print(set)

set2 = set("sumanth")

print(set2)

set3={1,2,3,4,5}

set4 = set(["sumanth","bro","Sumanth"])
print(set4)
print(len(set4))

set5={1,2,3,4,5,}
set6={3,4,5,6,7,8,6}
my_set= set5.union(set6)
print(my_set)

my_set1= set5.intersection(set6)
print(my_set1)

my_set2= set5.difference(set6)
print(my_set2)
set7={1,2,3,4,5,6,7,8}
my_set3= set5.issubset(set5)
print(my_set3)

set6.add(10)
print(set6)


