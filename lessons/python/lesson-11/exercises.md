# Lesson 11 Exercises

## Section 1

### Phone numbers

You have this dictionary which contains some phone number entries:

```python
phone_numbers = {
  "James": "945-394-2356",
  "Miranda": "648-384-2345"
}
```

Write some Python code in addition to this that accesses James'
phone number from this dictionary and prints it out. Then do
the same for Miranda.

## Write your own phone numbers

Make up your own dictionary containing your own phone numbers ---
you can make them up if you want.

### Add a Phone number

Write some code in addition to the above code to add a new
phone number entry to this dictionary.

### Number Exists?

Write some code in addition to the above code to as the user for
an person's name, and then print that person's phone number if
it exists, and prints "That person is not in the phone book."
if it doesn't exist.

## Section 2: Dictionary Translator Pattern

The dictionary below contains common shorthands people use in their texts.

```python
acronyms = {
  "LOL": "Laughing Out Loud",
  "LMAO": "Laughing my a$$ off",
  "ROFL": "Rolling On Floor Laughing",
  "TY": "Thank You",
  "TYVM": "Thank You Very Much",
  "OMG": "Oh My God",
  "TTYL": "Talk To You Later"
}
```

### Translate Text

Sarah doesn't understand these acronyms, and would like to have a Python program
that translates it into human language for her. Write a program that translates
texts such as

```
omg lol
```

to there expanded form. The input above would yield:

```
Oh My God Laughing Out Loud
```

While, we are at it, write this as a function.

## Section 3

Come up with a topic that you are interested in. Write a program to
manage an encyclopedia in that topic. You will use a while loop to
repeatedly ask the user to enter a new term and definition, or to look up
an existing term. This is an example run of this application:

```
***************************
* Welcome to Rubix-pedia! *
***************************
Would you like to:
1. Enter a term
2. Look up a term
? 1

What is the term? F2L
What is F2L? First 2 layers
Ok. Stored entry for F2L!

Would you like to:
1. Enter a term
2. Look up a term
? 1
What is the term? algorithm
What is algorithm? a prescribed sequence of moves
Ok. Stored entry for algorithm!

Would you like to:
1. Enter a term
2. Look up a term
? 2
What term to look up? algorithm
algorithm is a prescribed sequence of moves

Would you like to:
1. Enter a term
2. Look up a term
? 2
What term to look up? side piece
Sorry, we don't have a definition for side piece
```
