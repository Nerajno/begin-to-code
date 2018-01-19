# Lesson 10 Exercises

## Read a record

This is a record representing a child named alice.

```python
alice = Record(name="Alice", gender="female", age=7)
```

Write code to print the following sentence using the record
as defined above:

```
Alice is a 7 year old female.
```

## Write Some Records

For each member in your family, initialize a record to represent
them in the same manner as alice --- in Python, and then print
that same sentence description them for each of them.

What can you do to make your code less repetitive?

## Enter A Record

Write a program to ask the user to enter a person's name, gender, and age.
Save each value as an attribute in a record. Then, print the sentence
describing them.

Example run of the program:

```
Enter name: Arnav
Enter gender: male
Enter age: 6
Arnav is a 6 year old male.
```

## Enter More Records

Allow the user to enter any number of persons. After entering each person,
he can choose to enter another one. He can do this indefinitely, until he
decides to stop. At the end, print the sentence describing them.

This is an example run of the program:

```
Enter name: Arnav
Enter gender: male
Enter age: 6
Add another? (y/n) y
Enter name: Sasha
Enter gender: female
Enter age: 5
Add another? (y/n) y
Enter name: Diego
Enter gender: male
Enter age: 7
Add another? (y/n) n
Arnav is a 6 year old male.
Sasha is a 5 year old female.
Diego is a 7 year old male.
```

## The Dream Team

This is the 1994 USA Olympics basketball team. Arguably the greatest athletic
team ever assembled in the history of mankind --- in Python.

```python
barkley  = Record(name="Charles Barkley",    gp=6, pts=98, fgm=34, fga=58)
bird     = Record(name="Larry Bird",         gp=2, pts=19, fgm=8,  fga=11)
clyde    = Record(name="Clyde Drexler",      gp=5, pts=69, fgm=27, fga=39)
ewing    = Record(name="Patrick Ewing",      gp=5, pts=59, fgm=27, fga=43)
magic    = Record(name="Magic Johnson",      gp=6, pts=58, fgm=19, fga=34)
jordan   = Record(name="Michael Jordan",     gp=6, pts=76, fgm=29, fga=53)
laettner = Record(name="Christian Laettner", gp=6, pts=44, fgm=18, fga=31)
malone   = Record(name="Carl Malone",        gp=6, pts=89, fgm=33, fga=53)
mullin   = Record(name="Chris Mullin",       gp=6, pts=86, fgm=31, fga=49)
pippen   = Record(name="Scottie Pippen",     gp=6, pts=48, fgm=20, fga=30)
robinson = Record(name="David Robinson",     gp=6, pts=71, fgm=32, fga=42)
stockton = Record(name="John Stockton",      gp=2, pts=10, fgm=5,  fga=6 )

dream_team = [
    barkley, bird, clyde, ewing, magic, jordan, laettner,
    malone, mullin, pippen, robinson, stockton
]
```

As you can see, `dream_team` is a list containing each player of the team
as a record. Each player record has these attributes:

* name - the name of the player
* gp - # of games played
* pts - total # of points across all games played
* fgm - # of field goals (shots) made
* fga - # of field goals (shots) attempted

You will write code to answer the following questions --- one function each:

1. Which player scored the most points overall?
2. Which player made the most shots?
3. Which player took the most shots?
4. What is each player's field goal percentage (fgm / fga)?
5. What is each player's average points per game (pts / gp)?
6. Which player has the highest field goal percentage?
7. Which player has the highest points per game?

## Project Cost Estimator

You are planning a shopping list for project of some sort. You could use a
program to help you estimate the cost of the project.

Write a program that allow you to enter any number of items, their
estimated cost, and quantity. When you are done entering all of the items,
it gives you an estimated total cost.

Here is an example run of the program:

```
**************************************
* WELCOME TO PROJECT COST ESTIMATOR! *
**************************************
Enter name of an item: Glue
Enter estimated cost: 3.50
Enter quantity needed: 6

Summary
=======
Glue - $3.5 (6 qty)
---------------------------
Total estimated cost: $21.00

Enter another? (y/n) y
Enter name of an item: Borax
Enter estimated cost: 5.50
Enter quantity needed: 1

Summary
=======
Glue - $3.5 (6 qty)
Borax - $5.50 (1 qty)
---------------------------
Total estimated cost: $26.50

Enter another? (y/n) y
Enter name of an item: Glitter
Enter estimated cost: 3.00
Enter quantity needed: 1

Summary
=======
Glue - $3.5 (6 qty)
Borax - $5.50 (1 qty)
Glitter - $3.00 (1 qty)
---------------------------
Total estimated cost: $29.50

Enter another? (y/n) n
Bye!
```
