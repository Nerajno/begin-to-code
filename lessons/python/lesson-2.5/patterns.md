# Patterns in Lesson 2.5

This lesson covered a number of patterns (and combinations of them) that
involve lists.

## Loop and Counter Pattern

```python
numbers = [1, 5, 2, 3, 4]
i = 0
while i < 5:
  number = numbers[i]
  print("The %d-th number is %d" % (i, number))
  i = i + 1
```

## (Loop and) Filter Pattern

```python
numbers = [1, 5, 2, 3, 4]
i = 0
while i < 5:
  number = numbers[i]
  if number % 2 == 0:
    print("%d is an even number." % (number))
  i = i + 1
```

## Accumulator Pattern

```python
numbers = [3, 6, 1, 4, 2, 5]
total = 0
i = 0
while i < len(numbers):
  number = numbers[i]
  total = total + number
  i = i + 1
```

## Accumulator + Filter Pattern

```python
numbers = [3, 6, 1, 4, 2, 5]
total = 0
i = 0
while i < len(numbers):
  number = numbers[i]
  if number % 2 == 0:
    total = total + number
  i = i + 1
```
