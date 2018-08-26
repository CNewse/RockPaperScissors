''' ROCK PAPER SCOSSORS '''
''' C NEWSON 26/08/2018 '''

import random

## Set game rules and results (0 = draw, 1 = player wins, -1 = ai win)
def who_wins():  
    if ai_weapon == user_weapon:
        result = 0
    elif ai_weapon == 'scissors':
        if user_weapon == 'rock':
            result = 1
        elif user_weapon == 'paper':
            result = -1
    elif ai_weapon == 'paper':
        if user_weapon == 'rock':
            result = -1
        elif user_weapon == 'scissors':
            result = 1
    elif ai_weapon == 'rock':
        if user_weapon == 'paper':
            result = 1
        elif user_weapn == 'scissors':
            result = -1
    return result

num_games = int(input('How many games would you like to play?'))

##initialise lists to hold game results
ai_weapons = []
user_weapons = []
results = []

for i in range(num_games):
    ai_weapon = random.choice(['rock','paper','scissors'])
    user_weapon = input('\n Please select your weapon, rock, paper or scissors: ')
    ai_weapons.append(ai_weapon)
    user_weapons.append(user_weapon)
    results.append(who_wins())
    if who_wins() == 1:
        game_result = 'you win!'
    elif who_wins() == -1:
        game_result = 'you lose!'
    elif who_wins() == 0:
        game_result = "it's a draw"

    print('The computer chose', ai_weapon, game_result)

agg_results = {x:results.count(x) for x in results}

print('\n','Out of' ,num_games, 'you won', agg_results.get(1,None))
