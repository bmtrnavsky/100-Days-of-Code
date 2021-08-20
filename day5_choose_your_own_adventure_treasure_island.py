print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("you find yourself cold and wet on a beach. \nNightfall is rapidly approching would you like to walk\nor light a fire and camp?\nEnter 1 for walk or 2 for camp?  ")
if choice1 == 1:
  print("You wander into the darkness and die from exposure\n Game Over")
else:
  print("You find the warmth and light of the fire comforting in this strange place")

choice2 = input("Walking down the beach you find a river.\nWould you like to cross the river or follow it to its source?\nEnter 1 to cross or 2 to follow it to its source " )
if choice2 == 1:
  print("As you bravely swim across the river you are consumed by\na viscous sea monster!\nGame Over!")
else:
  print("Following the river through the jungle is quite an\nadventure. After several hours of walking you find\nwhat appears to be an abandoned temple")

choice3 = input("You can see the treasure just inside the temple\ndoor. However, the temple is surrounded by a moat. You have\nthree choices to get to the treasure. Swim the moat, cross the\nrickety bridge, or swing on the vine.\nEnter 1 to swim, 2 to cross the\n bridge or 3 to swing on the vine. ")
if choice3 == 1:
  print("The waters of treasure island are dangerous! You were\nconsumed by crocidiles!\nGame Over!")
elif choice3 == 2:
  print("The rickety bridge was not substancial enough to hold\nyour weight. It collapes under your weight and you are\nconsumed by hungry crocidiles.\nGame Over!")
else:
  print("You skilfully swing across the moat and enter the temple\nsafely!\nYou found the treasure! Congratulations!")
