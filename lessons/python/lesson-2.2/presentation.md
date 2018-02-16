# Lesson 2.6
## String Formatting

---
Welcome back! In this lesson we'll learn
about string formatting in order to make your
print outs more neat and tidy.
************************************************
## Section 1
# String Formatting

---
************************************************
## Definition: String Formatting

The process of taking a format string --- a
template with placeholders --- and substituting
in dynamic values in place of the placeholders.

---

************************************************
## A Format String

```python
"Hello, %s! You are %d years old!"
```

---
This is a format string. A format string is
a normal Python string with one or more placeholders.
************************************************
## A Format String

```python
"Hello, [[[%s]]]! You are [[[%d]]] years old!"
```

---

The placeholders are called *conversion specifiers*.
They start with a percent sign (`%`), followed
by a one-character conversion type code.
************************************************
## A Format String

```python
"Hello, [[%s]][[string conversion]]! You are %d years old!"
```

---
In this example, the first conversion specifier uses the
"s" code, which converts a value to a string.
************************************************
## A Format String

```python
"Hello, %s! You are [[%d]][[signed integer conversion]] years old!"
```

---
The second specifier uses the "d" code, which
converts the value to a signed integer.
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, %s! You are %d years old!" % (name, age)
print(result)
```

---
Once you have a formatting string, you need to use the `%`
formatting operator to perform the formatting and
substitute values into the string to get the resulting
string.
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, %s! You are %d years old!" [[%]][[formatting operator]] (name, age)
print(result)
```

---
This is the formatting operator. Not to be confused with...
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, [[[%]]]s! You are [[[%]]]d years old!" % (name, age)
print(result)
```

---
the `%` sign in the the conversion
specifiers.
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, %s! You are %d years old!" [[%]][[formatting operator]] (name, age)
print(result)
```

---
The formatting operator performs the magic that makes the substitutions.

By default, substitutions are done in order.
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, %s! You are %d years old!" % ([[name]][[1st value]], age)
print(result)
```

---
The first value on the right-hand side is substituted into...
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, [[%s]][[1st conversion specifier]]! You are %d years old!" % (name, age)
print(result)
```

---
the first conversion specifier.
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, %s! You are %d years old!" % (name, [[age]][[2nd value]])
print(result)
```

---
And the second value on the right-hand side is substituted in to...
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, %s! You are [[%d]][[2nd conversion specifier]] years old!" % (name, age)
print(result)
```

---
the second conversion specifier.
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = [["Hello, %s! You are %d years old!" % (name, age)]][["Hello, Camila! You are 7 years old!"]]
print(result)
```

---
And the result of this entire string formatting expression is a new version
of the format string: "Hello, Camila! You are 7 years old!"
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
[[result]][[store "Hello, Camila! You are 7 years old!" here]] = "Hello, %s! You are %d years old!" % (name, age)
print(result)
```

---
We store it into `result`
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
result = "Hello, %s! You are %d years old!" % (name, age)
[[print(result)]][[prints "Hello, Camila! You are 7 years old!"]]
```

---
and print it out.
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
[[print("Hello, %s! You are %d years old!" % (name, age))]][[also prints "Hello, Camila! You are 7 years old!"]]
```

---
Alternately, we could choose to directly print the result without first
storing it in a variable.
************************************************
## The Formatting Operator

```python
name = "Camila"
age = 7
print("Hello, %s! You are %d years old!" % [[(name, age)]][[What this is?]])
```

---
Now, what is this thing on the right-hand side of the formatting operator
that's surrounded by parenthesis?

That's a *tuple*. Let's take a brief detour and talk about what tuples are
for just a bit.
****************************************************
## Definition: Tuple

An immutable (cannot be changed) ordered sequence of values.

---
A tuple in Python is a an immutable --- meaning cannot be changed ---
ordered sequence of values. It is commonly used to group multiple related
values. It is similar to lists --- a topic that's coming up next ---
with the main difference that it is immutable.
****************************************************
## Tuples

```python
(1, 2)
```

---
This is a tuple in Python. It is written as a comma-separated list of
values, surrounded by parenthesis. Very much like the argument list
of a function call:

```python
print(1, 2)
```

Except that there is no function name to the left of the parenthesis.
****************************************************
## Tuples

```python
my_tuple = [[(1, 2)]][[A tuple expression]]
```

---
A tuple is an expression and you can assign it to a variable just like
any other expression.
****************************************************
## Tuples

```python
a_2_tuple = (1, 2)
a_3_tuple = (3, 4, 6)

a_4_tuple_of_strings = ("apple", "orange", "pear", "kiwi")
a_2_tuple_of_lists = ([1, 2, 3], [4, 5, 6])
```

---

A tuple can contain any number of values. A tuple that contains 2 values is
called a 2-tuple. One that contains 3 values is called a 3-tuple, and so on.

A tuple can also contain any kind of values, including numbers, strings,
lists (gasp!), and more.
****************************************************
## Tuples

```python
apples = ("apple", 2)
oranges = ("orange", 5)
```

---
A tuple can also contain mixed types of things. In this example,
both of these tuples contain one string and one number.
************************************************
## Tuples

```python
name = "Camila"
age = 7
print("Hello, %s! You are %d years old!" % [[(name, age)]][[A tuple ("Camila", 7)]])
```

---
Back to our string formatting example, the thing on the right-hand side of the
string formatting operator is a 2-tuple that contains the string "Camila",
and then the number 7.
************************************************
## Tuples

```python
name = "Camila"
age = 7
[[a_2_tuple]][[store ("Camila", 7) here]] = (name, age)
print("Hello, %s! You are %d years old!" % a_2_tuple)
```

---
Alternatively, we could have first stored the tuple value into a variable
************************************************
## Tuples

```python
name = "Camila"
age = 7
a_2_tuple = (name, age)
print("Hello, %s! You are %d years old!" % [[a_2_tuple]][[use ("Camila", 7) here]])
```

---
and then used it in the format operation by using the variable name.

So that's tuples.
************************************************
## Formatting: One Conversion

```python
your_name = "world"
print("Hello, %s!" % your_name)
```

---
Back to string formatting!

One more thing before be going into more detail about
specific conversion specifiers...
************************************************
## Formatting: One Conversion

```python
your_name = "world"
print("Hello, [[%s]][[the only conversion specifier]]!" % your_name)
```

---
If you you only have one conversion specifier in the
formatting string,
************************************************
## Formatting: One Conversion

```python
your_name = "world"
print("Hello, %s!" % [[your_name]][[just "world"]])
```

---
There is no need to use a tuple on the right-hand side to wrap a single value,
you may use just that value. Python did that for your convenience.

*You're welcome!*
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches // 12
inches = inches % 12
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
This program asks for your height in inches, and then converts that
to feet plus some leftover inches.
************************************************
## Formatting: Integers

```python
[[inches = int(input("How tall are you in inches? "))]][[Height in inches?]]
feet = inches // 12
inches = inches % 12
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
Here it asks for your height in inches.

************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches [[//]][[integer division]] 12
inches = inches % 12
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
This operator --- which you may not have seen before --- is the integer
division operator. It will perform the division and return the quotient with
no fraction or digits after the decimal point.
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = [[inches // 12]][[divide by 12]]
inches = inches % 12
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
So it will divide your height by 12, do that in your head now.

In my case that would be 68 divided by 12 to get 5.
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
[[feet]][[store 5 in here (for me)]] = inches // 12
inches = inches % 12
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
So you'd store that 5 in the `feet` variable. For you, it might be a
different number.
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches // 12
inches = inches [[%]][[the modulus operator]] 12
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
This is the modulus operator which will perform the division and give
you the remainder of the division.
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches // 12
inches = [[inches % 12]][[divide by 12 and get remainder]]
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
So for me that would be 68 divided by 12 to get the remainder of 8.
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches // 12
[[inches]][[store 8 in here (for me)]] = inches % 12
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
and we store that 8 into here. For you it might be a different number.
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches // 12
inches = inches % 12
print([["So you are %d feet and %d inches!" % (feet, inches)]][[format the string]])
```

---
Finally, we set up a formatting string and substitute in the values of feet
and inches to be printed out.
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches // 12
inches = inches % 12
print("So you are [[[%d]]] feet and [[[%d]]] inches!" % (feet, inches))
```

---
We have 2 "d" conversion specifiers, which are perfect for displaying
integers.
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches // 12
inches = inches % 12
print("So you are %d feet and %d inches!" % ([[[feet]]], [[[inches]]]))
```

---
and two integer values to match, wrapped within a 2-tuple. Perfect!
************************************************
## Formatting: Integers

```python
inches = int(input("How tall are you in inches? "))
feet = inches // 12
inches = inches % 12
print("So you are %d feet and %d inches!" % (feet, inches))
```

---
Run this code in Python Tutor and watch it in action.
************************************************
## Formatting: Floats

```python
c = float(input("What is the temperature in °C? "))
f = c * 9 / 5 + 32
print("It is %f°F." % f)
```

---
Okay, now let's get into numbers with decimal points
such as `3.1415`.
In computer science, they are called floating point numbers.

This program asks the user to enter the temperature in degrees
Celsius, converts it to degrees Fahrenheit, and prints it out.
Please read this example and get a feel for how it works.
************************************************
## Formatting: Floats

```python
c = float(input("What is the temperature in °C? "))
f = c * 9 / 5 + 32
print("It is [[%f]][[formats a float]]°F." % f)
```

---
This example uses the `%f` conversion specifier --- short for floats.
************************************************
## Formatting: Floats

```python
c = float(input("What is the temperature in °C? "))
f = c * 9 / 5 + 32
print("It is %f°F." % f)
```

Output:
```
What is the temperature in °C? 32
It is 89.600000°F.
```

---
This is one sample output for the program, given the user
enters 32.
************************************************
## Formatting: Floats

```python
c = float(input("What is the temperature in °C? "))
f = c * 9 / 5 + 32
print("It is %f°F." % f)
```

Output:
```
What is the temperature in °C? 32
It is 89.[[600000]][[6 decimal places]]°F.
```

---
By default --- as you can see --- the `%f` conversion specifier displays 6 decimal
places, but this can be configured.
************************************************
## Formatting: Floats

```python
"%.2f"
```

---
The notation for configuring the number of decimal places looks
like this.
************************************************
## Formatting: Floats

```python
"[[%]][[symbol for conversion specifier]].2f"
```

---
You start with the percent sign like before,
************************************************
## Formatting: Floats

```python
"%[[.]][[decimal point]]2f"
```

---
then a period --- like a decimal point,
************************************************
## Formatting: Floats

```python
"%.[[2]][[how many decimal places?]]f"
```

---
then a number specify the number of decimal places you
want to display, in this case 2.
************************************************
## Formatting: Floats

```python
"%.2[[f]][[conversion type: float]]"
```

---
then finally the conversion type of f, again, for floats.

The decimal place specifier only works for converting floats.
************************************************
## Formatting: Floats

```python
pi = 3.141592653589793
print("PI is %f" % pi)
print("PI is %.2f" % pi)
print("PI is %.14f" % pi)
print("PI is %.50f" % pi)
```

---
What will this print?

Go to the next slide to find out.
************************************************
## Formatting: Floats

```python
pi = 3.141592653589793
print("PI is %f" % pi)
print("PI is %.2f" % pi)
print("PI is %.14f" % pi)
print("PI is %.50f" % pi)
```

Result:
```
PI is 3.141593
PI is 3.14
PI is 3.14159265358979
PI is 3.14159265358979311599796346854418516159057617187500
```

---
Is this what you expected?
************************************************
## Summary

* Formatting strings
* Tuples
* Formatting Floating Point Numbers

---
That's it for this lesson. This is what you've learned.
************************************************
## Homework

[Homework](https://gist.github.com/airportyh/5327a45c6912a6ed439aef4e979a9e8d)

---
Enjoy your homework!
