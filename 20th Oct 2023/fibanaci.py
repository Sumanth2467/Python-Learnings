

number = int(input("Enter the Number"))

a,b = 0,1
while a < number:
    print(a, end ='')
    a, b = b, a+b

