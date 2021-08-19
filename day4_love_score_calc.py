print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

name1_true = name1_lower.count('t') + name1_lower.count('r') + name1_lower.count('u') + name1_lower.count('e')

name1_love = name1_lower.count('l') + name1_lower.count('o') + name1_lower.count('v') + name1_lower.count('e') 

name2_true = name2_lower.count('t') + name2_lower.count('r') + name2_lower.count('u') + name2_lower.count('e')

name2_love = name2_lower.count('l') + name2_lower.count('o') + name2_lower.count('v') + name2_lower.count('e') 

love_score_t = name1_true + name2_true
love_score_l = name1_love + name2_love

love_score_str = str(love_score_t + love_score_l)
love_score_int = int(love_score_str)
print(love_score_int)

if love_score_int < 10 or love_score_int > 90:
  print(f"Your score is {love_score_str}, you go together like coke and mentos.")
elif love_score_int > 40 and love_score_int < 50:
  print(f"Your score is {love_score_str}, you are alright together.")  
else:
  print(f"Your score is {love_score_str}.")
