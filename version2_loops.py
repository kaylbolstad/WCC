import random

def get_guess():
    guess = raw_input('Enter your guess: ')
    # Assume it's not valid, until it's proven otherwise
    valid = False
    while valid != True:
        try:
            # Try and convert this number to an integer
            # If it fails, the exception will occur
            guess = int(guess)
        except Exception:
            # Exception was thrown when trying to convert to number,
            # Report the issue and ask again
            print('Invalid input; please enter a whole number.')
            valid = False
            guess = get_guess()
        # If they get here, it means the number must have been valid
        # Set valid to be true to break out of the while loop
        valid = True
    return guess
# Test get_guess
print get_guess() # Expected: Keeps prompting until user enters a valid number
def compare(numA, numB):
    if numA > numB:
        return "high"
    else:
        return "low"

def play(min, max):
    # Pick a secret number
    secret_number = random.randint(min, max)
    print('TEMPORARY DEBUGGING HELPER -> The secret number is: ' + str(secret_number))
    # Print message at the start the game
    print("\nI'm thinking of a number between 1 and 100; what do you think it is? You have 5 guesses.")
    for guess_count in range(1,6):
        player_guess = get_guess()
        number_compare = compare(player_guess, secret_number)

        if number_compare == "high":
            print "Too high. Guess again."
        elif number_compare == "low":
            print "Too low. Guess again."
        elif player_guess == secret_number:
            print('You got it! The number was ' + str(secret_number))
            break
    if player_guess != secret_number:
        print "You guessed too many times, the number was " + str(secret_number) + "."

    # Print conclusion


# Run the game
play(1, 100)
