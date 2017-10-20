# Vocabulary From Lesson 1

## Function

A *function* is a bundle of code that performs a specific
task and/or answers a specific question. Sometimes it takes
one or more input arguments, and sometimes it produces
and returns an output value. Example:

```python
print('Hello!!!')
```
In the statement above, the word `print` refers to the "print" function.

## Function Call

A *function call* is a program statement that calls a
specific function.

```python
print('Hello!!!')
```
The entire line above is the function call.

## Argument

An *argument* is a value that gets passed to a function at the
that function is called.

```python
print('Hello!!!')
```
In the statement above, there is one argument passed to the print function, and that argument is `'Hello!!!'`.

## Argument List

An *argument list* is a list of arguments surrounded by
parentheses, used when making a function call.

```python
print('Hello', your_name)
```
In the above statement, `('Hello', your_name)` is the argument
list.

## print function

The *print function* is a built-in function that prints
text to the terminal. It takes one or more arguments as input,
prints them out all on a line, and does not return any output.

```python
print('Hello!!!')
```
The above statement calls the print function to use it
to print `Hello!!!` in the terminal.

## input function

The *input function* is a built-in function that asks the
user to enter some text. It takes one argument - the text
that is displayed to the user to prompt them to enter the text,
and it returns the text that the user entered as the output.

## int function

The *int function* is a built-in function that converts
text to an int - integer. An integer may not have decimal
points. The `int` function takes a text argument as input,
and returns an int argument as output.

```python
value = '123'
value_as_integer = int(value)
```
The second line above takes the text inside the `value` variable and converts it to an integer, and then stores
it in the `value_as_integer` variable.

## float function

The *float function* is a built-in function that converts
text to a float - floating point number. A float is a number
that may have decimal points. The `float` function takes
a text argument as input, and returns a float as output.

```python
value = '123.45'
value_as_float = float(value)
```
The second line above takes the text inside the `value`
variable and converts it to a float, and then stores
it in the `value_as_float` variable.

## Variable

A *variable* is a named placeholder that can store a value. The variable's
name can be used anywhere in a program in place of an actual value.
A variable's value may change as the result of a variable assignment
using the `=` operator.

```python
thing = 'Thingamabob'
```
In the variable assignment statement above, `thing` is the
variable.

```python
print(thing)
```
In the print function call above, the variable `thing` is being
referred to as a argument passed to the print function.

## Variable Assignment

A *variable assignment* statement is a statement which
assigns a value to a variable. If the variable that is
being assigned doesn't exist, the statement will create
that variable. If the variable already exists, it will
assign the value to that existing variable.

```python
thing = 'Thingamabob'
```
Above is a variable assignment statement that assigns the
value `'Thingamabob'` to the variable `thing`.

## Arithmetic Operator

An *arithmetic operator* is a math operator that operates on
two numbers. The most commons are:

| Operator | Use                                        |
|----------|--------------------------------------------|
|    +     | Add two numbers                            |
|    -     | Subtract two numbers                       |
|    *     | Multiply two numbers                       |
|    /     | Divide two numbers                         |
|    %     | Modulus - reminder of dividing two numbers |

```python
answer = 2 + 3
```
The above statement uses the `+` arithmetic operator to add
the numbers 2 and 3, and then stores the result in the `answer` variable.

## String

A *string* is how text is represented in Python. We are
glossing over it this lesson, but will dive more into it.
