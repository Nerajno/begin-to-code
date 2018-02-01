# Lesson 12
## Dictionaries - Part 2

---
Welcome back! We have more dictionaries to cover.
In this lesson, we will really showcase the power of the
dictionary. Let's begin.
*****************************************************
## Section 1
### Bucket Accumulator Pattern

---
The first thing we are going to learn is another pattern.
*****************************************************
## Bucket Accumulator Pattern

The *bucket accumulator pattern* is similar to the accumulator
pattern, except that it accumulates to multiple "buckets" rather
than to just one accumulator variable. Each bucket corresponds
to an entry in a dictionary, and the key of the entry is what
uniquely identifies a bucket.

---

*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
print(tally)
```

---
This is a program that counts the number of times each
letter is used in the word "bananas". The program will
produce a count for the letter "b", a count for the
letter "a", another for the letter "n", and finally,
another for the letter "s".
*****************************************************

![Bananas 1](lessons/python/lesson-12/images/bananas-1.png)

---
This is how this program works. With start with the word
"bananas". Scanning letter to letter starting from the left.
*****************************************************

![Bananas 2](lessons/python/lesson-12/images/bananas-2.png)

---
The first letter is "b",
*****************************************************

![Bananas 4](lessons/python/lesson-12/images/bananas-4.png)

---
because we haven't encountered
this letter yet --- it is the first one, after all ---
we need to initialize a bucket (dictionary entry) for it,
and initialize the value to 0.
*****************************************************

![Bananas 5](lessons/python/lesson-12/images/bananas-5.png)

---
Then we immediately increment the count to 1, to account for
this instance of the letter "b".
*****************************************************

![Bananas 6](lessons/python/lesson-12/images/bananas-6.png)

---

The next letter is "a".
Same as last time, because haven't seen an "a" yet,
*****************************************************

![Bananas 7](lessons/python/lesson-12/images/bananas-7.png)

---
we
need to initialize the bucket,
*****************************************************

![Bananas 8](lessons/python/lesson-12/images/bananas-8.png)

---
and then increment its value to 1.
*****************************************************

![Bananas 9](lessons/python/lesson-12/images/bananas-9.png)

---
The next letter is "n".
*****************************************************

![Bananas 10](lessons/python/lesson-12/images/bananas-10.png)

---
Same thing: initialize a bucket for "n",
*****************************************************

![Bananas 11](lessons/python/lesson-12/images/bananas-11.png)

---
Increment its value.
*****************************************************

![Bananas 12](lessons/python/lesson-12/images/bananas-12.png)

---
Next we encounter another "a".

Because this time, we already have a bucket for the letter "a",
*****************************************************

![Bananas 13](lessons/python/lesson-12/images/bananas-13.png)

---
All we have to do is increment bucket a's value.
*****************************************************

![Bananas 14](lessons/python/lesson-12/images/bananas-14.png)

---
Next is "n". A bucket for "n" already exists.
*****************************************************

![Bananas 15](lessons/python/lesson-12/images/bananas-15.png)

---
So we increment bucket n's value.
*****************************************************

![Bananas 16](lessons/python/lesson-12/images/bananas-16.png)

---
Next, another "a".
*****************************************************

![Bananas 17](lessons/python/lesson-12/images/bananas-17.png)

---
Increment bucket a again.
*****************************************************

![Bananas 18](lessons/python/lesson-12/images/bananas-18.png)

---
Finally, "s". Because we haven't encountered an "s" yet,
*****************************************************

![Bananas 19](lessons/python/lesson-12/images/bananas-19.png)

---
We initialize a bucket for "s",
*****************************************************

![Bananas 20](lessons/python/lesson-12/images/bananas-20.png)

---
And then add 1 to its value.
*****************************************************
## Bucket Accumulator Pattern

```
{
    'b': 1,
    'a': 3,
    'n': 2,
    's': 1
}
```

---
This is the result of the program.

The counts are stored in a dictionary called `tally`.
Each entry in the dictionary represents a bucket.
The key of each entry is a letter, and the value of each
entry is a number that represents the count
for that letter.
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
print(tally)
```

---
Now, let's take a closer look at the code.
*****************************************************
## Bucket Accumulator Pattern

```python
[[string = "bananas"]][[set up the string]]
tally = {}
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
print(tally)
```

---
We have predefined the string to be processed to be "bananas".
This could have been taken from user input, if we preferred.
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
[[tally = {}]][[empty dictionary]]
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
print(tally)
```

---
The program starts by initializing an empty dictionary
to use to tally the results.
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
[[for letter in string:]][[loop through each letter]]
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
print(tally)
```

---
Then, it loops through each letter within the string.
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
for letter in string:
    [[if letter not in tally:]][[entry not initialized]]
        tally[letter] = 0
    tally[letter] += 1
print(tally)
```

---
This if statement checks to see if the dictionary already
contains an entry keyed by the current letter. In the
beginning, this will be false because we started out with
an empty dictionary.

So this statement says:

If it does *not* (notice the `not` operator) already
contain an entry for this letter,
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
for letter in string:
    if letter not in tally:
        [[tally[letter] = 0]][[initialize entry]]
    tally[letter] += 1
print(tally)
```

---
initialize the entry and sets its value to 0, to
start the count. This where our "bucket" is created.

In a normal accumulator pattern, this initialization
statement would have been done before the start
of the for loop. In the bucket accumulator pattern,
we do it on-demand --- as we encounter new letters.
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    [[tally[letter] += 1]][[accumulator statement]]
print(tally)
```

---
At this point we are guaranteed that an entry (bucket) for this letter
exists, and that it contains a numeric value, because we just
been through code that would initialize the entry in the case
that it didn't exist yet.

So, we can safely add 1 to the count,
using the `+=` operator, which is simply a short hand for:

```
tally[letter] = tally[letter] + 1
```

This --- you may recognize --- is the *accumulator statement*.
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
for letter in string:
[[    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1]][[for each letter]]
print(tally)
```

---
So it runs though this process for each letter in the string,
to eventually generate the final tally.
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
[[print(tally)]][[print the tally]]
```

---
At the end, the program prints
the tally.
*****************************************************
## Bucket Accumulator Pattern

```python
string = "bananas"
tally = {}
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
print(tally)
```

---
Run this code through Python Tutor. Pay close attention to
how the `tally` dictionary gets its entries updated.
*****************************************************
## Challenge

```python
string = "To be or not to be"
tally = {}
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
print(tally)
```

---
What if you had to handle different capitalization?
I've changed the input string to "To be or not to be". I expect
the threes t's to be counted into the same bucket. But with
this program as it is, it does not.

Try to make this program do that. The result
should be

```
{
    't': 3,
    'o': 4,
    ' ': 5,
    'b': 2,
    'e': 2,
    'r': 1,
    'n': 1
}
```

The next slide has the solution.
*****************************************************
## Solution

```python
string = "To be or not to be"
tally = {}
for letter in string:
    [[key = letter.lower()]][[lowercase the letter]]
    if key not in tally:
        tally[key] = 0
    tally[key] += 1
print(tally)
```

---
The trick is to lowercase the letter first, before
using it as the key.

I chose to use a new variable named `key`, so that we don't
confuse the letter itself with the key. If we wanted to
further change the relationship between a letter and the
key, we'd only have to change it in one place from this point on.
*****************************************************
## Applications of Bucket Accumulator Pattern

* Tallying by category (count)
* Greatest or Least in each category (min or max)
* Collect records in each category (list accumulator)

---
Just as the accumulator pattern can be used for a variety of
different tasks, the bucket accumulator pattern is also
extremely versatile.

Here, by category, I mean whatever attribute
you are using as the key of a bucket --- what key you select,
determines the set of buckets you'll end up with.

Let see another example, this time using lists as the
resulting values of each bucket.
*****************************************************
## The Sorting Hat

![Sorting hat](lessons/python/lesson-12/images/sorting-hat.png)

---

In the Harry Potter novel series, every student who attends
the Hogwarts School of Witchcraft and Wizardry must put on the
Sorting Hat which will "sort" them into one of four houses
of the school.
*****************************************************
## The Sorting Hat

```python
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
```

---
Here are some well known students from the novel, defined as
a list of records.

Each record contains the three attributes:

* name - the name of the character
* house - the house that they were predestined to be in
* book_intro - the book within the series where this character is introduced
*****************************************************
## The Sorting Hat

```python
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
```

---
We will write a program to simulate the process
of putting the Sorting Hat on each of these students and sorting
them into the four houses.

If you have a hunch, and prefer to try figuring this out yourself first,
you can do that now before going to the next slide.
*****************************************************
## The Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

---
This is the solution. Similarly to the letter tally
program, this one uses the bucket accumulator pattern.
Each bucket is a house of the school.
*****************************************************
## The Sorting Hat

```python
[[houses = {}]][[initialize empty dictionary]]
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

---
The dictionary variable has been named `houses` because it
will end up with exactly 4 entries --- one for each house.
We initialize it to an empty dictionary and let the houses
be created on-demand as we encounter students to be
sorted into them.
*****************************************************
## The Sorting Hat

```python
houses = {}
[[for character in harry_potter:]][[for each character]]
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

---
We loop through each character in the list.
*****************************************************
## The Sorting Hat

```python
houses = {}
for character in harry_potter:
    [[if character.house not in houses:]][[house uninitialized]]
        houses[character.house] = []
    houses[character.house].append(character)
```

---
Here, we use `character.house` as the key of the dictionary.
This is the name of the house that they are predestined to be
in.

This line says: if their house hasn't been initialized in
the `houses` dictionary,
*****************************************************
## The Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        [[houses[character.house] = []]][[initialize house]]
    houses[character.house].append(character)
```

---
then we'll initialize that dictionary entry to represent the house.
We'll initialize the value of the entry to an empty list, to which
students can be added.
*****************************************************
## The Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    [[houses[character.house].append(character)]][[accumulator statement]]
```

---
Now that the house where the student belongs exists, we can
add them to the house. This is the *accumulator statement*.
*****************************************************
## The Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

---
The end result of the program is that we have a `houses` dictionary,
which has 4 entries in it --- one for each house, keyed by each house's name.
The value of each entry is a list of the students within that house.
*****************************************************
## The Sorting Hat

```python
print("Ravenclaw student list:")
for student in houses["Ravenclaw"]:
    print(student.name)
```

Output:
```
Ravenclaw student list:
Luna Lovegood
Cho Chang
Moaning Myrtle
```

---
So now, if you want to see the list of students in Ravenclaw, you can
write a for loop like this.

Run this [code in Python Tutor](http://pythontutor.com/visualize.html#code=class%20Record%28object%29%3A%0A%20%20%20%20def%20__init__%28self,%20**kw%29%3A%0A%20%20%20%20%20%20%20%20self.__dict__.update%28kw%29%0A%0A%20%20%20%20def%20__repr__%28self%29%3A%0A%20%20%20%20%20%20%20%20return%20%22Record%25r%22%20%25%20self.__dict__%0A%0Aharry_potter%20%3D%20%5B%0A%20%20%20%20Record%28name%20%3D%20%22Harry%20Potter%22,%20house%20%3D%20%22Gryffindor%22,%20book_intro%20%3D%201%29,%0A%20%20%20%20Record%28name%20%3D%20%22Hermione%20Granger%22,%20house%20%3D%20%22Gryffindor%22,%20book_intro%20%3D%201%29,%0A%20%20%20%20Record%28name%20%3D%20%22Ron%20Weasley%22,%20house%20%3D%20%22Gryffindor%22,%20book_intro%20%3D%201%29,%0A%20%20%20%20Record%28name%20%3D%20%22Draco%20Malfoy%22,%20house%20%3D%20%22Slytherin%22,%20book_intro%20%3D%201%29,%0A%20%20%20%20Record%28name%20%3D%20%22Luna%20Lovegood%22,%20house%20%3D%20%22Ravenclaw%22,%20book_intro%20%3D%205%29,%0A%20%20%20%20Record%28name%20%3D%20%22Cedric%20Diggory%22,%20house%20%3D%20%22Hufflepuff%22,%20book_intro%20%3D%203%29,%0A%20%20%20%20Record%28name%20%3D%20%22Severius%20Snape%22,%20house%20%3D%20%22Slytherin%22,%20book_intro%20%3D%201%29,%0A%20%20%20%20Record%28name%20%3D%20%22Lord%20Voldemort%22,%20house%20%3D%20%22Slytherin%22,%20book_intro%20%3D%201%29,%0A%20%20%20%20Record%28name%20%3D%20%22Cho%20Chang%22,%20house%20%3D%20%22Ravenclaw%22,%20book_intro%20%3D%204%29,%0A%20%20%20%20Record%28name%20%3D%20%22Moaning%20Myrtle%22,%20house%20%3D%20%22Ravenclaw%22,%20book_intro%20%3D%203%29%0A%5D%0A%0Ahouses%20%3D%20%7B%7D%0Afor%20character%20in%20harry_potter%3A%0A%20%20%20%20if%20character.house%20not%20in%20houses%3A%0A%20%20%20%20%20%20%20%20houses%5Bcharacter.house%5D%20%3D%20%5B%5D%0A%20%20%20%20houses%5Bcharacter.house%5D.append%28character%29%0A%0Aprint%28%22Ravenclaw%20student%20list%3A%22%29%0Afor%20student%20in%20houses%5B%22Ravenclaw%22%5D%3A%0A%20%20%20%20print%28student.name%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) to see how it works. *I must warn you, the objects graph gets a bit complicated
with this example.*
*****************************************************
## The Sorting Hat

```python
print("Ravenclaw student list:")
for student in houses["Ravenclaw"]:
    print(student.name)
```

Output:
```
Ravenclaw student list:
Luna Lovegood
Cho Chang
Moaning Myrtle
```

---
This is the end of the section 1. If you'd like to do section 1
of the [homework](https://gist.github.com/airportyh/be75d7e49a5945519b5ce6a4fbdbbf0d) before moving on, you may do so now.
*************************************
## Section 2
### Iterating Dictionaries

---
Now that you have your buckets, you are probably thinking,
how do I go through all the buckets if I don't necessarily
know what the keys of the buckets are beforehand?

It turns out that you can iterate through the entries
of a dictionary just like you can iterate through
the items within a list.
*************************************
## for loop for dictionaries

```python
string = "bananas"
tally = {}
for letter in string:
    if letter not in tally:
        tally[letter] = 0
    tally[letter] += 1
```

---
Let's go back to the first example, as you may remember,
at the end of this program, the `tally` dictionary
should end up with
*************************************
## for loop for dictionaries

```
{
    'b': 1,
    'a': 3,
    'n': 2,
    's': 1
}
```

---
this value.
*************************************
## for loop for dictionaries

```python
for letter in tally:
    print(letter)
```

Output:
```
b
a
n
s
```

---
At this point, we can use the for loop to loop
through each key(letter) in the dictionary, like
this.

But what about the value(count)? You say.
*************************************
## for loop for dictionaries

```python
for letter in tally:
    [[count = tally[letter]]][[look up letter for count]]
    print(letter, ":", count)
```

---
Well you could look up the dictionary again, like so,
*************************************
## for loop for dictionaries

```python
for entry in tally.items():
    print(entry[0], ":", entry[1])
```

---
or you can use the `items()` method.
*************************************
## for loop for dictionaries

```python
for entry in [[tally.items()]][[returns a list of 2-tuples]]:
    print(entry[0], ":", entry[1])
```

---
The `items()` method of the dictionary returns
a list of 2-tuples: `(key, value)`.
Each 2-tuple represents one entry within the dictionary.
*************************************
## for loop for dictionaries

```python
[('b', 1), ('a', 3), ('n', 2), ('s', 1)]
```

---
For the example of "bananas", you'll get something that is
equivalent to this list of tuples.
*************************************
## for loop for dictionaries

```python
[[for entry in tally.items():]][[for each item]]
    print(entry[0], ":", entry[1])
```

---
So when you are iterating through each of these tuples,
*************************************
## for loop for dictionaries

```python
for entry in tally.items():
    print([[entry[0]]][[the key]], ":", entry[1])
```

---
The 0-th thing in the tuple is the key,
*************************************
## for loop for dictionaries

```python
for entry in tally.items():
    print(entry[0], ":", [[entry[1]]][[value]])
```

---
and the 1-st thing is the value.

But it gets better...
*************************************
## for loop for dictionaries

```python
for entry in tally.items():
    print(entry[0], ":", entry[1])
```

---
Instead of writing this,
*************************************
## for loop for dictionaries

```python
for letter, count in tally.items():
    print(letter, ":", count)
```

---
You could write this.
*************************************
## for loop for dictionaries

```python
for letter, count in tally.items():
    print(letter, ":", count)
```

---
WHAT???!!!
*************************************
## for loop for dictionaries

```python
for [[letter, count]][[this matches a 2-tuple]] in tally.items():
    print(letter, ":", count)
```

---
This expression here, matches a 2-tuple. So
it takes the 2 values within that tuple,
*************************************
## for loop for dictionaries

```python
for [[letter]][[0-th thing]], count in tally.items():
    print(letter, ":", count)
```

---
And assigns the 0-th thing in the tuple (`entry[0]`)
to `letter`.
*************************************
## for loop for dictionaries

```python
for letter, [[count]][[1-st thing]] in tally.items():
    print(letter, ":", count)
```

---
and the 1-st thing in the tuple (`entry[1]`) to `count`.
This short-hand transformation is called
*destructuring assignment* --- it undoes the structure
of the tuple into a number of variables.

What's good about this???
*************************************
## for loop for dictionaries

```python
for letter, count in tally.items():
    print(letter, ":", count)
```

---
While this code isn't necessarily shorter, it is easier
to read, because the variable names `letter` and `count`
are more descriptive and concrete than `entry`, `entry[0]`
and `entry[1]`.
*************************************
## Destructuring Assignment

```python
one, two = (1, 2)
```

---
In fact, you can use destructuring assignment
outside of the context of a for loop as well.
*************************************
## Destructuring Assignment

```python
one, two = (1, 2, 3)
```

ValueError: too many values to unpack (expected 2)

---
If you try to destructure to the wrong number of
variables, you get this error.
*************************************
## Destructuring Assignment

```python
result = divmod(5, 2)
```

`result` is `(2, 1)`

---
You can use destructuring assignment with the
outputs of functions too. For example, the `divmod`
function performs integer division. It returns a 2-tuple:
`(quotient, remainder)`.
*************************************
## Destructuring Assignment

```python
quotient, remainder = divmod(5, 2)
```

---
We can destructure the return value of the function
like so, so that we don't have to do any indexing
with the tuple, and this leads to more readable code.
*************************************
## Summary

* Bucket Accumulator Pattern
* for loop for dictionaries
* `items()` method
* Destructuring assignment

---
You made it to the end! This is what you've learned.
*************************************
## Homework

[Homework](https://gist.github.com/airportyh/be75d7e49a5945519b5ce6a4fbdbbf0d)

---
This is your homework. Enjoy!
