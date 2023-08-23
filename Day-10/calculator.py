from art import logo
from replit import clear


def calculation(first_number, next_number, operator):
    if operator == '+':
        return first_number + next_number
    elif operator == '-':
        return first_number - next_number
    elif operator == '*':
        return first_number * next_number
    elif operator == '/':
        return first_number / next_number


def calculator(number):
    operator = input("Pick a operation: ")
    next_number = float(input("What's the next number?: "))
    cal_number = calculation(number, next_number, operator)
    print(f"{number} {operator} {next_number} = {cal_number}")
    return cal_number


def main():
    clear()
    print(logo)
    first_number = float(input("What's the first number?: "))
    print("+\n-\n*\n/")
    cal_number = calculator(first_number)
    repeat = 'y'
    while repeat == 'y':
        repeat = input(
            f"Type 'y' to continue calculation with {cal_number} or type 'n' to start a new calculation:"
        )
        if repeat == 'n':
            main()
        cal_number = calculator(cal_number)


main()
