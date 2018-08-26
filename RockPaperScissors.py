
''' ROCK PAPER SCOSSORS '''
''' C NEWSON 26/08/2018 '''

## Initialise AI
ai = 'scissors'

user_weapon = input('Please select your weapon, rock, paper or scissors: ')

if ai == 'scissors' and user_weapon == 'rock':
    result = 'player wins'
elif ai == 'scissors' and user_weapon == 'paper':
    result = 'computer wins'
else:
    result = 'Draw'

print(result)
