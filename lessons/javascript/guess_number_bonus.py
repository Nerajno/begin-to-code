
while True:
    import random
    secret_number = random.randint(1, 10)
    counter = 0
    guess = int(input("I'm thinking of a number from 1-10. Pick one!"))
    while counter <= 3:
        if guess > secret_number:
            print("Nope. Too high! Keep guessing!")
        if guess < secret_number:
            print("Nope. Too low! Keep guessing!")
        if guess == secret_number:
            print("You got it!")
    guess = int(input("Go again? y or n"))
    counter = counter + 1
    if guess != "y":
            break
print("Bye bye!")
        
    


    


    

  
    '''

Stage 4
Make it so that the player can only guess 5 times at most. If they guessed 5 times and still miss, print "You used up all your guesses!".

Hint: you'll need to introduce the loop counter pattern into your code by adding a loop counter, and repeating condition, and a incrementer statement.
    
    
    
    '''