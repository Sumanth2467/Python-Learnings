#Breat and Continue

#Break
count = 1
while count <=10:
    print(count)
    if count>=6:
        break
    count = count +1

#for loop
print("for loop Started")
for counter in range(1,11):
    if counter == 8:
        break
    print(counter)
print("For loop is finished")

#Pass
print("Pass Functionality")
for num in range(1,10):
    if num==7:
        pass
    print(num)


