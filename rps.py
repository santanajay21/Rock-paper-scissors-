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

game_images =[rock,paper,scissors]
user_choice = int(input("Welcome to the game. Type 0 for Rock, 1 for Paper, and 2 for scissor."))
print(game_images[user_choice])


cpu = random.randint(0,2)
print("Computer's Choice:")
print(game_images[cpu])

if user_choice >= 3 or user_choice < 0:
    print("You have typed an invalid number, You lose!")
elif user_choice == 0 and cpu == 2:
    print("You Win!")
elif cpu == 0 and user_choice == 2:
    print("You Lose!")
elif cpu > user_choice:
    print("You Lose!")
elif user_choice > cpu:
    print("You Win!")
elif cpu == user_choice:
    print("Its a draw!")
