import random

print("Welcome to Virtual Coin Toss!")

coin = random.randint(0, 1)
if coin == 1:
  print("Heads")
else:
  print("Tails")  
