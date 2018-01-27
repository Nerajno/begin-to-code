# Lesson 2.1 Exercises

## Section 1

### Hello Again?

Write a program to:

1. Ask the user for their name.
2. Say a greeting to them. (Phrase of your choice)
3. Repeat starting from \#1, unless they typed "Nobody" as their name.
  * If they typed "Nobody" as their name, end the program saying nothing.

### Do Another

Take a program you wrote for a previous assignment. Make it run
repeatedly.

After each run of the program, ask the user if they want to run it again.
If they typed "y", run the program again, if
they typed anything else, exist the program and print "Good bye!"

## Section 2: Loop Counter Pattern

1. Print the numbers between 1 to 10.
2. Print the numbers between 40 to 50.
3. Print the numbers between 1 to 10, but in reverse.
4. Print the even numbers from 2 to 20.
5. Ask the user for his name, say hello to him 10 times.
6. Ask the user for a number, print the numbers from 1 to that number.
7. Ask the user for a start number and an stop number. Print the numbers
starting from the start number and ending at the stop number.

## Guess A Number Game

You will write a guess-a-number game, where the player repeatedly guesses
numbers between 1 to 10 until they guess your secret number. You will
implement this game in these stages:

## Stage 1

Create a `secret` variable and set its value to your secret number ---
pick a number between 1 and 10. Use a while loop to repeatedly ask
the player for a guess. If the guess matches the secret number,
print "You win!", and end the loop. If the guess is wrong, print
"Wrong! Try again: " and ask for another guess.

## Stage 2

Extend to program to give hi-lo hints. If the guess is wrong and
is larger than the secret number, print "Wrong! Too high. Try again: ". It
it is wrong and less than the secret number, print "Wrong! Too low. Try again: ".

## Stage 3

Instead of hard-coding your secret number to a fixed number, use a
random number generator to pick one for you. To do this, you need
make two changes:

1. Add the line: `import random` to the top of your program
2. Where you define your `secret` variable, instead of setting its
value to a number, set its value to `random.randint(1, 10)` --- this
will give you a random number between 1 and 10, inclusive.

## Stage 4

Make it so that the player can only guess 5 times at most. If they guessed
5 times and still miss, print "You used up all your guesses!".

*Hint: you'll need to introduce the loop counter pattern into your code
by adding a loop counter, and repeating condition, and a incrementer statement.*

## Bonus Challenge 2

When a game is finished --- they either won or ran out of guesses. Given
them the option to play again.
