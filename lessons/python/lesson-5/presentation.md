# Lesson 5
## String Manipulation 2
### and
## The State Machine Pattern
---
In this lesson we will do more string manipulation,
and we will learn another pattern - the *State Machine Pattern*.
******************************************
## State Machine

noun: a machine - which may be implemented by a computer program - which is at
all times in one of a predefined number of states, and transitions to different
states based on the inputs it encounters and a predefined set of rules.

---
******************************************
## State Machine Example: Toggle Switch

![Toggle Switch 1](./lessons/python/lesson-5/toggle-switch-1.jpg)

---
This is an example of a simple state machine - that for a toggle light switch.
We have two states, represented as circles: the "off" and the "on" states.
At the start of the program - represented with the "start" arrow, the program is
put into the "off" state.

An arrow represents an event, of which "start" is one.
******************************************
## State Machine Example: Toggle Switch

![Toggle Switch 2](./lessons/python/lesson-5/toggle-switch-2.jpg)

---
A "push" event is another event this program responds to, and it causes its
state to transition from "off" to "on" - in the event that it was previously
in the "off" state.

The changing of the state of a state machine is called a *state transition*.
******************************************
## State Machine Example: Toggle Switch

![Toggle Switch 3](./lessons/python/lesson-5/toggle-switch-3.jpg)

---
If another "push" event is sent to the program in its "on" state, it transitions
back to the "off" state.

This is how a light switch works, more or less.
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
This the Python code that would implement this
state machine. Let's take a closer look.
******************************************
## Toggle Switch
```python
[[state]][[The state variable]] = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
First, there is a `state` variable that holds the state of the
state machine at any given time.
******************************************
## Toggle Switch
```python
state = 'off'
[[event_list]][[A list of events]] = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
Then, we have a list variable called `event_list` which simulates a sequence
of events coming into our state machine.
******************************************
## Toggle Switch
```python
state = 'off'
event_list = [[['push']][[A push event]], [['nothing']][[A non-event]], 'nothing', 'push']
for event in event_list:
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
Events are represented simply with strings - with the names of events.
We have some "push" events, and we also have some "nothing" events, which
I am using to mean non-events - events we can ignore for the purposes
of this demonstration.

In more complex programs, events may be represented by more complex structures
than simple strings.
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
[[for event in event_list:]][[Loop through each event]]
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
There is a for loop to iterate through each `event` in the sequence of events
in `event_list`. We will use the state machine to process each event in the list.
This simulates "encountering" the events one after another, in order.
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  [[if state == 'off':]][[When the state is "off"]]
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
This if statement makes a choice based on what the current state is.
If the state is "off", ...
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
[[    if event == 'push':
      state = 'on'
    else:
      pass]][[Code to execute if state is "off"]]
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
the program will execute this block of code, ...
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  [[elif state == 'on':]][[When the state is "on"]]
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
if the state is "on", on the other hand, ...
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
[[    if event == 'push':
      state = 'off'
    else:
      pass]][[Code to execute when state is "on"]]
```
---
the program will execute this block instead.

Now let's go into details for each state.
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
[[    if event == 'push':
      state = 'on'
    else:
      pass]][[Does this when state is off]]
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
When the state of the toggle switch is off, it performs this logic:

If the event - which is the event we happen to encounter right now, is "push" -
meaning someone pushed the button, then we set the state's value to "on".
This is a state transition from "off" to "on".

If the event is some other event (such as "nothing") that we don't care about,
simply do nothing - which the `pass` statement accomplishes.
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
[[    if event == 'push':
      state = 'off'
    else:
      pass]][[Does this when state is on]]
```
---
Similarly, if the toggle switch is in the "on" state, this is the logic that
follows:

If the event being processed is "push" we switch to the "off" state, another
state transition. Again, we do nothing if the event is anything else.
******************************************
## Toggle Switch
```python
state = 'off'
event_list = ['push', 'nothing', 'nothing', 'push']
for event in event_list:
  if state == 'off':
    if event == 'push':
      state = 'on'
    else:
      pass
  elif state == 'on':
    if event == 'push':
      state = 'off'
    else:
      pass
```
---
That is how this state machine works. You may run this in Python Tutor yourself
to verify that you understand how this works.
******************************************
## State Machine Example: Turnstile

![Turnstile](./lessons/python/lesson-5/turnstile.jpg)

<https://en.wikipedia.org/wiki/Finite-state_machine>

---
Another simple example of a state machine is a turnstile.
******************************************
## Turnstile States

* locked
* unlocked
---
A turnstile has 2 possible states: locked, or unlocked.
******************************************
## Turnstile Events

* coin inserted
* pushed
---
It has 2 possible events that could occur to it: a coin was inserted, or
the turnstile was pushed.
*******************************************
## State Machine Example: Turnstile

![Turnstile](./lessons/python/lesson-5/turnstile-state-machine.png)

---
If the turnstile is in the locked state, and it gets a coin inserted, it
goes into the unlocked state, where the turnstile can actually be turned.

Then, if a person turns the turnstile to go in, it goes into the locked state
again, to prevent the next person from going in.

If someone pushes the turnstile in a locked state, it doesn't turn, and it
remains in the locked state.

If someone puts a coin in while it is already unlocked, it remains unlocked,
and they have just lost a coin for nothing!
*******************************************
```python
state = 'locked'
event_list = ['coin', 'push', 'coin', 'coin', 'push', 'push']
num_coins = 0
for event in event_list:
  if state == 'locked':
    if event == 'coin':
      state = 'unlocked'
      num_coins = num_coins + 1
    elif event == 'push':
      pass
  elif state == 'unlocked':
    if event == 'coin':
      num_coins = num_coins + 1
    elif event == 'push':
      print('Come on in!')
      state = 'locked'
```
---
Again, we have the same basic structure for a state machine.
*******************************************
```python
[[state]][[State variable]] = 'locked'
event_list = ['coin', 'push', 'coin', 'coin', 'push', 'push']
num_coins = 0
for event in event_list:
  if state == 'locked':
    if event == 'coin':
      state = 'unlocked'
      num_coins = num_coins + 1
    elif event == 'push':
      pass
  elif state == 'unlocked':
    if event == 'coin':
      num_coins = num_coins + 1
    elif event == 'push':
      print('Come on in!')
      state = 'locked'
```
---
The state variable, which this time can be either "locked", or "unlocked".
*******************************************
```python
state = 'locked'
[[event_list]][[The event list]] = ['coin', 'push', 'coin', 'coin', 'push', 'push']
num_coins = 0
for event in event_list:
  if state == 'locked':
    if event == 'coin':
      state = 'unlocked'
      num_coins = num_coins + 1
    elif event == 'push':
      pass
  elif state == 'unlocked':
    if event == 'coin':
      num_coins = num_coins + 1
    elif event == 'push':
      print('Come on in!')
      state = 'locked'
```
---
We also have an `event_list` as well, to represent the series of events that
occurred to the state machine.
*******************************************
```python
state = 'locked'
event_list = ['coin', 'push', 'coin', 'coin', 'push', 'push']
num_coins = 0
[[for event in event_list:]][[The for loop]]
  if state == 'locked':
    if event == 'coin':
      state = 'unlocked'
      num_coins = num_coins + 1
    elif event == 'push':
      pass
  elif state == 'unlocked':
    if event == 'coin':
      num_coins = num_coins + 1
    elif event == 'push':
      print('Come on in!')
      state = 'locked'
```
---
And we have a for loop.
*******************************************
```python
state = 'locked'
event_list = ['coin', 'push', 'coin', 'coin', 'push', 'push']
num_coins = 0
for event in event_list:
[[  if state == 'locked':
    if event == 'coin':
      state = 'unlocked'
      num_coins = num_coins + 1
    elif event == 'push':
      pass]][[If state is locked]]
  elif state == 'unlocked':
    if event == 'coin':
      num_coins = num_coins + 1
    elif event == 'push':
      print('Come on in!')
      state = 'locked'
```
---
And we have a big if statement that decides what do do if the state is locked...
*******************************************
```python
state = 'locked'
event_list = ['coin', 'push', 'coin', 'coin', 'push', 'push']
num_coins = 0
for event in event_list:
  if state == 'locked':
    if event == 'coin':
      state = 'unlocked'
      num_coins = num_coins + 1
    elif event == 'push':
      pass
[[  elif state == 'unlocked':
    if event == 'coin':
      num_coins = num_coins + 1
    elif event == 'push':
      print('Come on in!')
      state = 'locked']][[If state is unlocked]]
```
---
vs unlocked.
*******************************************
```python
state = 'locked'
event_list = ['coin', 'push', 'coin', 'coin', 'push', 'push']
num_coins = 0
for event in event_list:
  if state == 'locked':
    if event == 'coin':
      state = 'unlocked'
      num_coins = num_coins + 1
    elif event == 'push':
      pass
  elif state == 'unlocked':
    if event == 'coin':
      num_coins = num_coins + 1
    elif event == 'push':
      print('Come on in!')
      state = 'locked'
```
---
Note that the turnstile also uses an extra variable `num_coins` that keeps
track of how many coins it has.

So, that is the turnstile. See that you follow what's going on by walking it
through Python Tutor.

Next, let's get to a more practical example.
*********************************************
## Problem: Text to HTML

Convert this text

```
This *is* the next big thing.
```

to this HTML code

```html
This <em>is</em> the next big thing.
```
---
Let's say that you are given this problem:

Convert the text you see above
to the HTML code you see below. To be more precise, take the text surrounded by
two asterisks (\*) and surround them with an `<em>` tag (for emphasis) in the output.

How would you do this? Think about this a moment. Write down your strategy
for how you would do it.

The next slide contains the solution, using a state machine.
***********************************************
```python
sentence = 'This *is* the next big thing.'
new_sentence = ''
state = 'open'
for char in sentence:
  if state == 'open':
    if char == '*':
      state = 'emphasis'
      new_sentence += '<em>'
    else:
      new_sentence += char
  elif state == 'emphasis':
    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char
```
---
This is the solution. First, I'd like you to read over this program and try
to understand how it works. Take notes if you'd like.
***********************************************
```python
sentence = 'This *is* the next big thing.'
new_sentence = ''
state = 'open'
for char in sentence:
  if state == 'open':
    if char == '*':
      state = 'emphasis'
      [[new_sentence += '<em>']][[Same as new_sentence = new_sentence + '<em>']]
    else:
      new_sentence += char
  elif state == 'emphasis':
    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char
```
---
Next, I want to make a note about the `+=` operator. `+=` is a short-hand operator.

For example, the long hand form of

```
n += 1
```

is

```
n = n + 1
```

Get used to this short hand. You will like it.
***********************************************
```python
sentence = 'This *is* the next big thing.'
new_sentence = ''
state = 'open'
for char in sentence:
  if state == 'open':
    if char == '*':
      state = 'emphasis'
      new_sentence += '<em>'
    else:
      new_sentence += char
  elif state == 'emphasis':
    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char
```
---
This program has several elements you recognize. First, it uses the
accumulator pattern.

Can you spot the *accumulator variable* and the *accumulator* statements?

The next slide will reveal them.
***********************************************
```python
sentence = 'This *is* the next big thing.'
[[new_sentence]][[accumulator variable]] = ''
state = 'open'
for char in sentence:
  if state == 'open':
    if char == '*':
      state = 'emphasis'
      [[new_sentence += '<em>']][[accumulator]]
    else:
      [[new_sentence += char]][[accumulator]]
  elif state == 'emphasis':
    if char == '*':
      state = 'open'
      [[new_sentence += '</em>']][[accumulator]]
    else:
      [[new_sentence += char]][[accumulator]]
```
---
Are they what you expected?
***********************************************
```python
sentence = 'This *is* the next big thing.'
new_sentence = ''
state = 'open'
for char in sentence:
  if state == 'open':
    if char == '*':
      state = 'emphasis'
      new_sentence += '<em>'
    else:
      new_sentence += char
  elif state == 'emphasis':
    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char
```
---
This program also uses the state machine pattern.

Can you spot the state variable? What is the sequence of events? Where is
the if statement to decide the action to take based on the current state?
***********************************************
```python
sentence = 'This *is* the next big thing.'
new_sentence = ''
[[state]][[The state variable]] = 'open'
for char in sentence:
  if state == 'open':
    if char == '*':
      state = 'emphasis'
      new_sentence += '<em>'
    else:
      new_sentence += char
  elif state == 'emphasis':
    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char
```
---
Well the state variable should be obvious enough, since it's literally called
`state`.
***********************************************
```python
[[sentence]][[The sequence of events]] = 'This *is* the next big thing.'
new_sentence = ''
state = 'open'
for char in sentence:
  if state == 'open':
    if char == '*':
      state = 'emphasis'
      new_sentence += '<em>'
    else:
      new_sentence += char
  elif state == 'emphasis':
    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char
```
---
The sequence of events was less obvious. It's actually the sequence of characters
in the `sentence`.

*What? You can do that?*

*Yes! You can!*

I am the instructor, and I said you can, so you can.

Each character in `sentence` is like an event occurring to our state machine,
which acts like a toggle switch, in that whenever it see an asterisk (\*), it
toggles its state from "open" to "emphasis", and vice versa.

The presence of the state variable, is how it knows when to output an open tag
`<em>` - when it is transitioning from the "open" state to the "emphasis" state,
and when to output a close tag `</em>`, when its transitioning back from the
"emphasis" state to the "open" state.
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/1.jpg)

---
Let's visualize walking through this program. At the beginning, the state
is "open", while `new_sentence` is still empty.
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/2.jpg)

---
When we process the first character of the sentence, ...
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/3.jpg)

---
we want to append it to `new_sentence`.
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/4.jpg)

---
We do the same with the next characters...
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/5.jpg)

---
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/6.jpg)

---
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/7.jpg)

---
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/8.jpg)

---
Until we encounter the first asterisk (\*), ...
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/9.jpg)

---
This is when the state transition occurs. The state changes from "open" to
"emphasis".
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/10.jpg)

---
We also append the open tag `<em>` to `new_sentence`.
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/11.jpg)

---
The next characters are append to `new_sentence` as normal.
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/12.jpg)

---
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/13.jpg)

---
When we encounter the second asterisk,...
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/14.jpg)

---
First we switch the state back from "emphasis" to "open". This is the
second state transition.
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/15.jpg)

---
Then we append the close tag `</em>` to `new_sentence`. Now we are operating
back in the "open" state and collecting characters again like normal.
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/16.jpg)

---
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/17.jpg)

---
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/18.jpg)

---
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/19.jpg)

---
****************************************
![Diagram 1](./lessons/python/lesson-5/convert-2-html/20.jpg)

---
Until the end of the characters in `sentence` is reached.
***********************************************
```python
sentence = 'This *is* the next big thing.'
new_sentence = ''
state = 'open'
for char in sentence:
  if state == 'open':
    if char == '*':
      state = 'emphasis'
      new_sentence += '<em>'
    else:
      new_sentence += char
  elif state == 'emphasis':
    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char
```
---
This is the program again. Again, see that you understand how it works. You may
walk it through Python Tutor.

There are more than one way to understand the state machine pattern. One way
that I like is to imagine that there are actually...
***********************************************
```python
sentence = 'This *is* the next big thing.'
new_sentence = ''
state = 'open'
for char in sentence:
  if state == 'open':
[[    if char == '*':
      state = 'emphasis'
      new_sentence += '<em>'
    else:
      new_sentence += char]][[Program number 1]]
  elif state == 'emphasis':
[[    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char]][[Program number 2]]
```
---
multiple programs
that are running within the state machine - one for each kind of state that
it can have. Whenever it encounters an event that it has to process,...
***********************************************
```python
sentence = 'This *is* the next big thing.'
new_sentence = ''
state = 'open'
for char in sentence:
  [[if state == 'open':]][[Selects program 1]]
    if char == '*':
      state = 'emphasis'
      new_sentence += '<em>'
    else:
      new_sentence += char
  [[elif state == 'emphasis':]][[Selects program 2]]
    if char == '*':
      state = 'open'
      new_sentence += '</em>'
    else:
      new_sentence += char
```
---
it
simply selects one of those programs to execute based on what the current
state is - and that's what the if statement does.
***********************************************
## Summary

* The `+=` operator
* The state machine pattern
---
That's it for this lesson. Here is what you learned.
***********************************************
## Exercises

[To the exercises!](https://gist.github.com/airportyh/283d98c18b3d2947513782d0fcf76e48)

---
Please attempt to complete these exercises to the best of your ability, but
don't resist ask questions.
