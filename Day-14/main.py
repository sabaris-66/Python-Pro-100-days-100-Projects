from art import logo, vs
from game_data import data
import random
from replit import clear

print(logo)


#a function to pick celebrities from the dictionary
def pick_celebrity(data, viewed_celebrities):
  b = random.choice(data)
  while b['name'] in viewed_celebrities:
    if len(viewed_celebrities) == len(data):
      print("You saw all the available celebrities\nGame Over")
      return 0
    b = random.choice(data)
  viewed_celebrities.append(b['name'])
  return b


#comparing celebrity followers count
def compare_followers(a, b):
  if a['follower_count'] > b['follower_count']:
    return 'a'
  return 'b'


def higher_lower(a, viewed_celebrities, score):
  b = pick_celebrity(data, viewed_celebrities)
  if b == 0:
    print(f"And your final score is {score}")
    return 0
  print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
  print(vs)
  print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
  user_option = input("Who has more followers, Type 'A' or 'B' : ").lower()
  real_answer = compare_followers(a, b)
  if user_option != real_answer:
    clear()
    print(logo)
    print(f"Sorry that's wrong, Final score: {score}")
    return 0
  else:
    score += 1
    clear()
    print(logo)
    print(f"You're right, Current score: {score}")
    a = b
    higher_lower(a, viewed_celebrities, score)


def main():
  a = random.choice(data)
  viewed_celebrities = []
  score = 0
  viewed_celebrities.append(a['name'])
  higher_lower(a, viewed_celebrities, score)


main()