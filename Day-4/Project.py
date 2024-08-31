import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

options = [rock, paper, scissors]

user_move = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
system_move = random.randint(0, 2)

print("System's Move:")
print(options[system_move])

print("User's Move:")
print(options[user_move])

if options[user_move] == rock and options[system_move] == paper:
    print('You Lose!')
elif options[user_move] == paper and options[system_move] == rock:
    print('You Win!')
elif options[user_move] == scissors and options[system_move] == rock:
    print('You Lose!')
elif options[user_move] == rock and options[system_move] == scissors:
    print('You Win!')
elif options[user_move] == paper and options[system_move] == scissors:
    print('You Lose!')
elif options[user_move] == scissors and options[system_move] == paper:
    print('You Lose!')
