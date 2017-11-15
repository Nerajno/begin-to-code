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
# Game Loop: Sections

1. Event handling
2. Automatic updates
3. Rendering

---
Within the body of this game loop, it has 3 main responsibilities,
and we in general separate them into 3 sections.

The *Event handling* section goes through each new event received and updates
the state of the game (the variables) in some way.

The *Automatic updates* section performs any updates to the state
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

But wait!!! There's one additional section just above the game loop.
We'll call this section the *initialization section*.
It's where we define and initialize various variables we'll need.

Code examples that are coming up later will specify which of these 4 sections
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
position of the ball x and y. We set the initial position to roughly the middle
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

![Arrow keys](lessons/python/lesson-8/images/arrow-keys.png)

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

Copy and run this code to see it working.
*****************************************************
# Moving the Ball: Mouse

![Mouse](lessons/python/lesson-8/images/mouse.png)

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

Copy and run this code to see it working.
*****************************************************
# Automatic Updates

![A bouncing ball](lessons/python/lesson-8/images/bouncing-ball.png)

---
Now, we'll implement a ball that bounces by itself, in addition to our
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
This code makes the ball move by itself (bouncing is the next step).
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

Think about that. If you think you have a good solution, please try to
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
these fixed speeds into variables which can change. We'll use these variables:

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
# Edge Detection

![Ball hitting edge](lessons/python/lesson-8/images/ball-edge.png)

---
Now we need to make the ball change direction when it hits an edge of the
screen.

Let's do that for the bottom edge first. So if the ball hit the bottom edge,
as you see on the screen, and you needed to write an if statement to detect
this, what would the conditional clause of the if statement look like?

Think about this for a minute, write down your answer, and then go on to the
next slide to reveal the answer.
*****************************************************
# Edge Detection

```python
# Automatic Updates
if ball2_y + 50 >= SCREEN_HEIGHT:
```

---
This is the answer. We want to see if the lowest part of the ball: the ball's
y position plus its radius exceeds the height of the screen.
*****************************************************
# Edge Detection

```python
# Automatic Updates
if ball2_y + 50 >= SCREEN_HEIGHT:
  WHAT TO DO HERE?
```

---
Now, what do we want to do if the condition is true? We want to make the ball
go the other way. Remember, the direction of the ball is determined by its
speed variables: `ball2_speed_x` and `ball2_speed_y`.

How would you flip its
direction on the y axis (we can leave the x axis alone, and let it continue
  moving in the same direction).
*****************************************************
# Edge Detection

```python
# Automatic Updates
if ball2_y + 50 >= SCREEN_HEIGHT:
  ball2_speed_y = ball2_speed_y * -1
```

---
We can change the sign of of the speed by multiplying it with -1. This causes
the direction of the ball in the y axis to flip.
*****************************************************
# Edge Detection

```python
# Automatic Updates
if ball2_y + 50 >= SCREEN_HEIGHT:
  ball2_speed_y = ball2_speed_y * -1
ball2_x += ball2_speed_x
ball2_y += ball2_speed_y
```

---
The two lines that update the position of the ball come into play next...
*****************************************************
# Edge Detection

```python
# Automatic Updates
if ball2_y + 50 >= SCREEN_HEIGHT:
  ball2_speed_y = ball2_speed_y * -1
ball2_x += ball2_speed_x
[[ball2_y += ball2_speed_y]][[This is going to add a negative number]]
```

---
Changing the sign of `ball2_speed_y` to a negative number is going to cause
the ball to go up over time, because this line which changes the ball's y
position is going to be adding a negative number, and therefore decreasing
its value.
*****************************************************
# Edge Detection

![Top edge](lessons/python/lesson-8/images/ball-top-edge.png)

---
Okay, what condition do you need to detect the ball hitting this top edge?
*****************************************************
# Edge Detection

```python
if ball2_y - 50 <= 0:
  ball2_speed_y = ball2_speed_y * -1
```
---
The highest part of the ball is its y position minus its radius. So if we
compare that to 0 --- the y coordinate of the top edge, that tells us the
ball has reached the edge. If the ball reaches the edge, we flip its y
direction just the same by multiplying it by -1.

Now, let's do this for the other 2 walls. Please try to do this yourself. You
may start with [this version of the code](https://gist.github.com/airportyh/7c637c6e8300045cb2b292d304df6bc7).
When you've had a try at this yourself, you may go to the next slide for the
solutions.
*****************************************************
# Edge Detection

```python
# Automatic Updates
if ball2_y + 50 >= SCREEN_HEIGHT:
    ball2_speed_y = ball2_speed_y * -1
if ball2_y - 50 <= 0:
    ball2_speed_y = ball2_speed_y * -1
if ball2_x + 50 >= SCREEN_WIDTH:
    ball2_speed_x = ball2_speed_x * -1
if ball2_x - 50 <= 0:
    ball2_speed_x = ball2_speed_x * -1
ball2_x += ball2_speed_x
ball2_y += ball2_speed_y
```

---
This is the solution. Does it match up with what you have or what you thought?
What were the differences, if any? What are the implications of the differences?
*****************************************************
# Collision Detection

![Collision Detection](lessons/python/lesson-8/images/collision-detection.png)

---
The next challenge in building many games is collision detection. How do you
detect when two objects meet? In our case, we would like detect the two balls
touching --- or overlapping with each other. How would we do that?
*****************************************************
# Collision Detection

* By Bounding Box
* By Distance (Circle Collision)

---
There are two methods for detecting collision: based on bounding boxes ---
meaning the 2D where the objects in question fit within; and one based on
the distance formula --- circle collision. We'll cover the distance formula
one.
*****************************************************
# Distance Formula

![Distance Formula](lessons/python/lesson-8/images/distance-formula.png)

---
This is the distance formula. Given two objects, object 1 is at position
(x1, y1) and object 2 is at position (x2, y2), this formula gives you the
distance between them.

The goal is, once we have the distance between the two balls, we can
determine if they are close together enough to be touching each other.
*****************************************************
# Distance Formula

```python
import math
```

```python
dx = ball_x - ball2_x
dy = ball_y - ball2_y
distance = math.sqrt(dx * dx + dy * dy)
```

---
This is how one might implement the distance formula within our program.
We have ball 1's position `(ball_x, ball_y)`, and ball 2's position:
`(ball2_x, ball2_y)`, this gives the distance in the `distance` variable. At
the top of your Python file, you'll need to import the math library in order
use its `sqrt` (short for square root) function. If you get the error:
`NameError: name 'math' is not defined`, you may have forgotten to import it.

Now that we have the distance between the two balls, what if statement would
you write to detect that the two balls are touch or overlapping each other?
Write down your answer, and the flip to the next slide for the solution.
*****************************************************
# Collision Detection

```python
# Automatic Updates
dx = ball_x - ball2_x
dy = ball_y - ball2_y
distance = math.sqrt(dx * dx + dy * dy)
if distance < 100:
  print('The balls collided!!!')
```

---
This code detects if the balls collide. Terrific!!!

Now, what should we do if the balls collide? Other than printing a message
to the console, I mean...
*****************************************************
# Game Over

![Game Over](lessons/python/lesson-8/images/game-over.png)

---
It should look like this!!!

What game doesn't have a proper game-over screen? To do this though, you'll
need to learn how to render text onto the screen using Pygame.
*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font(None, 40)
```

---
The first step in rendering text, is to initialize a font. You do this in the
initialization section outside of the game loop.
*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font([[None]][[Font name]], 40)
```

---
The first argument to the `Font` constructor function is a font file name.
We'll just use the default system font instead of a custom font by putting
`None` here.
*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font(None, [[40]][[Font size]])
```

---
The second argument to the `Font` constructor function is the font size.
Here we are using 40 points.
*****************************************************
# pygame.font.Font

| Argument | What it is                                           |
|----------|------------------------------------------------------|
| filename | A string containing the name of a font file or None. |
|   size   | A number containing the desired font size.           |

---

*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font(None, 40)
```

```python
# Rendering
game_over_message = font.render('GAME OVER', True, WHITE)
screen.blit(game_over_message, (200, 200))
```

---
Then, in the rendering section within the game loop, you use the `render`
method of the font object to generate a image containing the text. And then
finally, you use `screen.blit` to display that image containing the text
at a specific location of the screen.
*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font(None, 40)
```

```python
# Rendering
game_over_message = font.render([['GAME OVER']][[The text to render]], True, WHITE)
screen.blit(game_over_message, (200, 200))
```

---
The first argument to the `render` function is the text you want to render.
*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font(None, 40)
```

```python
# Rendering
game_over_message = font.render('GAME OVER', [[True]][[Anti-alias?]], WHITE)
screen.blit(game_over_message, (200, 200))
```

---
The second argument is a boolean value specifying whether you want antialiasing
for this font, which makes the text look smoother, but requires more computing
time.
*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font(None, 40)
```

```python
# Rendering
game_over_message = font.render('GAME OVER', True, [[WHITE]][[Text color]])
screen.blit(game_over_message, (200, 200))
```

---
The third argument is a 3-tuple representing the color of the text.
*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font(None, 40)
```

```python
# Rendering
[[game_over_message]][[A bitmap/surface]] = font.render('GAME OVER', True, WHITE)
screen.blit(game_over_message, (200, 200))
```

---
The output of the `render` function is a bitmap, or a surface.
*****************************************************
# Rendering Text

```python
# Initialization
font = pygame.font.Font(None, 40)
```

```python
# Rendering
game_over_message = font.render('GAME OVER', True, WHITE)
[[screen.blit(game_over_message, (200, 200))]][[Draw it on the screen]]
```

---
You use `screen.blit` to draw that bitmap onto the screen in the exact same
way you did it with images before.
*****************************************************
# Conditionally Rendering Text

```python
# Initialization
font = pygame.font.Font(None, 40)
lose = False
```

```python
# Rendering
if lose:
  game_over_message = font.render('GAME OVER', True, WHITE)
  screen.blit(game_over_message, (200, 200))
```

---
In our game though, we want to conditionally render the "GAME OVER" text,
because we only want it there if the player lost --- by letting the balls
collide. So we'll use a new variable `lose` to represent whether he has lost.
*****************************************************
# Conditionally Rendering Text

```python
# Automatic Updates
dx = ball_x - ball2_x
dy = ball_y - ball2_y
distance = math.sqrt(dx * dx + dy * dy)
if distance < 100:
  lose = True
```

---
Back in the collision detection code now, we have the answer as to what to
do when a collision has been detected, it changes the state of `lose` to `True`.
*****************************************************
# Summary

1. Game Loop
2. Updating position trigger by events
3. Updating position automatically
4. Collision detection via distance formula
5. Displaying text

---
This is what you learned. It's a lot! Now you know the basics of game
programming, and you'll be able to build your own games!!!
*****************************************************
# Homework

[Do these exercises](https://gist.github.com/airportyh/0cedc54bf31261040d1e2b8531923b32)

---
Here is your homework. Enjoy!
