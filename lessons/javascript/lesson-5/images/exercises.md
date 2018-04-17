# JS Lesson 5 Exercises

## Section 1

### Degree Converter

Write a Celsius to Fahrenheit converter. Use the HTML markup below:

```html
<input id="celsius-input" type="text">°C = <span id="fahrenheit-display"></span>°F
<button id="convert-button">Convert!</button>
```

Write code so that when the `#convert` button is clicked, the number
within the `#celsius` input is taken and converted to °F and displayed
within the `#fahrenheit`.

### Degree Converter 2

Rewrite your degree converter to simulate having two pages. The first page
has a text input and a button, and the second page displays the result
and gives you a button to do another conversion. You may use this HTML
structure:

```html
<div id="page-1">
  <input id="celsius-input" type="text">°C
  <button id="convert-button">Convert!</button>
</div>
<div id="page-2">
  <span id="celsius-display"></span> = <span id="fahrenheit-display"></span>°F
</div>
```

## Section 2

### Coins

Given these [images of coins](https://airportyh.github.io/begin-to-code/lessons/javascript/lesson-5/coins.zip). And this HTML markup:

```html
<div id="coin-container">
  <img src="quarter-front.png">
</div>
<button id="add-quarter-button">Add quarter</button>
<button id="add-dime-button">Add dime</button>
<button id="add-nickle-button">Add nickle</button>
<button id="add-penny-button">Add penny</button>
```

The `#coin-container` element already has one quarter in it. Make it so
that click one of the buttons will add one more of the corresponding coin
images into the `#coin-container` element.

### Coin Change Challenge

Make a coin change maker. Allow the user to enter the total about of the bill,
and the amount of cash given, and display the coin change required using the
coin images from the last problem.

```html
<label>Total</label>
<input id="total-input" type="text">
<label>Cash</label>
<input id="cash-input" type="text">
<div id="coin-container">
</div>
```

### Duolingo Translator Exercise

Duolingo is a language learning app. One of its exercises features a
screen that looks like this:

![Duolingo exercise](https://airportyh.github.io/begin-to-code/lessons/javascript/lesson-5/images/duolingo.PNG)

The top of the screen has a person saying a phrase in the foreign language
that you are learning, followed by an answer box enclosed in dashed borders
which contains your answer, and a word labels list, and then the "check"
button to check your answer.

When you click on one of the word in the word labels list under the answer box,
that word goes into the answer box, and is removed from the set of word labels.
If there are existing words in the answer box, the new word goes to the
right of the existing words. You form a sentence by clicking
on the word labels one by one to form the correct translated sentence for
the foreign phrase. If you made a mistake, you can click on one or more
of the words that are already in the answer box, and those word(s) will
move back down to the word labels list.

You job for this exercise is to build the answer box and the word labels.
The key features to implement are the following --- it does not have to
work exactly like Duolingo:

1. When you click on a word in the word labels list, it is removed from that
list and appears in the answer box.
2. When you click on a word in the answer box, it is removed from the answer
box and reappears in the word labels list.
