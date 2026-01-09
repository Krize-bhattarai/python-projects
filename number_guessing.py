# Generate fixed OR a random number
# Ask the user to make a guess
# If not a valid number, Print an error
# If number < guess, Print too Low
# If number > guess, Print too high
# Else, Print Well Done


# Project (Fixed Number)


guessing_number = 5

while True:
    guess = input("Guess the number between 1 and 9: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Enter numbers only")
        continue

    if guess == guessing_number:
        print("🎉 Well Done")
        break
    elif guess < guessing_number:
        print("Too Low")
    else:
        print("Too High")







    