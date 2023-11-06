squares = [1,4,9,16,25]

#assigning
l=squares
l2=squares.copy()
print(squares)
print(l)
print(l2)

#assigning value

l[0] = 24
print(squares)
print(l)
print(l2)

print(len(squares))#length of string
print(squares[0:2])#slicing


l3 = [23,34,56]
squares.extend(l3)
print(squares)


print(l2.pop(1))
print(l2)

x="Sumanth"
print(type(x))
list(x)
print(list(x))