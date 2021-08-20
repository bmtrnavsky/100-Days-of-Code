print("Welcome to the Love Calculator!")
#collect data
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine names
tl_name = name1 + name2

#convert to lower

tl_name_lower = tl_name.lower()

# Count and add True
t = tl_name_lower.count('t')
r = tl_name_lower.count('r')
u = tl_name_lower.count('u')
e = tl_name_lower.count('e')
true = t + r + u + e

# Count and add Love
l = tl_name_lower.count('l')
o = tl_name_lower.count('o')
v = tl_name_lower.count('v')
e = tl_name_lower.count('e')
love = l + o + v + e

#convert to string and concatinate
love_score_str = str(true) + str(love)
print(love_score_str)
#Convert to int
love_score_int = int(love_score_str)

#output 
if love_score_int < 10 or love_score_int > 90:
  print(f"Your score is {love_score_str}, you go together like coke and mentos.")
elif love_score_int > 40 and love_score_int < 50:
  print(f"Your score is {love_score_str}, you are alright together.")  
else:
  print(f"Your score is {love_score_str}.")
