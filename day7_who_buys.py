import random 

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#determine length of list
length = len(names)
#use len to select from a range 
position = random.randrange(0, length -1)
#print name at random position
person = names[position]
print(f"{person}, is going to buy the meal today!")
