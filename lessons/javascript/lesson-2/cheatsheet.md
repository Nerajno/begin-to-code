# Lesson 2 Python to JS Cheatsheet

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

## forEach Method

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

## Object as Record

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

## Accessing Object Property

Python
```python
banana.calories
```

JS
```JS
banana.calories
```

## Modifying an Object Property

Python
```python
banana.calories = 284
```

JS
```js
banana.calories = 284;
```

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

## Lookup by Key

Python
```python
lookup["LOL"]
```

JS
```js
lookup["LOL"]
```

## Modify or Adding Entry

Python
```python
lookup["LOL"] = "Lots of Laughs"
```

JS
```js
lookup["LOL"] = "Lots of Laughs";
```

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
