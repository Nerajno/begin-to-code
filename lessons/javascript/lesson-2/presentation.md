# JavaScript 2

---
Well come back for some JavaScript! Seeing that you are
unfazed by the first lesson, we will continue.
******************************************************
## Section 1
# Function and forEach

---
******************************************************
## Function

Python
```python
def hello(subject):
  return "Hello, " + subject + "!"
```

JS
```js
function hello(subject) {
  return "Hello, " + subject + "!";
}
```

---
This is a function in JS verse the same thing in Python.
******************************************************
## Function

Python
```python
[[def]][[def statement]] hello(subject):
  return "Hello, " + subject + "!"
```

JS
```js
[[function]][[function statement]] hello(subject) {
  return "Hello, " + subject + "!";
}
```

---
Instead of a `def` statement, JS has uses the `function`
statement.
******************************************************
## Function

Python
```python
def hello(subject):
  return "Hello, " + subject + "!"
```

JS
```js
function hello(subject) {
  [[return]][[return statement]] "Hello, " + subject + "!";
}
```

---
You have the `return` statement in JS just as Python
does.
******************************************************
## Function

Python
```python
def hello(subject):
  return "Hello, " + subject + "!"
```

JS
```js
function hello(subject) [[[{]]]
  return "Hello, " + subject + "!";
[[[}]]]
```

---
And lest you forget --- of course --- the curly brackets
for blocks, instead of indentation.
******************************************************
## Not Enough Arguments

JS
```js
function hello(subject) {
  return "Hello, " + subject + "!";
}

console.log(hello());
```

---
One thing to watch out for in JS is that if you supply
fewer arguments than a function needs: *it won't tell you!*
******************************************************
## Not Enough Arguments

JS
```js
function hello(subject) {
  return "Hello, " + subject + "!";
}

console.log(hello[[()]][[zero arguments sent]]);
```

---
This call to the `hello` function provides zero arguments.
******************************************************
## Not Enough Arguments

JS
```js
function hello[[(subject)]][[one argument needed]] {
  return "Hello, " + subject + "!";
}

console.log(hello());
```

---
But `hello` needs one parameter. So what happens?
******************************************************
## Not Enough Arguments

JS
```js
function hello([[subject]][[will be undefined]]) {
  return "Hello, " + subject + "!";
}

console.log(hello());
```

---
The unsupplied parameter will be initialized to the
value of `undefined` --- the equivalent of `None` in
Python.
******************************************************
## Not Enough Arguments

JS
```js
function hello(subject) {
  return [["Hello, " + subject]][["Hello, undefined"]] + "!";
}

console.log(hello());
```

---
The result of concatenating a string with an `undefined`
value is we'll get a string "undefined" added on to
the string on the left-hand side. Weird? Huh?

It turns out that if you try to concatenate anything that's
not a string with a string, JS first converts the non-string
into a string, then concatenates them. The conversion
for `undefined` is the string "undefined".
******************************************************
## Not Enough Arguments

JS
```js
function hello(subject) {
  return "Hello, " + subject + "!";
}

console.log(hello());
```

Output:

```
Hello, undefined!
```

---
The end result of this program is "Hello, undefined!".
******************************************************
## Python: Not Enough Arguments

Python
```python
def hello(subject):
  return "Hello, " + subject + "!"

print(hello())
```

Output:
```
TypeError: hello() missing 1 required positional argument: 'subject'
```

---
In contrast, in Python you'll get an error when you
try to call the function with too few arguments, telling
you what your mistake was.
******************************************************
## Not Enough Arguments

JS
```js
function hello(subject) {
  return "Hello, " + subject + "!";
}

console.log(hello());
```

Output:

```
Hello, undefined!
```

---
Because of behavior like this, JS tends to be harder
to debug. If you see unexpected undefined values
within a string or within other error messages, you'll
need to track backwards to find where the `undefined`
value originated from.

Often times it comes from passing too few arguments
to a function.
******************************************************
## For loops

Python
```python
for number in numbers:
  print(number)
```

---
Let's talk about for loops again.
******************************************************
## For loops

Python
```python
for number in numbers:
  print(number)
```

JS
```js
for (var i = 0; i < numbers.length; i++) {
  var number = numbers[i];
  console.log(number);
}
```

---
Last time you saw the JS version of the for loop.
And you were --- understandably --- terrified.

To us old-hat programmers, this was as natural as
drinking water!

Luckily for you, the JS programmers of the world
realized that they could learn a thing or two from
Python, and they invented...
******************************************************
## For Each Method

Python
```python
for number in numbers:
  print(number)
```

JS
```js
numbers.forEach(function(number) {
  console.log(number);
});
```

---
The `forEach` method!

The `forEach` method isn't a statement in JS, but rather
a method of the array, the same way that `slice` is a
method of an array.
******************************************************
## For Each Method

Python
```python
for number in numbers:
  print(number)
```

JS
```js
[[numbers]][[must be an array]].forEach(function(number) {
  console.log(number);
});
```

---
Note: this means `forEach` only works with arrays.
In particular, it doesn't work with strings. If you
have a string, you could use `split` to convert it
to an array, and then use `forEach`.
******************************************************
## For Each Method

Python
```python
for number in numbers:
  print(number)
```

JS
```js
numbers.forEach([[function(number) {
  console.log(number);
}]][[function as an argument]]);
```

---
The interesting thing about the `forEach` method is that
it takes a function as its first argument.

*You: What??? You can do that?*

Me: Yes. Yes you can. It will call that function once
for each item in the array.

You:

![Mind blown](lessons/javascript/lesson-2/images/mindblown.gif)
******************************************************
## For loops

Python
```python
for number in numbers:
  print(number)
```

JS
```js
numbers.forEach(function([[number]][[one item in the array]]) {
  console.log(number);
});
```

---
Each time, it will pass a different number within the array to this
function as its first parameter.
******************************************************
## For loops

Python
```python
for [[[number]]] in numbers:
  print(number)
```

JS
```js
numbers.forEach(function([[[number]]]) {
  console.log(number);
});
```

---
Thus the `number` parameter is this inlined function
has the same role as the `number` variable in the
Python for loop.
******************************************************
## For loops

Python
```python
for number in numbers:
[[[  print(number)]]]
```

JS
```js
numbers.forEach(function(number) [[[{
  console.log(number);
}]]]);
```

---
And the body of the inlined function has the same role
as Python's for loop body.
******************************************************
## For loops

Python
```python
for number in numbers:
  print(number)
```

JS
```js
numbers.forEach(function(number) {
  console.log(number);
});
```

---
The idea of passing a function as an argument may seem foreign. But it is
one of the main techniques used in functional programming, which we will
cover in more detail in a later lesson.
******************************************************
## For loops

JS for loop
```js
for (var i = 0; i < numbers.length; i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

JS forEach method
```js
numbers.forEach(function(number) {
  console.log(number);
});
```

---
You may choose to use the `forEach` method or JavaScript's for loop, or
even the while loop --- any of them will get the job done.
The advantage of `forEach` is that you don't have to manage your
own counter, similarly to with Python's for loop.
******************************************************
## For loops

JS for loop
```js
for (var i = 0; i < numbers.length; i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

JS forEach method
```js
numbers.forEach(function(number) {
  console.log(number);
}[[)]][[closing parenthesis]];
```

---
If you use the `forEach` method, make sure you close the parenthesis, to
match the
******************************************************
## For loops

JS for loop
```js
for (var i = 0; i < numbers.length; i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

JS forEach method
```js
numbers.forEach[[(]][[opening parenthesis]]function(number) {
  console.log(number);
});
```

---
opening parenthesis here.
******************************************************
## For loops

JS for loop
```js
for (var i = 0; i < numbers.length; i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

JS forEach method
```js
numbers.forEach(function(number) {
  console.log(number);
})[[;]][[ending semicolon]]
```

---
and end the statement with a semicolon, while we are at it.

This is the end of section one. You may do the [corresponding
homework](https://gist.github.com/airportyh/51a065de029903dee8c55d634e3bdb93) before you move on to the next slide.
******************************************************
## Section 2
# Object

---
Now we'll talk about objects in JS. Although we haven't
covered objects before, you are really more familiar
with it than you think.
******************************************************
### Object as Record

Python
```python
banana = Record(
  name = "banana",
  calories = 105,
  fat = 0.4,
  sodium = 1,
  sugar = 14
)
```

JS
```js
var banana = {
  name: "banana",
  calories: 105,
  fat: 0.4,
  sodium: 1,
  sugar: 14
};
```

---
The object is JS's replacement for our `Record` class Python.

Rather than having to use a class definition for `Record` as you did
in Python, JavaScript's object is a built-in language feature,
so you can use it out of the box.
******************************************************
### Object as Record

Python
```python
banana = [[[Record(]]]
  name = "banana",
  calories = 105,
  fat = 0.4,
  sodium = 1,
  sugar = 14
[[[)]]]
```

JS
```js
var banana = {
  name: "banana",
  calories: 105,
  fat: 0.4,
  sodium: 1,
  sugar: 14
};
```

---
In place of calling the `Record` constructor,
******************************************************
### Object as Record

Python
```python
banana = Record(
  name = "banana",
  calories = 105,
  fat = 0.4,
  sodium = 1,
  sugar = 14
)
```

JS
```js
var banana = [[[{]]]
  name: "banana",
  calories: 105,
  fat: 0.4,
  sodium: 1,
  sugar: 14
[[[}]]];
```

---
You use the curly brackets to surround the key/value pairs.
******************************************************
### Object as Record

Python
```python
banana = Record(
  name [[[=]]] "banana",
  calories [[[=]]] 105,
  fat [[[=]]] 0.4,
  sodium [[[=]]] 1,
  sugar [[[=]]] 14
)
```

JS
```js
var banana = {
  name: "banana",
  calories: 105,
  fat: 0.4,
  sodium: 1,
  sugar: 14
};
```

---
And instead of using assignment operators to assign each pair,
******************************************************
### Object as Record

Python
```python
banana = Record(
  name = "banana",
  calories = 105,
  fat = 0.4,
  sodium = 1,
  sugar = 14
)
```

JS
```js
var banana = {
  name[[[:]]] "banana",
  calories[[[:]]] 105,
  fat[[[:]]] 0.4,
  sodium[[[:]]] 1,
  sugar[[[:]]] 14
};
```

---
In JS object notation, you use colons.
******************************************************
## Accessing an Entry

Python
```python
banana.calories
```

JS
```JS
banana.calories
```

---
Accessing an entry by key in JS uses the same syntax as
Python.
******************************************************
## Accessing an Object Property

Python
```python
banana.[[calories]][["calories" attribute]]
```

JS
```JS
banana.calories
```

---
Whereas in Python, the name on the right of dot operator
is called an attribute,
******************************************************
## Accessing an Object Property

Python
```python
banana.calories
```

JS
```JS
banana.[[calories]][["calories" property]]
```

---
In JS it is called a property of an object.
******************************************************
## Modifying an Object Property

Python
```python
banana.calories = 284
```

JS
```js
banana.calories = 284;
```

---
Modify an object property is also the same syntactically
as Python.
******************************************************
## Object as Dictionary

Python
```python
lookup = {
  "LOL": "Laugh out loud",
  "OMG": "Oh my god"
}
```

JS
```JS
var lookup = {
  "LOL": "Laugh out loud",
  "OMG": "Oh my god"
};
```

---
You might have noticed earlier that the syntax for the object
looked suspiciously like a dictionary.

It turns out the JS object also doubles as a dictionary!
******************************************************
## Object as Dictionary

Python
```python
lookup = {
  "LOL": "Laugh out loud",
  "OMG": "Oh my god"
}
```

JS
```JS
var lookup = {
  [[["]]]LOL[[["]]]: "Laugh out loud",
  [[["]]]OMG[[["]]]: "Oh my god"
};
```

---
In JS, the quotes around the keys on the right-hand side
are optional, as long as the value of the key itself has
no spaces or special characters and is a valid variable name
--- although it is not technically a variable.
******************************************************
## Object as Dictionary

Python
```python
lookup = {
  "LOL": "Laugh out loud",
  "OMG": "Oh my god"
}
```

JS
```JS
var lookup = {
  [[[LOL]]]: "Laugh out loud",
  [[[OMG]]]: "Oh my god"
};
```

---
So for this example, since `LOL` and `OMG` *could* both be
variable names, we can omit the quotes.
******************************************************
## Lookup by Key

Python
```python
lookup["LOL"]
```

JS
```js
lookup["LOL"]
```

---
The syntax for a lookup by a key is the same.
******************************************************
## Modify or Adding

Python
```python
lookup["LOL"] = "Lots of Laughs"
```

JS
```js
lookup["LOL"] = "Lots of Laughs";
```

---
The syntax for modifying or adding an entry is the same
as well.
******************************************************
## Testing Existence

Python
```python
if "LOL" in lookup:
  print("It's in there!")
```

JS
```js
if ("LOL" in lookup) {
  console.log("It's in there!");
}
```

---
The syntax for checking if a key exists in the dictionary
is the same.
******************************************************
## Iterating the Entries

Python
```python
for key, value in lookup.items():
  print("%s translates to %s" % (key, value))
```

JS
```js
for (var key in lookup) {
  var value = lookup[key];
  console.log(key + " translates to " + value);
}
```

---
The syntax for iterating through the entries of a dictionary
is slightly different.

Because JS doesn't support the `items` method like Python,
we need to look through just the keys, and then use
the object to lookup the value for each key within the loop.
******************************************************
## Iterating the Entries

Python
```python
for key, value in lookup.items():
  print("%s translates to %s" % (key, value))
```

JS
```js
for (var key in lookup) {
  var value = lookup[key];
  console.log(key + " translates to " + value);
}
```

---
This is a different variant of the for loop in JS.
It's the for-in loop, but it works a little differently
from Python's for-in loop. I recommend using
this only when dealing with an object as a dictionary.
******************************************************
## Example: Sorting Hat

Python
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
Let's redo the sorting hat example from [lesson 12](/#python/lesson-12)
in JS.

In Python, we have a list of records. Let's convert this to JS...
******************************************************
## Example: Sorting Hat

JS
```js
var harryPotter = [
    { name: "Harry Potter", house: "Gryffindor":  book_intro: 1 },
    { name: "Hermione Granger", house: "Gryffindor", book_intro: 1 },
    { name: "Ron Weasley", house: "Gryffindor", book_intro: 1 },
    { name: "Draco Malfoy", house: "Slytherin", book_intro: 1 },
    { name: "Luna Lovegood", house: "Ravenclaw", book_intro: 5 },
    { name: "Cedric Diggory", house: "Hufflepuff", book_intro: 3 },
    { name: "Severius Snape", house: "Slytherin", book_intro: 1 },
    { name: "Lord Voldemort", house: "Slytherin", book_intro: 1 },
    { name: "Cho Chang", house: "Ravenclaw", book_intro: 4 },
    { name: "Moaning Myrtle", house: "Ravenclaw", book_intro: 3 }
];
```

---
This --- rather than a list of records --- is an *array* of *objects*.
******************************************************
## Example: Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

---
To sort these characters, we want to use the bucket accumulator
pattern. This is the Python version of the code. Let's
convert it to JS line by line.
******************************************************
## Example: Sorting Hat

```python
[[[houses = {}]]]
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

```js
[[[var houses = {};]]]
```

---
Whereas in Python we create an empty dictionary, in JS
we create an empty object. Easy.
******************************************************
## Example: Sorting Hat

```python
houses = {}
[[[for character in harry_potter:]]]
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

```js
var houses = {};
[[[harryPotter.forEach(function(character) {

});]]]
```

---
Now, to convert this for loop in Python, because in the
JS version, `harryPotter` is an array, we can
use the `forEach` method to simulate Python's for loop.
******************************************************
## Example: Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

```js
var houses = {};
harryPotter.forEach(function(character) {
  [[[ ]]]
});
```

---
Again, we'll match the brackets and the parenthesis and then
move the cursor back into the block to avoid forgetting to
close them.
******************************************************
## Example: Sorting Hat

```python
houses = {}
for character in harry_potter:
    [[[if character.house not in houses:]]]
        houses[character.house] = []
    houses[character.house].append(character)
```

```js
var houses = {};
harryPotter.forEach(function(character) {
  [[[if (!(character.house in houses)) {

  }]]]
});
```

---
For detecting if the character's house is already in the
houses object, we can use the `in` operator, but JS doesn't
have a `not in` syntax.
******************************************************
## Example: Sorting Hat

```js
var houses = {};
harryPotter.forEach(function(character) {
  if (!([[[character.house in houses]]])) {

  }
});
```

---
So instead we have to test if the house is `in` `houses`,
******************************************************
## Example: Sorting Hat

```js
var houses = {};
harryPotter.forEach(function(character) {
  if ([[!]][[not operator]](character.house in houses)) {

  }
});
```

---

and then use the not operator
`!` to flip the result from a true to a false or a false to
a true.
******************************************************
## Example: Sorting Hat

```js
var houses = {};
harryPotter.forEach(function(character) {
  if (![[[(]]]character.house in houses[[[)]]]) {

  }
});
```

---
These parenthesis are needed here because the `!` operator
has higher precedence than the `in` operator.

We need to put them here to avoid the `!` operator being
applied to `character.house` before it is applied to the `in`
operator.
******************************************************
## Example: Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

```js
var houses = {};
harryPotter.forEach(function(character) {
  if (!(character.house in houses)) {
    [[[ ]]]
  }
});
```
---
Back to the conversion...
******************************************************
## Example: Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        [[[houses[character.house] = []]]]
    houses[character.house].append(character)
```

```js
var houses = {};
harryPotter.forEach(function(character) {
  if (!(character.house in houses)) {
    [[[houses[character.house] = [];]]]
  }
});
```
---
The next line is identical except for the semicolon.
******************************************************
## Example: Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    [[[houses[character.house].append(character)]]]
```

```js
var houses = {};
harryPotter.forEach(function(character) {
  if (!(character.house in houses)) {
    houses[character.house] = [];
  }
  [[[houses[character.house].push(character);]]]
});
```
---
The next line --- outside of the if statement now ---
is mostly the same, except we convert the `append` method
to the `push` method.
******************************************************
## Example: Sorting Hat

```python
houses = {}
for character in harry_potter:
    if character.house not in houses:
        houses[character.house] = []
    houses[character.house].append(character)
```

```js
var houses = {};
harryPotter.forEach(function(character) {
  if (!(character.house in houses)) {
    houses[character.house] = [];
  }
  houses[character.house].push(character);
});
```
---
And that's it!
******************************************************
## Example: Sorting Hat

```js
var houses = {};
harryPotter.forEach(function(character) {
  if (!(character.house in houses)) {
    houses[character.house] = [];
  }
  houses[character.house].push(character);
});

[[[for (var house in houses) {
  var charactersInHouse = houses[house];
  console.log(house);
  console.log(charactersInHouse);
}]]]
```

---
So that we can see the results
easily --- the Python Tutor visualization for
this example is a mess --- let's loop through
the houses and print out the characters.

Run this code in Python Tutor and see how it works.
******************************************************
## Summary

* functions
* the `forEach` method
* object as record
* object as dictionary

---
That's it for this lesson. This is what you've learned.
******************************************************
## Homework

[Enjoy your Homework](https://gist.github.com/airportyh/51a065de029903dee8c55d634e3bdb93)

---
