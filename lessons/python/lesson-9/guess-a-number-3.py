import random

number = 0
tries_left = 0
guess = 0
answer = "n"

def print_result():
    if number == guess:
        print("Yes! You win!")
    elif guess > number:
        print("%d is too high." % guess)
    else:
        print("%d is too low." % guess)

def play_game():
    global number
    global tries_left
    global guess
    number = random.randint(1, 10)
    tries_left = 5
    while True:
        print("I am thinking of a number between 1 and 10.")
        guess = int(input("What is your guess? (1-10) "))
        tries_left -= 1
        print_result()
        if number == guess:
            break
        if tries_left == 0:
            print("Ran out of guesses!!!")
            break

while True:
    play_game()

    answer = input("Play again? (Y/N) ")
    if answer.lower() != 'y':
        print("Bye!")
        break
