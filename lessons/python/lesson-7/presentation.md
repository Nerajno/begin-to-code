# Pygame Part 2: Events
---
Hello! This lesson will introduce you to the concept of *events*
in Pygame. *Events* is an important concept in programming
and you will see it introduced over and over again in all sorts of
contexts. In particular, you will see it again in web programming
with JavaScript.
********************************************************
## Pygame Events

* Mouse events
  * button click
  * move
* Keyboard events
  * key pressed
  * key release
* Window events
  * quit
  * window activated
  * window deactivated
  * window resized

---
Different types of events may occur to the Pygame application through
the course of the game. These are the major types: mouse events,
keyboard events, and window events. By writing code to receive and process
these events, you can make your game interactive!!!
********************************************************
## pygame.event

```python
new_events = pygame.event.get()
```
---
Pygame has a `pygame.event` module, and with it, you can get a list of the
new events by calling its `get` function.

This line of code retrieves the list of the *new* events that have not yet
been processed and assigns that list to the `new_events` variable. If there
are no new events, `new_events` will be an empty list.
********************************************************
## Looping through events

```python
new_events = pygame.event.get()
for event in new_events:
  print('Got event', event)
```

---
Once you retrieved the new list of events, you can use a for loop to go
through each one and print it out.
*******************************************************
## First program with events

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))
pygame.display.update()

while True:
    new_events = pygame.event.get()
    for event in new_events:
        print('Got event', event)
```

---
This is a simple program that simply prints out any events that occurred.
*******************************************************
## First program with events

```python
[[import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))
pygame.display.update()]][[Pygame setup code]]

while True:
    new_events = pygame.event.get()
    for event in new_events:
        print('Got event', event)
```

---
This is your standard Pygame setup code. It:

1. Brings in the Pygame module.
2. Initializes it.
3. Creates a screen 600x400 in dimension.
4. Sets the caption of the window.
5. Paints the canvas black.
6. Flips the display to display the blackness.
*******************************************************
## First program with events

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))
pygame.display.update()

[[while True:]][[Keep this game running forever]]
    new_events = pygame.event.get()
    for event in new_events:
        print('Got event', event)
```

---

This while loop causes the game to continue going forever, which is allowing
Pygame to listen for events from the system.
*******************************************************
## First program with events

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))
pygame.display.update()

while True:
    new_events = [[pygame.event.get()]][[Retrieve all events since last time]]
    for event in new_events:
        print('Got event', event)
```

---
Every time through this while loop, we call `pygame.event.get()` to retrieve
all events which occurred since the last time this same function was called.
If no events had occurred since then, this function returns an empty list.
*******************************************************
## First program with events

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))
pygame.display.update()

while True:
    new_events = pygame.event.get()
    [[for event in new_events:]][[Loop through event new event]]
        print('Got event', event)
```
---
We use a for loop to process each event in the `new_events` list.
*******************************************************
## First program with events

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))
pygame.display.update()

while True:
    new_events = pygame.event.get()
    for event in new_events:
        [[print('Got event', event)]][[Print the event]]
```
---
Here we are just printing out each new event.
*******************************************************
## First program with events

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))
pygame.display.update()

while True:
    new_events = pygame.event.get()
    for event in new_events:
        print('Got event', event)
```

---
Type in this program, save it as any name other than `pygame.py`, and
run it.
*******************************************************
## Mouse Motion Events

```
Got event <Event(4-MouseMotion {'pos': (0, 288), 'rel': (0, 24), 'buttons': (0, 0, 0)})>
Got event <Event(4-MouseMotion {'pos': (0, 302), 'rel': (0, 14), 'buttons': (0, 0, 0)})>
Got event <Event(4-MouseMotion {'pos': (0, 315), 'rel': (0, 13), 'buttons': (0, 0, 0)})>
Got event <Event(4-MouseMotion {'pos': (0, 321), 'rel': (0, 6), 'buttons': (0, 0, 0)})>
Got event <Event(4-MouseMotion {'pos': (0, 326), 'rel': (0, 5), 'buttons': (0, 0, 0)})>
Got event <Event(4-MouseMotion {'pos': (0, 328), 'rel': (0, 2), 'buttons': (0, 0, 0)})>
Got event <Event(4-MouseMotion {'pos': (0, 329), 'rel': (0, 1), 'buttons': (0, 0, 0)})>
Got event <Event(4-MouseMotion {'pos': (0, 330), 'rel': (0, 1), 'buttons': (0, 0, 0)})>
```

---
Once the program is running, you may notice that when you move your mouse
pointer within the window, the terminal starts becoming busy printing
events like these. These are `MouseMotion` events, and they are fired every time
your mouse moves within the Pygame window.
*******************************************************
## Mouse Click Events

```
Got event <Event(5-MouseButtonDown {'pos': (130, 232), 'button': 1})>
Got event <Event(6-MouseButtonUp {'pos': (130, 232), 'button': 1})>
```

---
Now try clicking mouse button in the window, you should get events that look
like these.

These are `MouseButtonDown` and `MouseButtonUp` events. Along with
the mouse button event is information about which mouse button was pressed.
*******************************************************
## Window Deactivate Event

```
Got event <Event(1-ActiveEvent {'gain': 0, 'state': 3})>
```

---
You may also notice that if you switch to another application, you get this
event printed. This is a ActivateEvent that signals that the Pygame window
was deactivated.
*******************************************************
## Window Deactivate Event

```
Got event <Event(1-ActiveEvent {'gain': 1, 'state': 2})>
```

---
Inversely, if you focus back to the Pygame window, it will print this event,
which is another ActivateEvent, but this one signals that the window has
been activated.
*******************************************************
## Keyboard Events

```
Got event <Event(3-KeyUp {'key': 117, 'mod': 0, 'scancode': 3})>
Got event <Event(2-KeyDown {'unicode': 'o', 'key': 111, 'mod': 0, 'scancode': 1})>
Got event <Event(2-KeyDown {'unicode': 'e', 'key': 101, 'mod': 0, 'scancode': 2})>
Got event <Event(3-KeyUp {'key': 101, 'mod': 0, 'scancode': 2})>
Got event <Event(3-KeyUp {'key': 111, 'mod': 0, 'scancode': 1})>
Got event <Event(3-KeyUp {'key': 104, 'mod': 0, 'scancode': 38})>
Got event <Event(2-KeyDown {'unicode': 'u', 'key': 117, 'mod': 0, 'scancode': 3})>
Got event <Event(2-KeyDown {'unicode': 'n', 'key': 110, 'mod': 0, 'scancode': 37})>
Got event <Event(2-KeyDown {'unicode': 's', 'key': 115, 'mod': 0, 'scancode': 41})>
Got event <Event(2-KeyDown {'unicode': 'e', 'key': 101, 'mod': 0, 'scancode': 2})>
Got event <Event(2-KeyDown {'unicode': 'o', 'key': 111, 'mod': 0, 'scancode': 1})>
```

---
Now start typing keys on your keyboard and you will see something like the above.
Whenever you depress a key, you will get a `KeyDown` event, and then when you
release it, you will get a corresponding `KeyUp` event. Each key event
with attach with it information as to what key was pressed.
*******************************************************
## Detecting Event Type

`event.type` - event type number

---
There's a simple way to detect, or differentiate which type of event a
particular event is - using the `type` attribute of the event, which
gives you a numeric code.

* 1 means an ActiveEvent.
* 2 means a KeyDown event.
* 3 means an KeyUp event.
* 4 means a MouseMotion event.
* 5 means a MouseButtonDown event.
* 6 means a MouseButtonUp event.
* and 12 means a Quit event.
*******************************************************
## Event Types

| #  | Alias                  | What it is                                       |
|----|------------------------|--------------------------------------------------|
| 1  | pygame.ACTIVEEVENT     | The window was activated or deactivated          |
| 2  | pygame.KEYDOWN         | A keyboard key was pressed down                  |
| 3  | pygame.KEYUP           | A keyboard key was released after it was pressed |
| 4  | pygame.MOUSEMOTION     | The mouse moved somewhere within the window      |
| 5  | pygame.MOUSEBUTTONDOWN | A mouse button was clicked                       |
| 6  | pygame.MOUSEBUTTONUP   | A mouse button was released after being clicked  |
| 12 | pygame.QUIT            | The user clicked on the close button to quit     |

---
Here is that information in a table format.

The alias is an attribute on the `pygame` module which you can use in place
of the actual number itself. Why would you write `pygame.KEYDOWN` when you
could just write `2`? Because when you are reading the program, you are not
likely to have remembered what the number 2 meant, whereas the meaning of
KEYDOWN is intuitive.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True

print('Bye!!!')
pygame.quit()
```
---
This program handles the quit event gracefully - for once.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

[[finished = False]][[A variable to remember whether to continue the game]]
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True

print('Bye!!!')
pygame.quit()
```
---
First, in order to handle the Quit event, we need to declare a boolean variable
outside of the while loop to remember whether or not we are finished with
the game. At the start, with set this to `False` in order to get the game
going.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while [[not finished]][[Only continue the game if we are not yet finished]]:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True

print('Bye!!!')
pygame.quit()
```
---
We now use a conditional to decide whether to continue running the game.
We base it on the current value of the `finished` variable. If `finished` is
`True`, then we'll drop out of this while loop and end the game.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while not finished:
    [[new_events = pygame.event.get()]][[Get latest events]]
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True

print('Bye!!!')
pygame.quit()
```
---
Now we retrieve the list of the new events as before within the body of the
while loop.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while not finished:
    new_events = pygame.event.get()
    [[for event in new_events:]][[Loop through each event]]
        if event.type == pygame.QUIT:
            finished = True

print('Bye!!!')
pygame.quit()
```
---
And loop through each new event using a for loop.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        [[if event.type == pygame.QUIT:]][[Detect Quit event]]
            finished = True

print('Bye!!!')
pygame.quit()
```
---
Here we use an if-statement to detect we have a Quit event.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if [[event.type]][[Get's type code]] == pygame.QUIT:
            finished = True

print('Bye!!!')
pygame.quit()
```
---
Here is where we use `event.type` to get the event's type code.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == [[pygame.QUIT]][[Alias for 12]]:
            finished = True

print('Bye!!!')
pygame.quit()
```
---
We compare `event.type` to the alias `pygame.QUIT`, which happens to be 12.
Again, we could have simply written 12 here in place of `pygame.QUIT`, but
`pygame.QUIT` makes more sense to an onlooker.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            [[finished = True]][[User quit, we are finished!!!]]

print('Bye!!!')
pygame.quit()
```
---
In the event of Quit, we are going to end the game by setting
the value of the `finished` variable to `False`, so that
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while [[not finished]][[False if finished is True]]:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True

print('Bye!!!')
pygame.quit()
```
---
...the next time the while loop evaluates this condition, it evaluates to
`False`, and the loop exits.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while [[not finished]][[False if finished is True]]:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True

[[print('Bye!!!')]][[Print bye]]
pygame.quit()
```
---
We print a little message to the terminal at the end.
*******************************************************
## Handling the Quit Event

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Handle Quit Example')

screen.fill((0, 0, 0))
pygame.display.update()

finished = False
while [[not finished]][[False if finished is True]]:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True

print('Bye!!!')
[[pygame.quit()]][[Pygame clean up]]
```
---
And incidentally, we call the `quit` function of `pygame` to ask Pygame
to clean up after itself, which - although not necessary - is recommended.
*******************************************************
## Additional Event Attributes

* `pygame.KEYDOWN`, `pygame.KEYUP` - what key was pressed?
* `pygame.MOUSEMOTION`, `pygame.MOUSEBUTTONUP`, `pygame.MOUSEBUTTONDOWN` -
  where is the mouse?
* `pygame.MOUSEBUTTONUP`, `pygame.MOUSEBUTTONDOWN` - which mouse button was
  clicked?

---
Some events have some additional associated information attached with them.

For example,

* if a key was pressed, you might want to know which key it was.
* if the mouse was clicked, or is moving, you might want to know where the mouse
  is on the screen
* if the mouse was clicked, you might want to know which mouse button was
  clicked - the left or the right one.

This is achieved by using some addition attributes on the event object.
*******************************************************
## MouseButtonDown, MouseButtonUp Attributes

* `pos` - a 2-tuple representing position of the mouse when the button was
  clicked
* `button` - the button code (a number) representing the button that was pressed

---
When you click a mouse button, you trigger two separate events: MouseButtonDown
and MouseButtonUp. Both of these events offer a `pos` attribute to tell you
where within the screen you clicked. And both of them offer a `button` attribute
to tell you which button on the mouse you clicked - which is a number that
could be, 1, 2, 3, depending on the button and the type of mouse
that you are using. Mouse buttons 4 and 5 are used for scrolling via the mouse.
*******************************************************
## MouseMotion Attributes

* `pos` - a 2-tuple representing position of the mouse when the button was
  clicked
* `rel` - the relative position of the mouse vs where it was before
* `buttons` - 3-tuple representing the state of each of the buttons on the mouse

---
When you move the mouse, you trigger MouseMotion events. A MouseMotion event
also offers a `pos` attribute telling you the location of the mouse at this
instant. It also offers a `rel` attribute giving the relative position of the
mouse relative to where it was the last MouseMotion event was fired. Third,
it provides a `buttons` attribute which tells you what the buttons of each
of 3 possible buttons on the mouse are.
*******************************************************
## Mouse Click Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, (0, 255, 0), event.pos, 10)
            pygame.display.update()
```
---
Check out this example which uses a mouse click. *This is a partial code
example.* I am only showing the while loop portion in order to save space.

This program draws a new dot on the screen whenever the user clicks on the
screen - where they clicked.
*******************************************************
## Mouse Click Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif [[event.type == pygame.MOUSEBUTTONDOWN]][[Detects a click]]:
            pygame.draw.circle(screen, (0, 255, 0), event.pos, 10)
            pygame.display.update()
```
---
This condition detects a mouse click.
*******************************************************
## Mouse Click Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            [[pygame.draw.circle(screen, (0, 255, 0), event.pos, 10)]][[Draws a circle]]
            pygame.display.update()
```
---
When the mouse is clicked, we draw a circle on the screen.
*******************************************************
## Mouse Click Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, [[(0, 255, 0)]][[3-tuple RGB value for green]], event.pos, 10)
            pygame.display.update()
```
---
This circle is green.
*******************************************************
## Mouse Click Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, (0, 255, 0), [[event.pos]][[Position of the mouse]], 10)
            pygame.display.update()
```
---
We are putting the center of the circle where the mouse was when it was clicked.
*******************************************************
## Mouse Click Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, (0, 255, 0), event.pos, 10)
            pygame.display.update()
```
---
So there you have it! An interactive program. Please take a moment now to
type this into a file of your own and play with it. You can find the [complete
code example here](https://gist.github.com/airportyh/77dbc6c8db48d9b2713cadce85d5ec4e).
*******************************************************
## KeyDown, KeyUp Attributes

* `unicode` - (`pygame.KEYDOWN` only) the character that was typed
* `key` - the key code (a number) representing key that was typed
* `mod` - modifier keys that are simultaneously being pressed

---
For keyboard events, these are some extra attributes you have access to
as well.

* `unicode` - which is only available on the KeyDown event - is an
attribute that gives you access to the actual character that was typed - if
one is available.
* `key` is a numeric key code corresponding to the key you
typed.
* `mod` is a number that represents which of the modifier keys are
currently being pressed.
*******************************************************
## Keyboard Event Example

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))

x = 300
y = 200
pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
pygame.display.update()
```

---
Let's say we make a game that has a ball in the middle of the screen.
*******************************************************
## Keyboard Event Example

```python
[[import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))]][[Pygame setup]]

x = 300
y = 200
pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
pygame.display.update()
```

---
We do the standard Pygame initialization stuff. We've set the size of the
screen to 600 wide by 400 high.
*******************************************************
## Keyboard Event Example

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))

[[x = 300
y = 200]][[The coordinates of the ball]]
pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
pygame.display.update()
```

---
We create the variables `x` and `y` here, to represent the position of the ball.
Initially, we put it in the center of the screen: (300, 200).
*******************************************************
## Keyboard Event Example

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))

x = 300
y = 200
pygame.draw.circle(screen, (0, 255, 0), [[(x, y)]][[Coordinates of the ball as a 2-tuple]], 10)
pygame.display.update()
```

---
Now we use the `x` and `y` variables as a 2-tuple to draw the ball on
the screen.
*******************************************************
## Keyboard Event Example

```python
import pygame

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame Events Example')

screen.fill((0, 0, 0))

x = 300
y = 200
pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
[[pygame.display.update()]][[Flip the display to show it]]
```

---
And of course, don't forget to flip the display to actually show the drawing.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
Now let's look further down in this program at the while loop. This is a
*partial program*. You can see the
[whole program here](https://gist.github.com/airportyh/5e63e2d5d288569d0d9e519b0bf77a39).
*******************************************************
## Keyboard Event Example

```python
while not finished:
    [[new_events = pygame.event.get()]][[Get the new events]]
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
Like before, we'll get the list of new events.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    [[for event in new_events:]][[Loop through each event]]
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
Then, loop through each event and process them.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        [[if event.type == pygame.QUIT:
            finished = True]][[Handle user quitting]]
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
This if-statement block handles if the user clicks on the close button on
the window to quit.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        [[elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()]][[Handles key presses]]
```

---
This elif-statement block handles key presses.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif [[event.type == pygame.KEYDOWN]][[Detects key press]]:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
This conditional here detects if a key has been pressed down.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if [[event.key == pygame.K_LEFT]][[Detects left arrow key]]:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
This nested conditional here detects if the key pressed was the left arrow
key.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if [[event.key]][[The key code for the pressed key]] == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
`event.key` gives us a unique numeric key code that represents the pressed key.
We are using this number to detect if the user pressed the key we want to
handle.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == [[pygame.K_LEFT]][[Key code for the left arrow key]]:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
`pygame.K_LEFT` is an alias that gives the key code for the left arrow key,
which is 276. We could have written 276 in place of `pygame.K_LEFT`, but
`pygame.K_LEFT` is more intuitive to humans as to what the key is.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                [[x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()]][[Do this if left arrow was pressed]]
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
These instructions within the if block are what we execute whenever the
left arrow key is pressed.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                [[x = x - 5]][[Move ball to the left]]
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
The first thing we do is to move the ball 5 pixels to the left - conceptually -
by decreasing the `x` variable by 5. This doesn't update the drawing though.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                [[screen.fill((0, 0, 0))]][[Repaint the background black]]
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
Next, we'll repaint the entire background black. Why? I am going to defer
answering this.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                [[pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)]][[Draw new ball]]
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
Now we draw the ball at its new updated position, still at `(x, y)`, but now
x has an updated value.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                [[pygame.display.update()]][[Flip the display]]
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
And still we have to remember to flip the display before it will update it.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            [[elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()]][[Handle a right arrow press]]
```

---
This is the code for handling a right arrow press. It mirrors the code
for the left arrow press.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
So this is the code. Again, you get get the
[entire code example here](https://gist.github.com/airportyh/5e63e2d5d288569d0d9e519b0bf77a39).

Run this code. Then, try to make it do more:

1. Pressing the up arrow key (`pygame.K_UP`) makes the ball move up.
2. Pressing the down arrow key (`pygame.K_DOWN` - not to be confused with
  `pygame.KEYDOWN`) makes the ball move down.
*******************************************************
## Keyboard Event Example

```python
while not finished:
    new_events = pygame.event.get()
    for event in new_events:
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x - 5
                [[screen.fill((0, 0, 0))]][[Why have to do this?]]
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
            elif event.key == pygame.K_RIGHT:
                x = x + 5
                screen.fill((0, 0, 0))
                pygame.draw.circle(screen, (0, 255, 0), (x, y), 10)
                pygame.display.update()
```

---
Now, can you answer the question: why do we have to repaint the screen
black at this point?

If you want a hint, try removing this line or commenting it out in your
version of the program.
*******************************************************
## Summary

* Pygame events
* Quit event
* Mouse events
* Keyboard events
* Handling events
---
This is what you learned.
*******************************************************
## Homework

[7 exercises](https://gist.github.com/airportyh/923b49ec02469e554e1fe693aaebb8d1)

---
Here is your homework! Good luck!!!
