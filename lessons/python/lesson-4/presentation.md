# Lesson 4
## String Manipulation
---
This lesson we'll talk more about strings
and lists.
*****************************
```python
a_long_string = 'The quick brown fox jumps over...'
```
---
A common problem in computer science is given a long string of text,
how can you find specific words within it? In this lesson, we'll
consider this, and other similar problems.

First we'll learn some new abilities of strings and lists.
*****************************
## String Indexing
```python
a_string = 'apricot'
print(a_string[0])
```
This prints 'a'

---
It turns out that you can index the characters of a string the same way
you index the items of a list.
*****************************
## String Indexing
```python
a_string = 'apricot'
print(a_string[2])
print(a_string[3])
print(a_string[5])
print(a_string[6])
```
This prints
```
r
i
o
t
```
---
Here's another example.
*****************************
## Looping through a string
```python
a_string = 'apricot'
for char in a_string:
  print(char)
```
This prints
```
a
p
r
i
c
o
t
```
---
You can also loop through each character of a string using a for-loop.
*****************************
## Looping through a string II
```python
a_string = 'apricot'
for idx in range(len(a_string)):
  print(a_string[idx])
```
This prints
```
a
p
r
i
c
o
t
```
---
Alternatively you can create a range based on the length of the string.
*****************************
## Slicing (substrings)
```python
print(a_string[3:5])
```
---
You can get a slice - or a substring - of a string using this slice syntax.
The slice syntax is an extension of the subscript syntax.
*****************************
## Slicing (substrings)
```python
print(a_string[[[3]][[The start index (inclusive)]]:5])
```
---
To the left of the colon is the start index, and it is inclusive.
*****************************
## Slicing (substrings)
```python
print(a_string[3:[[5]][[The end index (non-inclusive)]]])
```
---
To the right of the colon is the end index, and it is non-inclusive.
This feels a little bit like a range, doesn't it?
*****************************
## Slicing Example
```python
a_fruit = 'purple mangosteen'
print(a_fruit[7:12])
```
This prints
```
mango
```
---
Here is a complete example of string slicing in action.
*****************************
## Slicing example
```python
a_fruit = 'purple mangosteen'
print(a_fruit[7:])
```
This prints
```
mangosteen
```

---
You can optionally omit the end index, which causes the slice to
go all the way to the end.
*****************************
## Slicing example
```python
a_fruit = 'purple mangosteen'
print(a_fruit[:6])
```
This prints
```
purple
```
---
Likewise, you can optionally omit the start index, which makes it start at 0.
*****************************
## List Slicing
```python
a_list = [
  'Manny', 'Arnav', 'Juan',
  'Manoush', 'Joshua'
]
print(a_list[2:4])
```
This prints
```
['Juan', 'Manoush']
```
---
It turns out that slicing also works for lists!!
Another handy tool to put in your toolbox.
****************************
## String Spliting
```python
a_string = 'Manny,Arnav,Juan,Manoush,Joshua'
```
---
Now for a challenge, imagine that you were given this string containing a list
of names, each name separated by a comma. If you wanted to do something with
each name in this list - say, simply print each name one on a line, how would
you do it?

Hint: you can loop though the string using an index similar to the previous
slide titled "Looping through a string II". Imagine how you would write this
code - but you don't have to actually do it.
****************************
## String Splitting
```python
a_list = a_string.split(',')
```
---
If you couldn't figure out how to solve the challenge, don't fret. Python has
made it easy for you. Simply use the `split` function available on the string
type.
****************************
## String Splitting
```python
a_list = [[a_string]][[The string we want to split]].split(',')
```
---
To use the split function, first we write the string or a variable containing
the string we intend to split. It could also be any arbitrary expression that
evaluates to a string.
****************************
## String Splitting
```python
a_list = a_string[[.]][[The dot operator]]split(',')
```
---
Then we use the dot notation to tell Python that we are invoking a function
on that particular string.
****************************
## String Splitting
```python
a_list = a_string.[[split]][[The split function]](',')
```
---
Then, to the right of the dot we write the name of the function we are invoking,
in this case, split.
****************************
## String Splitting
```python
a_list = a_string.split[[(',')]][[The parameter list]]
```
---
Then, to the right of that, we list the arguments passed to the split function.
****************************
## String Splitting
```python
a_list = a_string.split([[',']][[The separator]])
```
---
We are passing one argument to split, telling it the separator to use,
in this case, we want to use the comma. Split will now split
out a substring everytime it sees a comma in a_string.
****************************
## String Splitting
```python
[[a_list]][[Output is a list of strings]] = a_string.split(',')
```
---
The result of the split operation is a list of strings.
****************************
## String Splitting
```python
a_string = 'Manny,Arnav,Juan,Manoush,Joshua'
a_list = a_string.split(',')
print(a_list)
```
Output:
```
['Manny', 'Arnav', 'Juan', 'Manoush', 'Joshua']
```
---
This is the complete example.
****************************
## Question
```python
a_string = 'Manny,Arnav,Juan,Manoush,Joshua'
a_list = a_string.split('J')
print(a_list)
```
What is the output?

---
What would happen if we split on the letter 'J' instead?

Come up with an
answer on your own, and then verify it by running this program.
***************************
## String Joining
```python
a_string = ','.join(a_list)
```
---
The inverse operation of split is join.
***************************
## String Joining
```python
a_string = [[',']][[The separator]].join(a_list)
```
---
In contrast to split, with join, we start with the separator on the left.
***************************
## String Joining
```python
a_string = ','[[.]][[Dot operator]]join(a_list)
```
---
then the dot operator,
***************************
## String Joining
```python
a_string = ','.[[join]][[the join function]](a_list)
```
---
then the join function
***************************
## String Joining
```python
a_string = ','.join([[a_list]][[a list of strings]])
```
---
Then we pass a list to it as its argument. It is assumed that the list
contains strings. If the list contains something other than strings,
this will fail.
***************************
## String Joining
```python
[[a_string]][[A string]] = ','.join(a_list)
```
---
The result of the operation is a string.
***************************
## String Joining
```python
a_list = ['Apple', 'Kiwi', 'Banana', 'Orange']
a_string = '*'.join(a_list)
print(a_string)
```
---
What is the result of this program? Write it down on paper, and then verify it by
running the program.
***************************
## Sorting a List
```python
a_list = ['Apple', 'Kiwi', 'Banana', 'Orange']
```
---
One last tool I want to put in your toolbox is list sorting.

Given that you have a list like this,
***************************
## Sorting a List
```python
a_list.sort()
```
---
to rearrange the list in alphabetical order, all you have to do is to invoke
the sort function like so.
***************************
## Sorting a List
```python
a_list = ['Apple', 'Kiwi', 'Banana', 'Orange']
a_list.sort()
print(a_list)
```
Output:
```
['Apple', 'Banana', 'Kiwi', 'Orange']
```
---
This is the full example.
***************************
## Sorting a List
```python
a_list = [98, 42, 28, 78, 12, 5]
a_list.sort()
print(a_list)
```
Output:
```
[5, 12, 28, 42, 78, 98]
```
---
It works for lists of numbers as well. In fact, it works for any data type
that can reasonably be sorted.
***************************
## Example 1
