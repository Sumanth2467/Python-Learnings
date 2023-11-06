name = str(input("Enter your name\n"))
vowels ="aeiouAEIOU"

count=sum(name.count(vowels)for vowel in vowels)
print(count)