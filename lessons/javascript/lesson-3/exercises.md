# JS Lesson 3 Exercises

For each exercise below, use the following HTML
template:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Example</title>
  </head>
  <body>

    HTML_BODY_CONTENT

  </body>
  <script src="jquery.js"></script>
  <script>

  JS_CODE

  </script>
</html>
```

## Clicking

Given this HTML_BODY_CONTENT:

```html
<button id="click">Click me!</button>
```

Write the JS_CODE to make it so that when the button
is clicked. It changes the text on the button itself
to "You clicked!!!" and change it's text color to
green.

## Apples and Bananas

Given this HTML_BODY_CONTENT:

```html
<h1 id="header"></h1>
<button id="i">I</button>
<button id="like">like</button>
<button id="to">to</button>
<button id="eat">eat</button>
<button id="apples">apples</button>
<button id="bananas">bananas</button>
```

Write the JS_CODE to make it so than any of
the buttons are clicked, the word on the button
is appended to the header, plus an extra space
character.

## Apples and Bananas Redux

Extend your solution from the previous exercise and add
a Piglatin button:

```html
<button id="piglatin">Piglatin</button>
```

When it is clicked, it piglatin-izes each word that is
currently in the header. You may use a previous
piglatin function you've written.

## Card Flip Toggle

Use the card images you downloaded from the lesson to do
this exercise.

Given this HTML_BODY_CONTENT:

```html
<img id="card" src="images/card_back.png" alt="A Poker Card">
```

Write the JS_CODE so that when you click on the card, it
reveals an Ace of Spades, but when click on the Ace of Spades,
it flips back to the card back image.

*Hint: you may consider using the state machine pattern,
being sure to declare the state variable outside of the
event handler function.*

## Card Flip Redux

Given this HTML_BODY_CONTENT:

```html
<img id="card" src="images/card_back.png" alt="A Poker Card">
```

Write the JS_CODE so that when you click on the card, a
random card is revealed. If you click again, it becomes another
random card.

## Rock, Paper, and Scissors

Write a Rock, Paper and Scissors game.

Use this HTML_BODY_CONTENT:

```html
<h1>Rock, Paper, and Scissors</h1>
<h2>Computer:</h2>
<span id="computer-move"></span>

<h2>You:</h2>
<span id="player-move"></span>

<h2 id="game-result"></h2>

<label>Your Move:</label>
<button id="play-rock">Rock</button>
<button id="play-paper">Paper</button>
<button id="play-scissors">Scissors</button>
```

Implement behaviors one by one for the JS_CODE:

1. When the "Rock" button is clicked, put the text
"Rock" in the `id="player-move"` span element.
2. Do the same as above for the "Paper" and "Scissors"
buttons.
3. Write a `playComputerMove` function, which
randomly sets the text in the `id="computer-move"`
span element to either "Rock", "Paper", or "Scissors".
4. Within each of the click event handlers, add a
call to the `playComputerMove` function, so that whenever
the player makes a move, the computer also immediately
makes a move.
5. Write a `determineWinner` function which
        a. determines who the winner is, or if it is a tie
        b. updates the text in the `id="game-result"` h2
            element to say either: "YOU WIN!", "YOU LOSE!"
            or "It's a tie."
6. Within each of the click event handlers, add a
call to the `determineWinner` function to show the result
of the game.
