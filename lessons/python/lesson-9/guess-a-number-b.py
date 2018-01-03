import random

def print_game_result(number, guess):
    if number == guess:
        print("Yes! You win!")
    elif guess > number:
        print("%d is too high." % guess)
    else:
        print("%d is too low." % guess)

def get_guess():
    print("I am thinking of a number between 1 and 10.")
    guess = int(input("What is your guess? (1-10) "))
    return guess

def play_game():
    number = random.randint(1, 10)
    tries_left = 5
    while True:
        guess = get_guess()
        tries_left -= 1
        print_game_result(number, guess)
        if number == guess:
            break
        if tries_left == 0:
            print("Ran out of guesses!!!")
            break

def play_again():
    answer = input("Play again? (Y/N) ")
    return answer.lower() == 'y'

while True:
    play_game()
    if not play_again():
        print("Bye!")
        break
