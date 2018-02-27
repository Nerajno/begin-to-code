# JavaScript 1

---
Welcome to day 1 of JavaScript! New pupil!

For this course, I will assume you have basic knowledge
of HTML and CSS and is able to use them to self-sufficiently
build web pages that do what you want them to do. If you do
not have that ability yet, my apologies, but you should
come back when you've acquired them.

Today, you will be inundated with JavaScript knowledge.
Now that you have a solid foundation of the fundamental
programming concepts, I know you can handle it.

Are you ready?
*****************************************************
## Installing the Chrome Web Browser

[Install Google Chrome](http://chrome.google.com)

---
For this course, I recommend installing the Chrome
Web Browser. If you don't have this software on your
computer already, please install it.
******************************************************
## A HTML Page with JavaScript

`index.html`
```html
<script>
console.log("Hello world!");
</script>
```

---
This is a minimalistic web page --- `index.html` ---
that contains executable JavaScript. I know this is
probably not what you are used to. You are probably
more familiar with HTML code that look like...
******************************************************
## An HTML Page

```html
<!doctype html>
<html>
  <head>
    <title>Welcome to my Corner of the World Wide Web!!!</title>
  </head>
  <body>
    <h1>Welcome to my Corner of the World Wide Web!!!</h1>
    <p>Please have a look around!</p>
  </body>
</html>
```

---
This. But for the time being, we are going to leave the header
tags and paragraph tags alone, and focus on JavaScript. Please
bare with me.

So...

******************************************************
## A HTML Page with JavaScript

`index.html`
```html
[[[<script>]]]
console.log("Hello world!");
[[[</script>]]]
```

---
We will only have one tag --- a script tag.
******************************************************
## A HTML Page with JavaScript

`index.html`
```html
<script>
console.log("Hello world!");
[[[</script>]]]
```

---
Make sure you get the close tag right! It has a slash (`/`) before the "s".
******************************************************
## A HTML Page with JavaScript

`index.html`
```html
<script>
[[console.log("Hello world!");]][[This is JavaScript!!!]]
</script>
```

---
And inside of that script tag, we write JavaScript.

And when you load the page, it will execute that JavaScript!
It's *that* simple.
******************************************************
## A HTML Page with JavaScript

`index.html`
```html
<script>
console.log("Hello world!");
</script>
```

---
Type up this `index.html` file, store it in a directory
of your choosing, and then open it up using Google Chrome...
******************************************************
## Load Page
There are open the `index.html`:

1. Drag the `index.html` file from your finder or file
explorer into the Chrome browser window.
2. Within the Chrome application, go to `File` ->
`Open File...`, and then locate the `index.html`.
3. If you've changed your default browser to Chrome, then simply
double-clicking the `index.html` will open it in Chrome.
---
Once, you've done one of these things...
******************************************************
## Load Page

![Load Page](lessons/javascript/lesson-1/images/load-page.png)

---
You should see something like this.
******************************************************
## Load Page

![Load Page](lessons/javascript/lesson-1/images/load-page.png)

---
We have a blank page...
******************************************************
## Load Page

![Load Page](lessons/javascript/lesson-1/images/load-page.png)

---
Yes!!! We have a blank page. That's what we made. But it's a
blank page that runs JavaScript. Let's open the JavaScript
console to find some evidence that the JavaScript has ran.
******************************************************
## JS Console

![Open JS Console](lessons/javascript/lesson-1/images/open-dev-tools.png)

---
To do that, we'll open the JavaScript console by going to `View` -> `Developer`
-> `JavaScript Console`. Alternatively, you can use the keyboard shortcut
displayed next to the `JavaScript Console` menu item. I recommend learning
this shortcut because it is easy to learn and will help you be more efficient
in the future.
******************************************************
## JS Console

![JS Console](lessons/javascript/lesson-1/images/js-console.png)

---
Once it is open, the JS console should look like this! And it should
say "Hello, world!". And if it did, that's *your* program doing that!

Try to make it print a different text in the console. Reload the page,
and see the updated result.
******************************************************
## JS in Python Tutor

![JS in Python Tutor](lessons/javascript/lesson-1/images/js-in-python-tutor.png)

---
Another way to run your JavaScript is in Python Tutor!!!

That's right! The Python Tutor you've grown to love. Despite the name,
Python Tutor actually supports multiple languages, including JavaScript.

Make sure you change the "Write code in" selection to "JavaScript ES6".

Oh, and don't put the script tags `<script>` `</script>` in there ---
only the JavaScript.
******************************************************
## Syntactical Differences

* Blocks
* Parenthesis for conditionals
* Semicolons

---
Python and JavaScript share a lot of common features, so JavaScript
will not seem alien to you, I don't think. But there are some
overall differences in syntax that will appear over and over again
, and I want to highlight those first.

*Let's jump into some JavaScript!*
******************************************************
## Blocks in JS

Python
```python
if age >= 21:
  print("You may come in.")
```

JS
```js
if (age >= 21) {
  console.log("You may come in.");
}
```

---
The first one is blocks.
******************************************************
## Blocks in JS

Python
```python
if age >= 21:
[[[→→print("You may come in.")]]]
```

JS
```js
if (age >= 21) {
  console.log("You may come in.");
}
```

---
In Python, blocks are the parts of code that
are indented.
******************************************************
## Blocks in JS

Python
```python
if age >= 21:
  print("You may come in.")
```

JS
```js
if (age >= 21) [[[{
  console.log("You may come in.");
}]]]
```

---
In JavaScript, however, blocks start and end with matching curry brackets.
******************************************************
## Blocks in JS

Python
```python
if age >= 21:
  print("You may come in.")
```

JS
```js
if (age >= 21) {
[[[→→]]]console.log("You may come in.");
}
```

---
Although the indentation is not necessary in JavaScript, I recommend always
indenting anyway for readability's sake.
******************************************************
## Blocks in JS

```js
if (age >= 21) {
if (height >= 48) {
console.log("You may come in.");
} else {
console.log("You are not at the minimum height.");
}
}
```

---
For example,
This code --- although is perfectly valid JavaScript --- is harder to
parse (for humans, I mean)...
******************************************************
## Blocks in JS

```js
if (age >= 21) {
  if (height >= 48) {
    console.log("You may come in.");
  } else {
    console.log("You are not at the minimum height.");
  }
}
```

---
then this properly indented version.
******************************************************
## Blocks in JS: A Tip

```js
if (age >= 21) {
  [[[ ]]]
}
```

---
In JS, curly brackets (`{}`) are used a lot, and they tend to nest multiple
levels deep. If you have a mismatch between the open bracket and a closing
bracket, it can be difficult to troubleshoot the error.

A habit that helps you reduce mistakes and save time is this:

As you are typing, always type both the opening bracket and the
closing brackets first, and then move your cursor back into the block
to type the statement(s) within the block. This ensures that you don't
forget to close the block.

Onward to the next syntactical difference...
******************************************************
## Parenthesis for Conditionals

```python
if age >= 21:
  print("You may come in.")
```

```js
if [[[(]]]age >= 21[[[)]]] {
  console.log("You may come in.");
}
```

---
The second syntactical difference is the mandatory parenthesis
around the conditional clause of an if statement, a while statement,
a for loop statement, and more. This set of parenthesis is optional in Python.
******************************************************
## Semicolons

```python
if age >= 21:
  print("You may come in.")
```

```js
if (age >= 21) {
  console.log("You may come in.")[[[;]]]
}
```

---
The third syntactical difference is the ending semicolons.
Each statement in JavaScript --- other than blocks --- should have an
ending semicolon. Although technically this ending semicolon is optional,
I recommend always writing this semicolon anyway because the majority of
of the community conforms to this norm.
******************************************************
## Things You've Learned

* Printing
* Variables
* Prompting
* String formatting
* Operators
* If statements
* While loops
* Lists
* For loops
* Split and joining strings

---
Here is an overview of some of the concepts you've learned in Python.
Each of these concepts exists in JavaScript, either directly or indirectly as
something under a different name. The fundamental concept is the same,
all you have to do is the translation.

For each concept, I will give you an example in Python, and then
the equivalent in JavaScript. Let's jump right into it.
******************************************************
## Printing

Python
```python
print("Hello, world!")
```

JS
```js
console.log("Hello, world!");
```

---
First up is printing. In Python you use the `print` function,
in JS you use the `log` method of the `console` object.
******************************************************
## Printing

Python
```python
print("Hello, world!")
```

JS
```js
console.log("Hello, world!")[[[;]]]
```

---
Also note the semicolon.
******************************************************
## Variables

Python
```python
name = "Camila"
age = 6
```

JS
```js
var name = "Camila";
var age = 6;
```

---
This is Python's variable initialization vs the same in JS.
******************************************************
## Variables

Python
```python
name = "Camila"
age = 6
```

JS
```js
[[[var]]] name = "Camila";
[[[var]]] age = 6;
```

---
In JS the `var` statement is required to declare a variable.
******************************************************
## Prompting

Python
```python
name = input("What is your name? ")
```

JS
```js
var name = prompt("What is your name? ");
```

---
To prompt the user for input in JS, instead of the `input` function,
you use the `prompt` function.
******************************************************
## Number Conversion

Python
```python
age = int(input("How old are you? "))
```

JS
```js
var age = Number(prompt("How old are you? "));
```

---
And if you need to convert a user input to a number, you the `Number` function.
JS does not distinguish between int and float.
******************************************************
## String Formatting

Python
```python
name = "Camila"
age = 6
print("Hello %s! You are %d years old!" % (name, age))
```

JS
```js
var name = "Camila";
var age = 6;
console.log("Hello " + name + "! You are " + age + "years old!");
```

---
String formatting: Python has string formatting...
******************************************************
## String Formatting

Python
```python
name = "Camila"
age = 6
print("Hello %s! You are %d years old!" % ([[[name]]], [[[age]]]))
```

JS
```js
var name = "Camila";
var age = 6;
console.log("Hello " + name + "! You are " + age + "years old!");
```

---
where dynamic values are substituted into
******************************************************
## String Formatting

Python
```python
name = "Camila"
age = 6
print("Hello [[[%s]]]! You are [[[%d]]] years old!" % (name, age))
```

JS
```js
var name = "Camila";
var age = 6;
console.log("Hello " + name + "! You are " + age + "years old!");
```

---
Their respective locations in the format string.
******************************************************
## String Formatting

Python
```python
name = "Camila"
age = 6
print("Hello %s! You are %d years old!" % (name, age))
```

JS
```js
var name = "Camila";
var age = 6;
console.log("Hello " [[[+]]] name [[[+]]] "! You are " [[[+]]] age [[[+]]] "years old!");
```

---
JS has no such feature :(

So you have to use string concatenation to piece together bits of string into
one longer string to be printed.
******************************************************
## String Formatting

Python
```python
name = "Camila"
age = 6
print("Hello %s! You are %d years old!" % (name, age))
```

JS
```js
var name = "Camila";
var [[[age = 6]]];
console.log("Hello " + name + "! You are " + [[[age]]] + "years old!");
```

---
Note that in this example, `age` is a number, not a string. In this case,
JS will use type coercion to convert the number to a string first, before
concatenating it with the surrounding strings.
******************************************************
### If Statement

Python
```python
if age >= 21:
  print("You may come in.")
elif age >= 18:
  print("Wait a few years.")
else:
  print("Where is your mommy?")
```

JS
```js
if (age >= 21) {
  console.log("You may come in.");
} else if (age >= 18) {
  console.log("Wait a few years.");
} else {
  console.log("Where is your mommy?");
}
```

---
The if statement in JS has the same structure as if statements in Python.
******************************************************
### If Statement

Python
```python
if age >= 21:
  print("You may come in.")
elif age >= 18:
  print("Wait a few years.")
else:
  print("Where is your mommy?")
```

JS
```js
if [[[(]]]age >= 21[[[)]]] {
  console.log("You may come in.");
} else if [[[(]]]age >= 18[[[)]]] {
  console.log("Wait a few years.");
} else {
  console.log("Where is your mommy?");
}
```

---
Notice the mandatory parenthesis around the conditional clauses.
******************************************************
### If Statement

Python
```python
if age >= 21:
  print("You may come in.")
elif age >= 18:
  print("Wait a few years.")
else:
  print("Where is your mommy?")
```

JS
```js
if (age >= 21) [[[{]]]
  console.log("You may come in.");
[[[}]]] else if (age >= 18) [[[{]]]
  console.log("Wait a few years.");
[[[}]]] else [[[{]]]
  console.log("Where is your mommy?");
[[[}]]]
```

---
and the curly brackets around the code blocks: the consequent clauses and the
alternate clause.
******************************************************
## Equal Comparison

Python
```python
if guess == secret_number:
  print("You won!")
```

JS
```js
if (guess === secretNumber) {
  console.log("You won!");
}
```

---
To test for equality, Python has the `==` operator.
******************************************************
## Equal Comparison

Python
```python
if guess == secret_number:
  print("You won!")
```

JS
```js
if (guess [[===]][[triple equals]] secretNumber) {
  console.log("You won!");
}
```

---
JS also has an `==` operator, but due to the unpredictable way in
with it works when it compares values of different types, the community
at large has decided to shun it and use the more strict `===` operator
in its place.

I recommend the same --- we won't mention the `==` operator again.
******************************************************
## CamelCased Names

Python
```python
if guess == secret_number:
  print("You won!")
```

JS
```js
if (guess === secretNumber) {
  console.log("You won!");
}
```

---
Another difference to mention about this code is the difference in
variable naming conventions. For variable names that are multi-word phrases,
the Python community prefers to use snake_case: which
connects_words_together_with_underscores. But in the JavaScript community,
developers prefer to use camelCase: where
wordsAreAllCaptializedAndThenJammedTogether. Thus the difference between
the `secret_number` in the Python version vs the `secretNumber` in the JS
version.
******************************************************
## Operators

| Operation      | Python | JavaScript |
|----------------|--------|------------|
| Assignment     | =      | =          |
| Equal          | ==     | ===        |
| Add            | +      | +          |
| Subtract       | -      | -          |
| Multiply       | *      | *          |
| Divide         | /      | /          |
| Modulus        | %      | %          |
| Integer Divide | //     | NA         |
| Power          | **     | `Math.pow(base, exp)` |
| Logical and    | `and`  | `&&`       |
| Logical or     | `or`   | `||`       |

---
JS has most of the common operators that Python has, but not all of them.
******************************************************
## While loop

Python
```python
counter = 1
while counter <= 10:
  print(counter)
  counter += 1
```

JS
```js
var counter = 1;
while (counter <= 10) {
  console.log(counter);
  counter += 1;
}
```

---
The while loop in JS is basically the same as Python.
******************************************************
## List / Array

Python
```python
numbers = [1, 2, 5, 6, 7]
```

JS
```js
var numbers = [1, 2, 5, 6, 7];
```

---
In JS, lists are called arrays, but they have the same semantics, and
same syntax too!
******************************************************
## List / Array -  access

Python
```python
numbers[4]
```

JS
```js
numbers[4]
```

---
Accessing an individual item of an array uses the same subscript
notation syntax.
******************************************************
## List / Array -  get length

Python
```python
len(numbers)
```

JS
```js
numbers.length
```

---
Getting the length of a list/array is different. Python uses the
`len` function, while in JS, it uses the special `length` property on
the array.
******************************************************
## List.append / Array.push

Python
```python
numbers.append(8)
```

JS
```js
numbers.push(8);
```

---
Whereas in Python, you use the `append` method to add an item to a list,
in JS, you use the `push` method to add to an array.
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
For loops.

Python's for loop allows you to iterate through a list or sequence
without having to use a counter variable. In JS, the for loop can't
do that. The for loop in JS is merely a while loop in disguise...
******************************************************
## For loops

JS for loop
```js
for (var i = 0; i < numbers.length; i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

Equivalent JS While loop
```js
var i = 0;
while (i < numbers.length) {
  var number = numbers[i];
  console.log(number);
  i += 1;
}
```

---
The JS for loop above is equivalent to the while loop below. The while
loop below uses the loop and counter pattern taught in
[Python Lesson 2.1](/#python/lesson-2.1).
******************************************************
## For loops

JS for loop
```js
for ([[var i = 0]][[clause 1]]; [[i < numbers.length]][[clause 2]]; [[i+=1]][[clause 3]]) {
  var number = numbers[i];
  console.log(number);
}
```

Equivalent JS While loop
```js
var i = 0;
while ([[i < numbers.length]][[conditional clause]]) {
  var number = numbers[i];
  console.log(number);
  i += 1;
}
```

---
Whereas the while loop only has one conditional clause within its parenthesis,
the for loop has 3 clauses within its parenthesis,
******************************************************
## For loops

JS for loop
```js
for (var i = 0[[[;]]] i < numbers.length[[[;]]] i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

Equivalent JS While loop
```js
var i = 0;
while (i < numbers.length) {
  var number = numbers[i];
  console.log(number);
  i += 1;
}
```

 ---
separated by semicolons.
******************************************************
## For loops

JS for loop
```js
for ([[var i = 0]][[initialization clause]]; i < numbers.length; i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

Equivalent JS While loop
```js
[[var i = 0;]][[initialization]]
while (i < numbers.length) {
  var number = numbers[i];
  console.log(number);
  i += 1;
}
```

---
The first clause is the *initialization clause*, which mirrors
the initialization statement in the while loop version.

Despite the location of this clause --- which may make it seem like it is
a part of the loop, it is only executed once overall,
before the loop, rather than once per iteration. Again, the behavior
of the for loop is identical to the while loop below.
******************************************************
## For loops

JS for loop
```js
for (var i = 0; [[i < numbers.length]][[conditional clause]]; i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

Equivalent JS While loop
```js
var i = 0;
while ([[i < numbers.length]][[conditional clause]]) {
  var number = numbers[i];
  console.log(number);
  i += 1;
}
```
---
the second clause is the *conditional clause*, which matches with the
conditional clause in the while loop.
******************************************************
## For loops

JS for loop
```js
for (var i = 0; i < numbers.length; [[i+=1]][[incrementer clause]]) {
  var number = numbers[i];
  console.log(number);
}
```

Equivalent JS While loop
```js
var i = 0;
while (i < numbers.length) {
  var number = numbers[i];
  console.log(number);
  [[i += 1;]][[incrementer statement]]
}
```

---
and the last clause is the *incrementer clause*, which matches with the
incrementer statement in your while loop version.

The location of this incrementer clause in the for loop is misleading.
Although it lives at the top of the loop, it actually executes at the end
of each iteration --- again, behaving in the same way as the while loop
version which uses the loop and counter pattern.

Why even bother with such confusion? If you prefer, you are welcome to simply
use a while loop anywhere you'd use a for loop.
******************************************************
## For loops

JS for loop
```js
for (var i = 0; i < numbers.length; i+=1) {
  var number = numbers[i];
  console.log(number);
}
```

Equivalent JS While loop
```js
var i = 0;
while (i < numbers.length) {
  var number = numbers[i];
  console.log(number);
  i += 1;
}
```

---
So this is what the for loop in JS looks like. It is what I'd call the
*classic* for loop --- it came from more traditional programming languages
like C.
******************************************************
## For loops

Python
```python
word = "bananas"
reversed_word = ""
for letter in word:
  reversed_word = letter + reversed_word
```

JS
```js
var word = "bananas";
var reversedWord = "";
for (var i = 0; i < word.length; i++) {
  var letter = word[i];
  reversedWord = letter + reversedWord;
}
```

---
You can use this classic for loop pattern to loop through the letters of
a string as well as an array, because a string in JS also acts like
an array, at least for the basic things.
******************************************************
## Splitting Strings

Python
```python
words = phrase.split(" ")
```

JS
```js
var words = phrase.split(" ");
```

---
To split a string into an array of strings by a separator string,
you can use the `split` method on the string just like with Python.
******************************************************
## Joining Strings

Python
```python
joined = " ".join(words)
```

JS
```js
var joined = words.join(" ");
```

---
With join, JS is a bit different from Python. It has its object and argument
swapped.
******************************************************
## Joining Strings

Python
```python
joined = " ".join([[words]][[the list to be joined]])
```

JS
```js
var joined = words.join(" ");
```

---
Whereas in Python, the list to be joined together is the argument of the
join method.
******************************************************
## Joining Strings

Python
```python
joined = [[" "]][[the separator]].join(words)
```

JS
```js
var joined = words.join(" ");
```

---
and the separator is the string object to the left of the dot operator.
******************************************************
## Joining Strings

Python
```python
joined = " ".join(words)
```

JS
```js
var joined = [[words]][[the array to be joined]].join(" ");
```

---
JS does it in reverse: the array containing the words to be joined is
the object to the left of the dot operator,
******************************************************
## Joining Strings

Python
```python
joined = " ".join(words)
```

JS
```js
var joined = words.join([[" "]][[the separator]]);
```

---
and the separator is the argument to the `join` method.
******************************************************
## Example 1

```python
number = 1
while number <= 100:
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

---
Let's use this FizzBuzz program as an example --- you might have seen it before.
We'll rewrite it from Python to JavaScript by converting it line by line.
******************************************************
## Example

```python
[[[number = 1]]]
while number <= 100:
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

```js
[[[var number = 1;]]]
```

---
Starting with line 1. Rewrite the variable assignment in JS.

For your homework, you'll be given [this Python to JS cheatsheet](https://gist.github.com/airportyh/fee3aa986fb61f6da7c7b00c5ff4dc3b) to use.
You should print out that cheatsheet and have it next to you for when
you need it.
******************************************************
## Example

```python
number = 1
[[[while number <= 100:]]]
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

```js
var number = 1;
[[[while (number <= 100) {

}]]]
```

---
Line 2 is a while loop statement. Because this introduces a block, we
type the closing curly bracket to match the opening bracket, and then come
back within the brackets to type the next statements, so that:

1. This is valid JS and can be evaluated (although at this point it will
  have an infinite loop, oops!)
2. It avoids us forgetting to close the curly bracket later.
******************************************************
## Example

```python
number = 1
while number <= 100:
  [[[if number % 5 == 0 and number % 3 == 0:]]]
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

```js
var number = 1;
while (number <= 100) {
  [[[if (number % 5 === 0 && number % 3 === 0) {

  }]]]
}
```

---
Next we have the if statement. Again, we type the matching brackets first,
and then come back inside the brackets.
******************************************************
## Example

```python
number = 1
while number <= 100:
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

```js
var number = 1;
while (number <= 100) {
  if (number % 5 [[[===]]] 0 && number % 3 [[[===]]] 0) {

  }
}
```

---
Remember to use triple equals!

******************************************************
## Example

```python
number = 1
while number <= 100:
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

```js
var number = 1;
while (number <= 100) {
  if (number % 5 === 0 [[[&&]]] number % 3 === 0) {

  }
}
```

---
Also, the `and` operator has been rewritten as the `&&` operator.
******************************************************
## Example

```python
number = 1
while number <= 100:
  if number % 5 == 0 and number % 3 == 0:
    [[[print("FizzBuzz")]]]
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

```js
var number = 1;
while (number <= 100) {
  if (number % 5 === 0 && number % 3 === 0) {
    [[[console.log("FizzBuzz");]]]
  }
}
```

---
Now we'll rewrite the print function call as a console.log call.
******************************************************
## Example

```python
number = 1
while number <= 100:
  if number % 5 == 0 && number % 3 == 0:
    print("FizzBuzz")
  [[[elif number % 3 == 0:]]]
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

```js
var number = 1;
while (number <= 100) {
  if (number % 5 == 0 && number % 3 == 0) {
    console.log("FizzBuzz");
  } [[[else if (number % 3 === 0) {

  }]]]
}
```

---
Now we convert the first `elif` to an `else if` statement in JS.
******************************************************
## Example

```python
number = 1
while number <= 100:
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    [[[print("Fizz")]]]
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
  number += 1
```

```js
var number = 1;
while (number <= 100) {
  if (number % 5 == 0 && number % 3 == 0) {
    console.log("FizzBuzz");
  } else if (number % 3 === 0) {
    [[[console.log("Fizz");]]]
  }
}
```

---
And then the print function call within it to a console.log call.

Okay, let's skip a few steps...
******************************************************
## Example

```js
var number = 1;
while (number <= 100) {
  if (number % 5 == 0 && number % 3 == 0) {
    console.log("FizzBuzz");
  } else if (number % 3 === 0) {
    console.log("Fizz");
  } else if (number % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(number);
  }
  number += 1;
}
```

---
This is the JavaScript version of the same FizzBuzz program.

You can [run this in Python Tutor](http://pythontutor.com/visualize.html#code=var%20number%20%3D%201%3B%0Awhile%20%28number%20%3C%3D%20100%29%20%7B%0A%20%20if%20%28number%20%25%205%20%3D%3D%200%20%26%26%20number%20%25%203%20%3D%3D%200%29%20%7B%0A%20%20%20%20console.log%28%22FizzBuzz%22%29%3B%0A%20%20%7D%20else%20if%20%28number%20%25%203%20%3D%3D%3D%200%29%20%7B%0A%20%20%20%20console.log%28%22Fizz%22%29%3B%0A%20%20%7D%20else%20if%20%28number%20%25%205%20%3D%3D%3D%200%29%20%7B%0A%20%20%20%20console.log%28%22Buzz%22%29%3B%0A%20%20%7D%20else%20%7B%0A%20%20%20%20console.log%28number%29%3B%0A%20%20%7D%0A%20%20number%20%2B%3D%201%3B%0A%7D&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=js&rawInputLstJSON=%5B%5D&textReferences=false).
**********************************************************
## Summary

* Printing
* Variables
* Prompting
* String formatting
* Operators
* If statements
* While loops
* Lists
* For loops
* Split and joining strings

---
You made it! This was a whirlwind tour of JS. Look how much you've
learned in only one lesson! For you homework, you'll have access
to [this cheatsheet](https://gist.github.com/airportyh/fee3aa986fb61f6da7c7b00c5ff4dc3b).
**********************************************************
## Homework

[Enjoy your homework!](https://gist.github.com/airportyh/6686e830b9e6eff77c6355e6be05cf66)
