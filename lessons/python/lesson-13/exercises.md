# Lesson 13 Exercies

These are refactoring exercises. That means the
only thing you have to do is to *not* break stuff.

Just kidding :) You are suppose to make the code
better.

Test the program before you make any modifications.
After making each modification, retest it to make
sure it still works exactly as the original despite your
changes.

After each refactoring change you make, compare your
version to the original and ask yourself, is this better?

## Section 1: Extract Variable and Inline Temp

Use *extract variable* or *inline temp* or a
combination of the two to make the programs
below more readable.

### Celsius to Fahrenheit Converter

```python
c = float(input("How hot is it in °C? "))
print("%.02f°F is %.02f°C" % (c * 9 / 5 + 32, c))
```

### Sorting Hat

```python
class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

harry_potter = [
    Record(name = "Harry Potter", house = "Gryffindor", book_intro = 1),
    Record(name = "Hermione Granger", house = "Gryffindor", book_intro = 1),
    Record(name = "Ron Weasley", house = "Gryffindor", book_intro = 1),
    Record(name = "Draco Malfoy", house = "Slytherin", book_intro = 1),
    Record(name = "Luna Lovegood", house = "Ravenclaw", book_intro = 5),
    Record(name = "Cedric Diggory", house = "Hufflepuff", book_intro = 3),
    Record(name = "Severius Snape", house = "Slytherin", book_intro = 1),
    Record(name = "Lord Voldemort", house = "Slytherin", book_intro = 1),
    Record(name = "Cho Chang", house = "Ravenclaw", book_intro = 4),
    Record(name = "Moaning Myrtle", house = "Ravenclaw", book_intro = 3)
]

houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

### Idol Scores

```python
from functools import reduce

class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

contestant = Record(
        name = "Jelly Blockton",
        judge_scores = [9, 4, 7, 8, 10, 5],
        popular_score = 10)

# The final score is the average of the judge's scores combined
# with the popular_score. But the judge's scores has a 70% weight
# while the popular score only has a 30% weight.
def final_score(contestant):
    result = reduce(lambda a, b: a + b, contestant.judge_scores, 0) / len(contestant.judge_scores) * 0.7 + contestant.popular_score * 0.3
    return result

print("%s's final score is %.2f." % (contestant.name, final_score(contestant)))
```

## Section 2: Extract Function and Inline Function

Improve the following code by using *extract function*,
*inline function* or a combination. You may throw in an *extract variable*
and an *inline temp* too, if desired.

### Pig Latin

```python
phrase = input("Enter a phrase: ")

words = phrase.split(" ")
result_words = []
for word in words:
    pigword = ""
    state = "collect-consonants"
    first_consonants = ""
    for letter in word:
        if state == "collect-consonants":
            if not letter in "aeiou":
                first_consonants += letter
            else:
                state = "collect-rest"
                pigword += letter
        elif state == "collect-rest":
            pigword += letter
    pigword += first_consonants
    if first_consonants == "":
        pigword += "y"
    pigword += "ay"
    result_words.append(pigword)
result = " ".join(result_words)

print(result)
```

### Dead People

```python
class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

harry_potter = [
    Record(name = "Harry Potter", house = "Gryffindor", dead = False),
    Record(name = "Hermione Granger", house = "Gryffindor", dead = False),
    Record(name = "Ron Weasley", house = "Gryffindor", dead = False),
    Record(name = "Draco Malfoy", house = "Slytherin", dead = False),
    Record(name = "Luna Lovegood", house = "Ravenclaw", dead = False),
    Record(name = "Cedric Diggory", house = "Hufflepuff", dead = True),
    Record(name = "Severius Snape", house = "Slytherin", dead = True),
    Record(name = "Lord Voldemort", house = "Slytherin", dead = True),
    Record(name = "Cho Chang", house = "Ravenclaw", dead = True),
    Record(name = "Moaning Myrtle", house = "Ravenclaw", dead = True)
]

dead_per_house = {}
for student in harry_potter:
    if student.house not in dead_per_house:
        dead_per_house[student.house] = 0
    if student.dead:
        dead_per_house[student.house] += 1

house_with_most_dead = None
highest_dead_count = 0
for house, dead_count in dead_per_house.items():
    if house_with_most_dead == None or dead_count > highest_dead_count:
        house_with_most_dead = house
        highest_dead_count = dead_count

print("%s had the most dead people with %d." % (house_with_most_dead, highest_dead_count))
```

### Oh My Vowelness

```python
sentence = input("Enter a sentence: ")
words = sentence.split(" ")
result_words = []
for word in words:
    # Calculate vowelness score
    vowel_count = 0
    consonant_count = 0
    for letter in word:
        letter = letter.lower()
        if letter in "aeiou":
            vowel_count += 1
        elif letter in "abcdefghijklmnopqrstuvwxyz":
            consonant_count += 1
    score = vowel_count - consonant_count

    # Select color code
    if score >= 2:
        color_code = 35
    elif score >= 1:
        color_code = 34
    elif score >= 0:
        color_code = 36
    elif score >= -1:
        color_code = 32
    elif score >= -2:
        color_code = 33
    else:
        color_code = 31

    result_words.append("\033[%dm%s\033[0m" % (color_code, word))

result = " ".join(result_words)
print(result)
```

## Bonus Challenge: Strictly Come Dancing

```python
# This implements a simplified version of the Strictly Come Dancing
# scoring system. For more info:
# http://tv.bt.com/tv/strictly-come-dancing/voting-11364202272549
# https://www.youtube.com/watch?v=ZoA0u66wcSs

from functools import reduce

class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

contestants = [
    Record(name = "Mack", judge_scores = [9, 8, 6], audience_votes = 3481),
    Record(name = "Jane", judge_scores = [10, 9, 10], audience_votes = 9456),
    Record(name = "Amjad", judge_scores = [10, 8, 10], audience_votes = 1204),
    Record(name = "Manoush", judge_scores = [9, 8, 7], audience_votes = 4967),
    Record(name = "Anushka", judge_scores = [9, 8, 9], audience_votes = 2252),
    Record(name = "Jamal", judge_scores = [9, 8, 8], audience_votes = 12356),
    Record(name = "Karen", judge_scores = [6, 8, 5], audience_votes = 443),
    Record(name = "Lamar", judge_scores = [4, 5, 8], audience_votes = 4683)
]

numbers = {
    0: "first",
    1: "second",
    2: "third"
}

def judge_score(contestant):
    return reduce(lambda a, b: a + b, contestant.judge_scores, 0) / len(contestant.judge_scores)

judge_rank = sorted(contestants, key=judge_score, reverse=True)
audience_rank = sorted(contestants, key=lambda c: c.audience_votes, reverse=True)

for i in range(len(judge_rank)):
    contestant = judge_rank[i]
    contestant.judge_score = len(judge_rank) - i

for i in range(len(audience_rank)):
    contestant = audience_rank[i]
    contestant.audience_score = len(audience_rank) - i

final_rank = sorted(contestants, key=lambda c: c.judge_score + c.audience_score, reverse=True)

for i in range(3):
    print("The %s place winner is %s." % (numbers[i], final_rank[i].name))

```
