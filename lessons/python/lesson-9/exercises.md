# Lesson 9 Exercises

## Vowel Count

Write a `vowel_count(string)` function that counts the # of vowels for a given
string. It has one parameter:

1. `string` - the string to be counted

Return value: a number representing the number of vowels in the string.

After you've written this function.
Write some extra code to test this function in isolation and verify that
it works properly.

## Calculate Tips

Write a `calculate_tip(amount, service)` function that calculates gives
the amount of the tip given the amount of the bill and the quality of the
service. It has two parameters:

1. `amount` - a number representing the amount of the bill
2. `service` - a string which can be one of "good", "fair", and "poor". For
good service, 20% tip should be given; for fair service, 15% tip should be
given; and for poor service, 10% tip should be given.

Return value: a number representing the tip amount.

After you've written this function.
Write some extra code to test this function in isolation and verify that
it works properly.

## Unit Conversion

This is a program that helps you do unit conversion from metric to imperial
units:

```python
print("***************************")
print("* Unit Conversion Program *")
print("***************************")

print("1. Convert Liters to Gallons")
print("2. Convert Kilometers to Miles")
print("3. Convert Kilograms to Pounds")

choice = input("Choose one: ")
amount = float(input("Enter amount: "))

if choice == "1":
    result = convert_liter_to_gallons(amount)
elif choice == "2":
    result = convert_kilometers_to_miles(amount)
elif choice == "3":
    result = convert_kilograms_to_pounds(amount)

print("Answer: %.2f" % result)
```

The only problem is that it's missing some functions that it needs to do the
actual conversion. Please add the required functions to the beginning
of this program to make it work.

## Colorize My Words

You will write a program which asks the user to enter a phrase, and prints
the phrase back with each word colorized based on the *vowelness* score
of the word.

### Vowelness Score
The *vowelness score* of a word is its number of vowels minus its
number of consonants.

### Colorizing a Word

You will colorize each word based on its vowelness:

* 2 or greater - magenta
* 1 - blue
* 0 - cyan
* -1 - green
* -2 - yellow
* -3 or lower - red

### Printing Colors in the Terminal

As you may remember, you can print colored text in the terminal using
control codes like so:

```python
word = "bananas"
color_code = 33 # 33 is yellow
print("\033[%dm%s\033[0m" % (color_code, word))
```

Look at the Foreground (text) table on [this page](https://misc.flogisoft.com/bash/tip_colors_and_formatting) to find
what color code corresponds to what color.

### Breaking Up the Problem

Instead of tackling the entire problem head on. I recommend breaking it
down to a number of small problems, and solve each one as a function first.
What would each function do? What would the input and output of each
function be?

Plan this out ahead before you start implementing the functions. Come up
with a list of functions you'll need to solve the larger problem. For each
function, write:

1. its name
2. a description of what it does
3. a list of its inputs/parameters and a description of each one
4. its output/return value and a description of it

If you'd like, you can send this to your mentor(s) and get feedback on it
before you start implementing the code.

### Testing in Isolation

When working on individual functions, make sure you test each function in
isolation as you are working on it. When you've tested a function to your
satisfaction, only then should you move on.
