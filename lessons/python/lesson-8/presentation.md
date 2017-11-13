# Lesson 8 -
## Pygame: Making a Game
---
Welcome to lesson 8! This time, you'll learn the skills
to make a game!!!
*****************************************************
# Agenda

1. The game loop
2. Updating variables triggered by events
3. Updating variables over time
4. Collision detection
5. Displaying text
6. Restarting game using states.
---
These are the concepts we'll cover in this lesson, after
you learn them, you'll be able to put them together to
build a simple game.
*****************************************************
# Game Loop

A loop that keeps running for the duration of the entire
game. The code within the body of the loop takes care
of rendering the game, updating variables in the game,
and event handling.

---
First let's talk about the game loop.
*****************************************************
# Game Loop: Example

```python
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                pen_down = False
    ...
```

---
You've seen a game loop --- it looks like this. A game loop
in Pygame is simply a while loop. It is responsible for
fetching the latest events and processing them. It is also
responsible for updating the display as it needs to, in
the drawing program.
*****************************************************
# Game Loop: Components

1. Event handling
2. Automatic updates
3. Rendering

---
Within the body of this game loop, it has 3 main responsibilities,
and we in general separate them into 3 sections.

The *Event handling* section goes through each new event received and updates
the variables in some way.

The *Automatic updates* section performs any updates to the variables
that represents the scene --- the set of objects represented in the game ---
that occur automatically over time - such as a ball that bounces back and forth,
or an enemy character that moves by itself.

The *Rendering* section draws the scene of the game. It only draws one frame
of the game --- or one page in a flip book, the next time through this loop
it would draw the next frame(page), and so on.
*****************************************************
# Initialization

```python
# Initialization
...
while not exit_game:
  # Event handling
  ...
  # Automatic updates
  ...
  # Rendering
  ...
```

---
So, we'll divide the body of the game loop into these 3 sections like so.

Just above the game loop, there are various variables we'll need to define
and initialize. We'll call this section the *initialization section*.

Code examples that are coming up later will specify which of these 3 sections
the code is meant to go inside of.

Next, let's dig into the *rendering* section.
*****************************************************
# Rendering

1. Repaint background
2. Draw individual objects

---
Let's start with rendering, because you need that in order to even see
anything.

In most games, these are the steps the rendering phase takes.

First, it repaints the entire background --- which will paint over
the previous frame of the game.

Then, it draws each object in the scene.
*****************************************************
# Rendering a Ball

```python
# Initialization
ball_x = 300
ball_y = 200
```

```python
# Rendering
screen.fill(BLACK)
pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
pygame.display.update()
```

---
This is an example of a ball being rendered.
*****************************************************
# Rendering a Ball

```python
# Initialization
[[ball_x = 300
ball_y = 200]][[Initialize ball position]]
```

```python
# Rendering
screen.fill(BLACK)
pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
pygame.display.update()
```

---
In the initialization section of the program (outside of the game loop),
we initialize two variables `ball_x` and `ball_y` to represent the
position of the ball x and y. We the initial position to roughly the middle
of the screen.
*****************************************************
# Rendering a Ball

```python
# Initialization
ball_x = 300
ball_y = 200
```

```python
# Rendering
[[screen.fill(BLACK)]][[Draw dark background]]
pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
pygame.display.update()
```

---
In the rendering section, we first draw the dark background. The reason we
are redrawing the background every single time through the loop is that
if the ball moves, we want to erase its last image to prevent it from looking
like the ball left a trail.
*****************************************************
# Rendering a Ball

```python
# Initialization
ball_x = 300
ball_y = 200
```

```python
# Rendering
screen.fill(BLACK)
[[pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)]][[Draw ball]]
pygame.display.update()
```

---
Next, we draw the ball. A red ball with 50 pixel radius, right at the
position of the ball: `(ball_x, ball_y)`.
*****************************************************
# Rendering a Ball

```python
# Initialization
ball_x = 300
ball_y = 200
```

```python
# Rendering
screen.fill(BLACK)
pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
[[pygame.display.update()]][[Update the display]]
```

---
Finally, we must call the `pygame.display.update()` function in order to
flip the display and show the image.

So this is how the rendering section for a simple program looks like. This
is the [example code](https://gist.github.com/airportyh/d48e6c46089ef241e2fbab24e86a18fd).

Now, let's make the ball move around.
*****************************************************
# Event Handling

1. Move by keyboard
2. Move by mouse

---
To add the ability for a user to move the ball, we can do one of two things:

1. Let the keyboard control the ball
2. Let the mouse position control the ball
*****************************************************
# Moving the Ball: Keyboard

![Arrow keys](/lessons/python/lesson-8/images/arrow-keys.png)

---
Let's start with using the arrow keys on the keyboard.
*****************************************************
# Moving the Ball: Keyboard

```python
# Event Handling
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            ball_y -= 5
```

---
We put this code in the event handling section of the game loop.

This says if the up arrow key (`pygame.K_UP`) is pressed down, then we'll
decrease the ball's y coordinate by 5 pixels. So the up arrow causes the ball
to move up in the screen. Now let's fill in if clauses for each arrow direction.
*****************************************************
# Moving the Ball: Keyboard

```python
# Event Handling
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            ball_y -= 5
        elif event.key == pygame.K_DOWN:
            ball_y += 5
        elif event.key == pygame.K_LEFT:
            ball_x -= 5
        elif event.key == pygame.K_RIGHT:
            ball_x += 5
```

---
There it is. This code allows the user to move the ball each direction using
the arrow keys on the keyboard. Here is the [example code](https://gist.github.com/airportyh/a5c30d2537a52d8d9958462d4a2ecd0a).
*****************************************************
# Moving the Ball: Mouse

![Mouse](/lessons/python/lesson-8/images/mouse.png)

---
Okay, now let's try the mouse.
*****************************************************
# Moving the Ball: Mouse

```python
# Event Handling
for event in pygame.event.get():
    if event.type == pygame.MOUSEMOTION:
        ball_x = event.pos[0]
        ball_y = event.pos[1]
```

---
This code detects `MOUSEMOTION` events, and whenever the mouse moves, it
changes the ball's position to to position of the mouse. So the ball
should now just follow the mouse.

Here is the full [code example](https://gist.github.com/airportyh/a932f22ad74209a090f850d2470c4ff2) with *both* keyboard and mouse implemented.
*****************************************************
# Automatic Updates

An bouncing ball.

---
Now, we'll implement a ball that bounces by itself. In addition to our
device-controlled ball.
*****************************************************
# A Bouncing Ball

```python
# Initialization
ball2_x = 100
ball2_y = 100
```

```python
# Automatic Updates
ball2_x += 1
ball2_y += 1
```

```python
# Rendering
screen.fill(BLACK)
pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
pygame.draw.circle(screen, BLUE, (ball2_x, ball2_y), 50)
pygame.display.update()
```

---
This is the code that makes it happen.
*****************************************************
# A Bouncing Ball

```python
# Initialization
[[ball2_x = 100
ball2_y = 100]][[Initial ball position]]
```

```python
# Automatic Updates
ball2_x += 1
ball2_y += 1
```

```python
# Rendering
screen.fill(BLACK)
pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
pygame.draw.circle(screen, BLUE, (ball2_x, ball2_y), 50)
pygame.display.update()
```

---
The first thing we'll do is to define two new variables to store the position
of the second ball, and initialize its position --- we'll put it in the top-left
corner here.
*****************************************************
# A Bouncing Ball

```python
# Initialization
ball2_x = 100
ball2_y = 100
```

```python
# Automatic Updates
[[ball2_x += 1
ball2_y += 1]][[Move the ball]]
```

```python
# Rendering
screen.fill(BLACK)
pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
pygame.draw.circle(screen, BLUE, (ball2_x, ball2_y), 50)
pygame.display.update()
```

---
Then, we'll add something to the *automatic updates* section of the game loop.
The automatic updates section is for putting code that would move objects in
the game even if no events are occurring. Because we want the second ball
to be continuously moving, this is the right place.

This code moves the ball a pixel to the left and a pixel to the bottom for
each iteration of the while loop. How fast the ball moves depends on the amount
used here, and also how fast the while loop runs --- more on that later.
*****************************************************
# A Bouncing Ball

```python
# Initialization
ball2_x = 100
ball2_y = 100
```

```python
# Automatic Updates
ball2_x += 1
ball2_y += 1
```

```python
# Rendering
screen.fill(BLACK)
pygame.draw.circle(screen, RED, (ball_x, ball_y), 50)
[[pygame.draw.circle(screen, BLUE, (ball2_x, ball2_y), 50)]][[Draw the second ball]]
pygame.display.update()
```

---
The last part needed to implement the second ball is to draw it on the screen
--- in addition to the first ball.

Here is the [example code](https://gist.github.com/airportyh/c3ad29b01c1c6135223dc85130da426b) up to this point.

Copy and run this program. You will notice that the ball after moving a bit,
the ball just falls off the screen. What can we do to make it bounce off
of the edge and come back the opposite direction?

Thank about that. If you think you have a good solution, please try to
implement it, and then move on to the next slide for my solution.
*****************************************************
# A Bouncing Ball

```python
# Automatic Updates
ball2_x += 1
ball2_y += 1
```

---
Looking at this code for updating the position of the ball again, note that
we are adding 1 pixel to both directions. We say this ball has the speed
of 1 pixel per frame in the x direction, and 1 pixel per frame in
the y direction.

If we knew how fast the frames are being rendered, we'd be
be able to calculate the speed in terms of time. For example, let's say
the game is rendering 30 frames per second, then at 1 pixel per frame,
that would mean the ball is moving at 30 pixels per second. More on frame rates
later.

All of that to say that the 1's in this code in fact represent the speed of
the ball.
*****************************************************
# A Bouncing Ball

```python
# Automatic Updates
ball2_x += ball2_speed_x
ball2_y += ball2_speed_y
```

---
If we want to changed the speed and direction of the ball, we need to extract
these fixed speeds into variables which can change. We'll called these variables:

* `ball2_speed_x` --- the speed of the ball in the x direction (negative value
  means it's moving to the left, positive means right)
* `ball2_speed_y` --- the speed of the ball in the y direction (negative value
  means it's moving up, positive means down)
*****************************************************
# A Bouncing Ball

```python
# Initialization
ball2_x = 100
ball2_y = 100
ball2_speed_x = 1
ball2_speed_y = 1
```

```python
# Automatic Updates
ball2_x += ball2_speed_x
ball2_y += ball2_speed_y
```

---
Now we'll also need to define and initialize these variables. We'll have the
ball going down and to the right like we did before.
*****************************************************
# A Bouncing Ball

```python

```

---
Now we need to make the ball change direction when it hits an edge of the
screen.
