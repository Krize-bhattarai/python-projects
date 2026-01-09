

# Ask the user to make a choice
# If choice is not valid, Print an error
# Let the computer to make a choice
# Print the choices with emojis
# Determine the winner
# Ask the user if they want to continue. If not Terminate

import random

emojis = {'R': '🪨', 'S': '✂️', 'P': '📃'}
choices = ('R', 'P', 'S')

while True:
    user_choice = input('Rock, Paper, or Scissors? (R/P/S): ').upper()
    if user_choice not in choices:
        print('Invalid Choice!')
        continue


    computer_choice = random.choice(choices)

    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')

    if user_choice == computer_choice:
        print('Tie')

    elif (user_choice == 'R' and computer_choice == 'S') or (user_choice == 'S' and computer_choice =='P') or (user_choice == 'P' and computer_choice =="R"):
        print('You Win')

    else:
        print('You Lose')

    while True:
        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'y':
            break
        elif should_continue == 'n':
            exit()
        else:
            print('Invalid Entry! Choose y or n only' )




