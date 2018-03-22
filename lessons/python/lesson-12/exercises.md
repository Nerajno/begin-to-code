# Lesson 12 Exercises

## Section 1: Bucket Accumulator Pattern

0. Write a function `number_tally(numbers)` that takes a list of numbers,
and counts how many times each number has appeared in the list. The
return value should be a dictionary, where the key of each entry is a number
in the list, and the value of each entry is a number representing the
number of times that word appeared.
1. Write a function `word_tally(phrase)` that takes a phrase as a string, and
counts how many times each word in the phrase has appeared. The return value
should be a dictionary, where the key of each entry is a word in the phrase,
and the value of each entry is a number representing the number of times
that word appeared.
2. Write a function `shelf_books(books)` that takes a list of strings ---
each string is the title of a book, and shelf each book into the correct
shelf based on its first letter. I.e. there is a shelf A, shelf B, shelf C,
..., shelf Z. The return value should be a dictionary representing all
of the shelfs that are needed. Each entry represents a shelf: the key is the
shelf letter, the value is a list containing the title of all books that
belong to that shelf.

### Basketball

It's basketball time again!!!

*If you'd rather do problems based on Dr.Who or what have you,
send in your own records and problem set. Have your mentor approve and/or
revise them, and work on those instead.*

```python
class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

# pos - position:
#    C - Center
#    PF - Power Forward
#    SF - Small Forward
#    SG - Shooting Guard
#    PG - Point Guard
# team - home team of the player
# PTS - total # of points across all games played

barkley  = Record(name="Charles Barkley",    pos="PF", team="Suns",        pts=98)
bird     = Record(name="Larry Bird",         pos="SF", team="Celtics",     pts=19)
clyde    = Record(name="Clyde Drexler",      pos="SG", team="Blazers",     pts=69)
ewing    = Record(name="Patrick Ewing",      pos="C",  team="Knicks",      pts=59)
magic    = Record(name="Magic Johnson",      pos="PG", team="Lakers",      pts=58)
jordan   = Record(name="Michael Jordan",     pos="SG", team="Bulls",       pts=76)
laettner = Record(name="Christian Laettner", pos="PF", team="Blue Devils", pts=44)
malone   = Record(name="Carl Malone",        pos="PF", team="Jazz",        pts=89)
mullin   = Record(name="Chris Mullin",       pos="SF", team="Warriers",    pts=86)
pippen   = Record(name="Scottie Pippen",     pos="SF", team="Bulls",       pts=48)
robinson = Record(name="David Robinson",     pos="C",  team="Spurs",       pts=71)
stockton = Record(name="John Stockton",      pos="PG", team="Jazz",        pts=10)

dream_team = [
    barkley, bird, clyde, ewing, magic, jordan, laettner,
    malone, mullin, pippen, robinson, stockton
]
```

You have all the members of the USA 1994 Olympics team, a.k.a The Dream Team,
arranged as a list of records. Write a function to answer each of the following:
(each function should return a dictionary)

1. What is the total number of points scored for each position?
  (key: position name, value: total score)
2. How many players are there for each position?
  (key: position name, value: # of players)
3. Group the players by their home teams.
  (key: home team, value: list of players)
4. Build a histogram of the number of points the players scored:
    * How many scored between 0 - 10 points?
    * How many scored between 11 - 20 points?
    * 21 - 30 points?
    * 31 - 40 points?
    * 41 - 50 points?
    * and so on...
Return a dictionary where each entry represents a range of 10 points. The
key of 10 represents the range between 0 - 10, 20 represents the range between
11 - 20, and so on. The value is a number representing the number of players
who scored within that range.
5. Who is the the highest number of points scored for each position?

*Look for continuation of these problems in section 2 below.*

## Section 2: Looping Through Dictionaries

### Wheels on the Bus

The children's song Wheels on the Bus has many verses, but every verse
has the same structure:

```
The (noun) on the bus go (three word phrase),
(three word phrase),
(three word phrase).
The (noun) on the bus go (three word phrase),
all through the town.
```

For example, the first verse has "wheels" as the *noun* and "round and round"
as the *three word phrase*, and it goes like this:

```
The wheels on the bus go round and round,
round and round,
round and round.
The wheels on the bus go round and round,
all through the town.
```

You are given this dictionary which contains a number of entries. Each entry
has the noun as the key, and the three word phrase as the value. Write code
to generate all the verses of the song using this dictionary:

```python
song_substitutions = {
    "wheels": "round and round",
    "wipers": "swish, swish, swish",
    "horn": "beep, beep, beep",
    "money": "click, click, click",
    "driver": "move on back",
    "baby": "wah, wah, wah",
    "mommy": "shush, shush, shush"
}
```

### More Basketball

1. Take your solution \#1 from the basketball exercise, take the return
value of the function, loop through the entries of the dictionary and print
each out. Example:

```
The high scorer at position C is David Robinson.
The high scorer at position PF is Charles Barkley.
The high scorer at position SF is Chris Mullin.
The high scorer at position SG is Michael Jordan.
The high scorer at position PG is Magic Johnson.
```

2. Take your solution \#2 - \#5 from the basketball, loop through the dictionary
to print the results.
