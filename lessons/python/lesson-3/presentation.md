# Lesson 3
## Lists, Ranges and the For Loop
---
In this lesson, we'll cover lists, ranges and the for loop.
******************************************
## Lists

```python
[1, 5, 2, 3, 4]
```
---
This is a list of numbers in Python
******************************************

![List Representation](lessons/python/lesson-3/list-repr-python-tutor.png)

---
This is how you would see a list represented inside of Python Tutor. 
First there's the label that says "list", that tells you this is a 
list, to differentiate it from other things that we'll learn later.

Then we have something that looks like like a row of cells, 
and each cell has a little index number -
that's the gray number on the top left corner of each cell. Here
the index numbers are 0, 1, 2, 3, 4 - they always go in order, starting
from 0 - if you hear the term zero-based indexing, that is referring to
lists, or arrays, or other things whose index number sequence start from zero. 

Then, the numbers in black in each cell are the contents of each cell. A cell
is like a variable that stores something, and a list is like a row of variables.
But a list can grow and shrink, so it could hold any number of cells.
*****************************************
## Lists
```python
a_list = [1, 5, 2, 3, 4]
```
---
You can store a list into a variable like so,
as you can with any other kind of value in Python.
*****************************************

![List Variable](lessons/python/lesson-3/list-variable.png)

---
When you have a list variable, what you would see
in Python Tutor is this - a variable slot inside
the frame in the "Frames" section pointing to a
representation of the list in the "Objects" section
like so.

"What is the Frames section and what is the
Objects section?" - you might be wondering.

The Frames
section is like the short-term memory of the brain, 
whereas the Objects section is like the long-term
memory of the brain - we'll revisit this later
when we get to functions.

At this point, notice
that the value of a list variable is not the contents
of the list, but merely a pointer to a "list object"
in the Object area - that has profound implications,
which we'll discover later.
*****************************************
## Accessing an item
```python
a_list[1]
```
---
To access an individual item inside a list, tell the
list the index number you want to access by using the subscript notation. 

The way to say this expression is: 

    a_list subscript 1
    
Another way to say this is:

    Access a_list at index 1

This expression returns the content of cell number 1,
which is our example, is 5 (look one slide back).

******************************************
## What will this print?
```python
a_list = [1, 5, 2, 3, 4]
print a_list[1]
print a_list[3]
print a_list[4]
print a_list[2]
print a_list[0]
```
---
It's time for a challenge! What will this program print?
Write out your prediction, on a piece or paper or 
a text editor. Then run this program to verify it.
*****************************************
## Accessing an non-existent cell
```python
a_list = [1, 5, 2, 3, 4]
print a_list[5]
```

```
IndexError: list index out of range
```
---
If you try to access an item by an index number that
does not exist in the list, you will get an error. More
specifically, an IndexError. This our example, there
isn't a cell with the index number of 5.
*****************************************
## Appending to a list

```python
a_list.append(7)
```
Result:

![Append result](lessons/python/lesson-3/append-result.png)

---
You can append a new item to a list using the append
method of the list, like so.
*****************************************
## Deleting from a list

```python
del a_list[1]
```
Result:

![Delete result](lessons/python/lesson-3/delete-result.png)

---
You can also delete an item from a list by the item's
index number.
*****************************************
## A list of strings
```python
parts = ['head', 'shoulders', 'knees', 'toes']
```

---
Lists can contain any data type, not just numbers.
*****************************************
## A mixed list
```python
part1 = ['head', 1]
part2 = ['shoulders', 2]
part3 = ['knees', 2]
part4 = ['toes', 10]
```

---
You can also have different types(kinds) of things
in the same list.
*****************************************
## A list of lists
```python
parts = [
  ['head', 1],
  ['shoulders', 2],
  ['knees', 2],
  ['toes', 10]
]
```


---
You can even have lists of lists!!! 

![Mindblown](lessons/python/lesson-3/mindblown.gif)

What would this
even look like in Python Tutor? I leave this as an
exercise for the reader:

Predict what it would look like, draw it on paper. Then
run this program in Python Tutor to verify.
*****************************************
## For loop
```
a_list = [1, 5, 2, 3, 4]
for item in a_list:
  print item
```
---
Let's talk about for-loops now. In Python - as opposed
to other programming languages - a for loop is used to
iterate through a list of items.
*****************************************
## For loop
```
a_list = [1, 5, 2, 3, 4]
for [[item]][[This declares a new variable called item]] in a_list:
  print item
```
---
Like the while loop, a for loop has a loop body.
The for-in statement does 2 things simultaneously:

1. declares a variable - in this case the variable item
2. sets the value of that variable to one of the items each time through the body of the loop
*****************************************
