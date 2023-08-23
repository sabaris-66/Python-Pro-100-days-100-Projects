import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  #global variable


def exceed_checker(user, pc):
    if sum(user) > 21:
        print("User value exceeds 21\n You lose!")
        return True
    elif sum(pc) > 21:
        print("PC value exceeds 21\n You Won!")
        return True
    elif sum(user) == 21 or sum(user) == 21:
        return blackjack(user, pc)
    else:
        return False


def ace_checker(user, pc):
    if 11 in user and sum(user) > 21:
        user[user.index(11)] = 1
    if 11 in pc and sum(pc) > 21:
        pc[pc.index(11)] = 1
    return exceed_checker(user, pc)


def sixteen_checker(user, pc):
    if sum(pc) < 17:
        pc.append(random.choice(cards))
    return exceed_checker(user, pc)


def game_checker(user, pc):
    if sum(user) < sum(pc):
        print(
            f"User value, {sum(user)}, {user} is lesser than PC value, {sum(pc)}, {pc}\n You lose!"
        )
    elif sum(user) > sum(pc):
        print(
            f"User value, {sum(user)}, {user} is greater than PC value, {sum(pc)}, {pc}\n You won!"
        )
    else:
        print("Its a draw, both sides have same value, {sum(user)}")


def blackjack(user, pc):
    if sum(user) == 21 and sum(pc) == 21:
        print(f"Its a draw since both users have {sum(user)}")
    elif sum(user) == 21:
        print(f"User score is {sum(user)}, {user}\n You won!")
    elif sum(pc) == 21:
        print(f"PC score is {sum(pc)}, {pc}\n You lost!")
    else:
        return False
    return True


def game():
    user, pc = [], []
    for i in range(2):
        user.append(random.choice(cards))
        pc.append(random.choice(cards))
    print(f"User cards: {user}")
    print(f"PC first card: {pc[0]}")
    if blackjack(user, pc):
        return 0
    if ace_checker(user, pc):
        return 0
    stand = 'y'
    while stand == 'y':
        print(f"Your cards are {user} and your total is {sum(user)}")
        stand = input(
            "Do you want to hit another card, Type 'y' to hit, 'n' to end: ")
        if stand != 'y':
            break
        user.append(random.choice(cards))
        if ace_checker(user, pc):
            return 0
    if sixteen_checker(user, pc):
        return 0
    game_checker(user, pc)
    return 0


game_start = 'y'
while game_start == 'y':
    game_start = input("Type 'y' to start Blackjack or 'n' to end: ")
    if game_start != 'y':
        break
    clear()
    print(logo)
    game()
