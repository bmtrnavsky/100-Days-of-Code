import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#put game images in a list
game_images = [rock, paper, scissors]

#get user input here

user_choice = int(input("What do you choose?\nType 0 for Rock, 1 for Paper, 2 for scissors.\n "))

#deals with invalad choices bug on user input

if user_choice > 3 or user_choice < 0:
  print("You typed an invalid number. You Lose!")
#print both players choices
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print(computer_choice)
  print(game_images[computer_choice])

#my game logic
  if user_choice == 0 and computer_choice == 2:
    print("You Win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
  elif computer_choice > user_choice:
    print("You Lose!")
  elif user_choice > computer_choice:
    print("You Win!")
  elif computer_choice == user_choice:
    print("It's a draw!") 
