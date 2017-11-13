# Lesson 2: If, While, and String Formatting
---
In this lesson, we'll cover the if-statement, the while loop statement,
and string formatting in Python for more precise printing.
***************************************************
## if statement

```python
if age > 21:
  print("You are old enough")
  print("Please come in")
```

---
Let's jump right into it. This is the if statement. It performs a set
of statements given that a condition is met.
***************************************************
## if statement

```python
[[if]][[The if keyword]] age > 21:
  print("You are old enough")
  print("Please come in")
```

---
It starts with the if keyword.
***************************************************
## if statement

```python
if [[age > 21]][[The conditional clause]]:
  print("You are old enough")
  print("Please come in")
```

---
Is followed by a conditional clause, which can use comparison operators such as
`>`, `==`, `<`, and more. More on operators in a bit.
***************************************************
## if statement

```python
if age > 21[[:]][[The colon]]
  print("You are old enough")
  print("Please come in")
```

---
Then, we have a mandatory colon.
***************************************************
## if statement

```python
if age > 21:
[[  print("You are old enough")
  print("Please come in")]][[Consequent block]]
```

---
Next we have the consequent block of the if statement. Which is a set of
statements which would be executed as a consequence of the conditional clause
being true.
***************************************************
## if statement: indentation

```python
if age > 21:
 →print("You are old enough")
 →print("Please come in")
```

---
Each line within the consequent block must be indented to the right of the
if statement on the first line. More over, each line in this block must
line up, meaning that they must indent by the same amount.

The rule for code blocks is: there is a colon (`:`) to begin the block, then
on the next line, all of the instructions that go within the block should
be indented one more level to the right of the beginning of the line where
the colon is.
***************************************************
## if statement: else clause

```python
if age > 21:
  print("You are old enough")
  print("Please come in")
else:
  print("Come back in a few years")
```

---
An optional part of the if statement is the else clause.
It also has an indented block. The block within the else
statement is called the *alternate block*, and it will
execute when the if statement's conditional is false.
***************************************************
## Drinking Age Full Example

```python
age = int(input("How old are you? "))
if age > 21:
  print("You are old enough")
  print("Please come in")
else:
  print("Come back in a few years")
```

---
This is the full drinking age example, you may run it in Python Tutor
to see how it works.
***************************************************
* elif
* pass
***************************************************
## While Loop

```python
while age < 21:
  print("Come back in a few years")
  age = age + 1
```
