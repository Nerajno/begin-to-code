# JSON
## Data Format of the Web

---
Hey there! Are you ready to learn about JSON?
The JavaScript Object Notation format?

JSON is a widely used data format for sending information.
It is commonly used by web based APIs either
in custom built in applications or those that are
made for public consumption. We'll talk much more about APIs in
later lessons, but for now, we'll talk about JSON:
the data format.
*******************************************************
## JSON: Fun Facts

* Created by Douglas Crockford (2001)

![Crockford](./lessons/javascript/lesson-8/images/douglas-crockford.jpg)

---
Let's start with some fun facts about JSON!

First, JSON was created by Douglas Crockford. You might know him
as the author of JavaScript the Good Parts. He is also the original
author of JSHint, as well as the Yahoo JavaScript lecture series that
has taught JavaScript to yours truly as well as many other old timers.
*******************************************************
## JSON: Fun Facts

* Created by Douglas Crockford (2001)
* JSON is also JS!

---
Second, JSON is also JavaScript! Technically, it is a subset of JavaScript.
Which means that any code that is valid JSON is also valid JavaScript.
However, any code that is valid JavaScript is not necessarily valid JSON.
*******************************************************
## JSON: Fun Facts

* Created by Douglas Crockford (2001)
* JSON is also JS!
* Used in languages other than JS

---
JSON had a huge surge in popularity during the ascend of JavaScript during
the mid-2000's. For that reason, other programming languages needed to
interoperate with JavaScript, and therefore need to support JSON as well.
*******************************************************
## JSON: Fun Facts

* Created by Douglas Crockford (2001)
* JSON is also JS!
* Used in languages other than JS
* Can represent these types:
    * strings
    * numbers
    * arrays
    * objects
    * booleans
    * null

---
JSON can represent the following JavaScript value types:

* strings
* numbers
* arrays
* objects
* booleans
* null

These are all of the types it can represent.
*******************************************************
## JSON: Fun Facts

* Created by Douglas Crockford (2001)
* JSON is also JS!
* Used in languages other than JS
* Can represent these types:
    * strings
    * numbers
    * arrays
    * objects
    * booleans
    * null
* Cannot represent all possible JS values

---
And that means it *cannot* represent any other value type in JavaScript,
including:

* dates
* undefined
* regular expressions
* custom object types
* DOM elements
* and more...
*******************************************************
## JSON Example

```json
{
  "make": "BMW",
  "model": "328c",
  "year": 1998,
  "color": "black",
  "convertible": true
}
```

---
This is a simple example of JSON code. This is an example of
a JavaScript object containing 5 key value pairs.

Look familiar? Good.

JSON does not have:

* variables
* if statements
* loops of any kind
* or functions

All it has is data. So the very first thing in the code is a value
--- in this case an object.
*******************************************************
## JSON Example

```json
{
  [[["]]]make[[["]]]: "BMW",
  [[["]]]model[[["]]]: "328c",
  [[["]]]year[[["]]]: 1998,
  [[["]]]color[[["]]]: "black",
  [[["]]]convertible[[["]]]: true
}
```

---
The only difference you might have noticed --- from what you are used to
--- is that there are double quotes
around the keys in this object.
*******************************************************
## JSON Example

```json
var transportDevice = {
  "make": "BMW",
  "model": "328c",
  "year": 1998,
  "color": "black",
  "convertible": true
};
```

This works!!!

---
But it turns out that this is valid in JavaScript too. The double quotes
around the keys in an object expression are optional most of the time.
*******************************************************
## JSON Example

```json
var transportDevice = {
  "make": "BMW",
  "model": "328c",
  "year": 1998,
  "color": "black",
  [[["top color"]]]: "black",
  "convertible": true
};
```

---
They *are* required if you want to use a key that has spaces or special
characters in it.

Conventionally though, JavaScript developers avoid this
altogether and use [camelCase](https://en.wikipedia.org/wiki/Camel_case)
wheneverTheyHaveTo stringABunchOfWordsTogether.
*******************************************************
## JSON Example

```json
{
  [[["]]]make[[["]]]: "BMW",
  [[["]]]model[[["]]]: "328c",
  [[["]]]year[[["]]]: 1998,
  [[["]]]color[[["]]]: "black",
  [[["]]]convertible[[["]]]: true
}
```

---
IN JSON though, those double quotes are required. In general, JSON uses a stricter
design philosophy than JavaScript, and this is the first sign of that.
*******************************************************
## JSON Example

This is not valid: JSON

```json
{
  "make": [[[']]]BMW[[[']]],
  "model": "328c",
  "year": 1998,
  "color": "black",
  "convertible": true
}
```

---
Here's another example. In JSON, all strings must be quoted with double
quotes. In JavaScript, strings can be quoted using either double quotes or
single quotes.

The good news is: these are the only two differences you need to remember.
The rest will be all familiar to you.
*******************************************************
## JSON Example

```json
[[[{]]]
  "make": "BMW",
  "model": "328c",
  "year": 1998,
  "color": "black",
  "convertible": true
[[[}]]]
```

---
When you are working with APIs, you'll usually be dealing with either an
array or an object as the top-level value. In this case, the top-level
value is an object.
*******************************************************
## JSON Example 2

```json
[
  {
    "make": "BMW",
    "model": "328c",
    "year": 1998,
    "color": "black",
    "convertible": true
  },
  {
    "make": "Nissan",
    "model": "Leaf",
    "year": 2018,
    "color": "silver",
    "convertible": false
  }
]
```

---
This is an example where the top-level value is an array.
*******************************************************
## Valid JSON Too

```json
"blah blahty blah"
```

```json
3.1415926535
```

```json
true
```

```json
null
```

---
Technically, the top-level value can be a string, number, boolean, or null,
although these are rarely used.
*******************************************************
## Nesting

```json
{
  "name": "Flo",
  "children": [
    { "name": "Fay" },
    {
      "name": "Kay",
      "children": [
        {
          "name": "Joe",
          "children": [
            { "name": "Mira" }
          ]
        }
      ]
    }
  ]
}
```

---
As is the case with JavaScript data structures, JSON data structures can
be nested. This JSON code is a representation of a family tree. It could
be nested an arbitrary number of levels deep.
*******************************************************
## JSON validator

[Code Beautify JSON Validator](https://codebeautify.org/jsonvalidator)

---
Often you won't have to type out JSON code by hand when you are working
with APIs. However, in the few occasions when you do, you may benefit to
have a validator to make sure you aren't forgetting to put all the double
quotes in the places they need to be.

The Code Beautify JSON Validator is such a tool. You can go there,
paste in your JSON code, click "Validate". And it gives you a green bar
saying "Valid JSON", then you are good to go.

Most modern text editors also support validating your JSON as you type
if you are typing in a file with the `.json` extension.
*******************************************************
## Summary

* History of JSON
* Quirks of JSON
* Syntax of JSON

---
This is what you've learned.
*******************************************************
## Homework

[Enjoy your homework](https://gist.github.com/airportyh/f9dbe6e539753291769333f4650bc4af)
