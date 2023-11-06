my_list = [1,2,3,5,7]
print(type(my_list))

#Tuple
car = ("Gwagon","evoque","x7")
print(type(car))

car2 = (1,"65&","hgfdg","true","1.23333")
print(car2)


tuple1=()
tuple2=(1,2,3,4,5)
tuple3=tuple(["Sumanth","Bro"])
print(tuple1)
print(tuple2)
print(tuple3)

print(max(tuple2))
print(max(tuple3))
print(max(car))

#merging tuples

hero1 = ("ntr","balayya")
hero2 =("ntr","prabas")
team = hero1+hero2
print(team)
print(list(team))
print(tuple(team))

#nested tuple
hero3 = ("ntr","balayya")
hero4 =("ntr","prabas")
team2=(hero3,hero4)
print(team2)
print(team2[1][1])
print("mega"in hero4)#can check true or flase
