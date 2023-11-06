number = int(input("Enter you number :"))
if number <0:
    print("Factorial is not possible")
else:
    fact =1
    for i in range(1,number+1):
        fact = fact*i
print("Fact is --", fact)