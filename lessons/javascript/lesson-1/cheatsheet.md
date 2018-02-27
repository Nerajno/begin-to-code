# Python to JS Cheatsheet

## Printing

Python
```python
print("Hello, world!")
```

JS
```js
console.log("Hello, world!");
```

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

## Prompting

Python
```python
name = input("What is your name? ")
```

JS
```js
var name = prompt("What is your name? ");
```

## Number Conversion

Python
```python
age = int(input("How old are you? "))
```

JS
```js
var age = Number(prompt("How old are you? "));
```

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

## If Statement

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

## List / Array

Python
```python
numbers = [1, 2, 5, 6, 7]
```

JS
```js
var numbers = [1, 2, 5, 6, 7];
```

## List / Array -  access

Python
```python
numbers[4]
```

JS
```js
numbers[4]
```

## List / Array -  get length

Python
```python
len(numbers)
```

JS
```js
numbers.length
```

## List.append / Array.push

Python
```python
numbers.append(8)
```

JS
```js
numbers.push(8);
```

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

## Splitting Strings

Python
```python
words = phrase.split(" ")
```

JS
```js
var words = phrase.split(" ");
```

## Joining Strings

Python
```python
joined = " ".join(words)
```

JS
```js
var joined = words.join(" ");
```
