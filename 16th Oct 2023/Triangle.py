side1 = float(input("Enter Your number ="))
side2 = float(input("Enter Your number ="))
side3 = float(input("Enter Your number ="))

if side1==side2 and side1==side3 and side2==side3:
    print("Eq")
elif side1==side2 or side2==side3 or side1==side3 :
    print("ISo")