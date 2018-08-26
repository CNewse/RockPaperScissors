''' ROCK PAPER SCOSSORS '''
''' C NEWSON 26/08/2018 '''

import random

## Set game rules
def who_wins():  
    if ai == user_weapon:
        result = 'DRAW'
    elif ai == 'scissors':
        if user_weapon == 'rock':
            result = 'you win!'
        elif user_weapon == 'paper':
            result = 'you lose'
    elif ai == 'paper':
        if user_weapon == 'rock':
            result = 'you lose'
        elif user_weapon == 'scissors':
            result = 'you win!'
    elif ai == 'rock':
        if user_weapon == 'paper':
            result = 'you win!'
        elif user_weapn == 'scissors':
            result = 'you lose'
    return result

## Initialise AI
ai = random.choice(['rock','paper','scissors'])

user_weapon = input('Please select your weapon, rock, paper or scissors: ')

print('You chose', user_weapon)
print('The computer chose', ai, '\n')

print(who_wins())
