
Having said that, there is a simpler way to for loop in JS.
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
If we are iterating through an array, there *is* a short-hand that is
comparable to Python's for loop. It is array's *forEach* method.
******************************************************
## For loops

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
To do this, the thing we are iterating must be an array. It doesn't
work for strings, for example.
******************************************************
## For loops

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
The `forEach` method takes in a function as its argument, and will call
that function once for each item in the array.
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
Each time, it will pass a different item within the array to this
function as its first parameter.
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
The idea of passing in a function as an argument may seem foreign. But it is
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
The advantage of `forEach` is that you don't have to manager your own counter,
similarly to with Python's for loop.
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

******************************************************
## Function

Python
```python
def celsius_to_fahrenheit(c):
  return c * 9 / 5 + 32
```

JS
```js
function celsiusToFahrenheit(c) {
  return c * 9 / 5 + 32;
}
```

---
Now for functions!! Functions also have a similar syntax.
******************************************************
## Function

Python
```python
def celsius_to_fahrenheit(c):
  return c * 9 / 5 + 32
```

JS
```js
[[function]][[function keyword]] celsiusToFahrenheit(c) {
  return c * 9 / 5 + 32;
}
```

---
In JS you use the `function` keyword, instead of `def`.
******************************************************
## Function

Python
```python
def celsius_to_fahrenheit(c):
  return c * 9 / 5 + 32
```

JS
```js
function celsiusToFahrenheit(c) [[[{]]]
  return c * 9 / 5 + 32;
[[[}]]]
```

---
And you use the curly brackets instead of indentation for blocks.
