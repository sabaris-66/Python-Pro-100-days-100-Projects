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

#Write your code below this line 👇
import random

user_input = int(input("Enter 0 for rock, 1 for paper, 2 for scissors\n"))
if user_input not in [0,1,2]:
  print("Error")
pc_input = random.randint(0, 2)
rps = [rock, paper, scissors]
print(rps[user_input])
print(rps[pc_input])
if (user_input == 0
        and pc_input == 1) or (user_input == 1
                               and pc_input == 2) or (user_input == 2
                                                      and pc_input == 0):
    print("You lose!")
elif user_input == pc_input:
    print("Its a tie")
else:
    print("You Won!")
