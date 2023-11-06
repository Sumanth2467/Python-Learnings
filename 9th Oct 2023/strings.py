#capitalize
name = "Sumanth"

#name[0] = "h" # Strings cannot change

result = name.capitalize()
print(name)
print(result)
#to print Id's
print(id(name))
print(id(result))

#to show in Upper case
name2 = name.upper()
print(name2)

#to show lower case
name3= name.lower()
print(name3)


#swapcase()
name4= name.swapcase()
print(name4)

name5 = "SUmantH"
print(name5.swapcase())


#title
name6= "sumanth sure"
print(name6.title())

#Replace
text = "Nice Bro"
result = text.replace("Bro","Man")
print(result)


#find()
text = "Nice Bro"
test = text.find("Bro")
print(test)

#count()
text = "Nice Bro"
print(text.count("B"))

#to find length
name = "test "
print(len(name))


#list
list = [1,2,2,3,4,4]
print(list)

#To remove duplicates in list
list = {1,2,2,3,4,4}
print(list)

