numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(num):
    return num%2==0

even_numbers = filter(is_even,numbers)
even_numbers_list= list(even_numbers)
print(even_numbers_list)



#example 2

words = ["apple","banana","cherry","fig","watermelon"]
min_len = 6

def check_len(word):
    return len(word)>=min_len
op= list(filter(check_len,words))
print(max(op))
print(op)


#example3

products = [{"name": "Sumanth","price": 1000},
            {"name": "jack fruit","price": 250},
            {"name": "tablet","price": 500},
            {"name": "smartphone","price": 700}]

def max_price(iteam):
    return iteam["price"]<=500

affordable_iteams = list(filter(max_price,products))
print(affordable_iteams)


list_check =["wed", 233]
print(type(list_check))