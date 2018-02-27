# Lesson 1 Exercises

## Convert the following Python Programs to JS

You may have the [cheatsheet](https://gist.github.com/airportyh/fee3aa986fb61f6da7c7b00c5ff4dc3b) printed out and have it next to you while you
do this.

### Tokyo Bay

```python
adult_count = int(input("how many adults are eating? "))
children_count = int(input("how many children are eating? "))
day_of_week = input("What day of the week is it? ")
if day_of_week == "Tuesday":
  total = adult_count * 15
else:
  total = adult_count * 15 + children_count * 10
print("It will cost you $%d to eat at Tokyo Bay." % total)
```

### Guess a Number

```python
secret_number = 6
guess = int(input("I'm thinking of a number from 1-10. Want to play?"))
while guess != secret_number:
    if guess > secret_number:
        print("Nope. Too high! Keep guessing!")
    if guess < secret_number:
        print("Nope. Too low! Keep guessing!")
    if guess == secret_number:
        break
    guess = int(input("Guess again!"))
    if guess == secret_number:
        break
```

### Total of The Odds

```python
scores = [7, 8, 9, 10, 5, 6, 7, 3, 4]
total = 0
for score in scores:
  if score % 2 == 1:
    total += score
print("Total of the odds: %d" % total)
```

### Reverse the Words

```python
phrase = input("Type a phrase: ")
words = phrase.split(" ")
result_words = []
for word in words:
    result_word = ""
    for letter in word:
        result_word = letter + result_word
    result_words.append(result_word)
result_phrase = " ".join(result_words)
print(result_phrase)
```

## Solve These Problems in JS

### Average the Numbers

```js
var numbers = [3, 9, 1, 5, 8, 9];
```

Given the above array of numbers, find its average and print it out.

### Vowel Swap

Ask the user to enter some text. Print the same text except:

* Change all a's to i's
* Change all e's to o's
* Change all i's to u's
* Change all o's to a's
* Change all u's to e's

### Title Case

Prompt the user to input a phrase. Print out the title-cased version
of the phrase (capitalize the first letter of each word). *Note: you may
find that JS doesn't have a title method. MUAHAHAHAHA!!!*

### Caesar Cipher

Ask the user to input a string and print the cipher text of the input using
the original Caesar Cipher: ROT13 --- using 13 as the key.

What is the Caesar Cipher? Read about it:
http://practicalcryptography.com/ciphers/caesar-cipher/
