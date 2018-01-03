import random

while True:
    number = random.randint(1, 10)
    tries_left = 5
    while True:
        print("I am thinking of a number between 1 and 10.")
        guess = int(input("What is your guess? (1-10) "))
        tries_left -= 1
        if number == guess:
            print("Yes! You win!")
            break
        elif guess > number:
            print("%d is too high." % guess)
        else:
            print("%d is too low." % guess)
        if tries_left == 0:
            print("Ran out of guesses!!!")
            break

    answer = input("Play again? (Y/N) ")
    if answer.lower() != 'y':
        print("Bye!")
        break
