# Lesson 2 Vocabulary

## if statement

A statement that conditionally executes a series of instructions based on
some specified condition. An if statement has:

1. a conditional clause
2. one or more consequent clauses
3. an alternate clause

Example:

```python
if age >= 21:
  print("You are old enough to drink")
else:
  print("Come back in a few years")
```

## (if statement) Conditional Clause

The part of an if statement that defines the condition that would activate
the consequent statements. In the following example, `age >= 21` is the
conditional clause.

```python
if age >= 21:
  print("You are old enough to drink")
else:
  print("Come back in a few years")
```

## Consequent Clause

The series of statements that
would execute if the conditional clause is evaluated as true. In the code
below, `print("You are old enough to drink")` is the
consequent clause

```python
if age >= 21:
  print("You are old enough to drink")
else:
  print("Come back in a few years")
```

## Alternate Clause

The series of statements that would execute if the conditional clause is
evaluated to false. In the code below, `print("Come back in a few years")`
is the alternate clause.

```python
if age >= 21:
  print("You are old enough to drink")
else:
  print("Come back in a few years")
```

## Format String

A string that contains one or more argument specifiers of the form `%d`, `%s`,
`%f` or similar to be used for substituting in dynamic values. In the example
below, `"Hello, %s! You were born in %d."` is the format string.

```python
print("Hello, %s! You were born in %d." % (name, year))
```

## (Format String) Argument Specifier

Within a format string, an argument specifier starts with a `%`, followed
usually by a single letter, but sometimes with some additional codes first.
In the example below, `%s` and `%d` are the argument specifiers:

```python
print("Hello, %s! You were born in %d." % (name, year))
```

## (Format String) Arguments

Arguments - within the context of format strings - are values that are
substituted into the argument specifiers within a format string. In the example
below, `(name, year)` are the arguments:

```python
print("Hello, %s! You were born in %d." % (name, year))
```

If there is one argument, there is no need to surround the values with
parenthesis:

```python
print("Hello, %s!" % name)
```

## Formatting Operator

The formatting operator `%` - not to be confused with a `%` sign that begins
an argument specifier, executes a format string and substitute the arguments
provided to its right into the format string on its left. Example:

```python
print("Hello, %s! You were born in %d." % (name, year))
```

The third `%` in the line above - the one between the format string and the
arguments is the formatting operator.

## While Loop

A while loop conditionally executes a series of statements like an if
statement, except that it does so repeatedly and indefinitely - until
the condition is no longer met. A while loop has:

1. A conditional clause
2. A loop body

Example:

```python
while age < 21:
  print("Come back next time")
  age = age + 1
```

## (while loop) Conditional Clause

The part of a while loop that defines the condition that would activate
the loop body. In the following example, `age < 21` is the
conditional clause.

```python
while age < 21:
  print("Come back next time")
  age = age + 1
```

## Loop Body

The part of a loop (while or for) to be executed each time the conditional
clause evaluates to true. In this example, the loop body consists of the
last 2 lines:

```python
while age < 21:
  print("Come back next time")
  age = age + 1
```

## Pattern

A structure commonly found in code solutions to various problems.

## Loop Counter Pattern

The loop counter pattern uses either a while loop or a for loop. There
are 3 important things to consider when this pattern is used:

1. The initialization statement
2. The continuing condition
3. The incrementer statement

Example:

```python
counter = 1
while counter <= 10:
  print('%d. Hi!!!' % counter)
  counter += 1
```

In the above example:

1. `counter = 1` is the initialization statement.
2. `counter <= 10` is the continuing condition.
3. `counter += 1` is the incrementer statement.
