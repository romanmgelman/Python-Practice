from random import shuffle

# SHUFFLES THE LIST
def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

# GETS INPUT AND RETURNS THE PLAYER'S GUESS
def player_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input('Enter 0, 1, or 2: ')
    return int(guess)

# CHECKS IF THE GUESSED INDEX CONTAINS THE BALL AND RETURNS AN ANSWER
def check_guess(cups, guess):
    if cups[guess] != 'o':
        print('Not right!')
        print(cups)
    else:
        print('You guessed it!')
        print(cups)

def cups_game():
    # WHOLE PROGRAM PUT TOGETHER
    # INITIAL LIST
    cups = [' ', 'o', ' ']
    # SHUFFLE LIST
    shuffled_cups = shuffle_list(cups)
    # USER GUESS
    guess = player_guess()
    # CHECK GUESS
    check_guess(shuffled_cups, guess)

cups_game()