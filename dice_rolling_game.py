#LOOP


# Dice Rolling Game
# Ask: roll the dice?
# Generate 2 random numers
# Print them
# If user enters n
# Print Thank You message
# Terminate
# Else
# Print invalid choice

import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing')
        break

    else: 
        print("Invalid Choice")
        continue