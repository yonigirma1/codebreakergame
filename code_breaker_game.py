#code breaker Game

import random

def get_input():
    '''
    Ask user for a guess number to be compared with the
    generated code by the computer
    '''
    return list(input("What is your guess: "))

def generate_num():
    '''
    This function makes the computer create a random
    three digit number
    '''
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return digits[:3]


def generate_clues(code, user_guess):
    '''
    Compares the user_guess with the code and gives
    clues based on parameters given
    '''
    if user_guess == code:
        return 'CODE CRACKED'

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append('Match')
        elif num in code:
            clues.append('Close')
    if clues == []:
        return 'Nope'
    else:
        return clues

print("Welcome Code Breaker! Let's see if you can guess my 3 digit number!")

secret_code = generate_num()
print("A code has been created. Please guess 3 digit number")

clues_report = []

while clues_report != 'CODE CRACKED':
    guess = get_input()

    generate_clues(secret_code, guess)
    print("Here is the result of your guess:")
    for clue in clues_report:
        print(clue)
