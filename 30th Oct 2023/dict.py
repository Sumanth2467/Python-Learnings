
#dictonary is a unordered and defined by{}

#set can store only values
# Dict can store values along with names

my_dict = {}
my_dict1 = dict()
print(type(my_dict))
print(type(my_dict1))


phone_book = {"Sumanth":543456, "Brooo":76568,"Testt": 87654}
print(phone_book["Sumanth"])
print(phone_book)

phone_book2 = dict(Sumu=7656,test=7654,Broooooo=7654)
print(phone_book2.get('Sumu'))

new_dic = dict(name="Sumanth",age=23,imale=True,Address="AP")
print(new_dic)
print(new_dic.get("name"))

new_dic2 = dict(name="Sumanth",age=24,imale=True,Address="AP")
val = new_dic2.pop("age")
print(new_dic2)

#how to iterate in dict
new_dic3 = {"Sumanth":543456, "Brooo":76568,"Testt": 87654}

for k,v in new_dic3.items():
    print(k,v)

new_dic4 = dict(name="Sumanth",age=24,imale=True,Address="AP")

for k,v in new_dic4.items():
    print(k,v)


#Ordered Dictonary
from collections import OrderedDict
od = OrderedDict()
od['a']= 34
od['b']= 77
od['c']= 98
od['d']= 88
print(od)
