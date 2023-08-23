import random
from art import logo

print(logo)
print(
    "Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100"
)
number = random.randint(1, 101)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level.lower() == 'hard':
    lives = 5
else:
    lives = 10
print(f"You have {lives} attempts to guess the number.")
game_over = False

while game_over != True:
    guess = int(input("Make a guess: "))
    if guess == number:
        print("You guess is correct!\nYou won!")
    else:
        lives -= 1
        if lives == 0:
            game_over = True
        if guess > number:
            print(
                f"Too high\nGuess again\nYou have {lives} attempts remaining to guess the number"
            )
        elif guess < number:
            print(
                f"Too low\nGuess again\nYou have {lives} attempts remaining to guess the number"
            )

if lives == 0 and guess != number:
    print("You're out of lives\nGame Over\nYou lose!")
