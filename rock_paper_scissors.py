from random import choice

def read_ratings(name):
    ratings = open('rating.txt', 'r')

    for line in ratings:
        if line.split()[0] == name:
            return int(line.split()[1])

    ratings.close()
    return 0
user_loss = {'rock':'paper', 'paper':'scissors', 'scissors':'rock'}
exit_option = '!exit'
rating_option = '!rating'
winning_cases = {
    'rock': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
    'fire': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
    'scissors': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
    'snake': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
    'human': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
    'tree': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
    'wolf': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
    'sponge': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
    'paper': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
    'air': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
    'water': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
    'dragon': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
    'devil': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
    'lightning': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
    'gun': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf']
}

name = input("Enter your name: ")
print(f'Hello, {name}')

game_score = read_ratings(name)
string = input()
current_options = []
if not string:
    current_options = ['rock', 'paper', 'scissors']
else:
    current_options = string.split(',')
print("Okay, let's start")
while True:
    user_guess = input()
    
    if user_guess == exit_option:
        print("Bye!")
        exit()
    elif user_guess == rating_option:
        print(f'Your rating: {game_score}')
    elif user_guess in current_options:
        computer_guess = choice(current_options)
        if computer_guess == user_guess:
            print(f"There is a draw ({computer_guess})")
            game_score += 50
        elif computer_guess in winning_cases[user_guess]:
            print(f"Well done. The computer chose {computer_guess} and failed")
            game_score += 100
        else:
            print(f"Sorry, but the computer chose {computer_guess}")           
    else:
        print("Invalid input")