# Pygame

---
This lesson you'll learn the basics of Pygame - a game creation framework
in Python. In a few lessons, you'll not only learn key fundamental concepts
in programming, but you'll get to make your very own video game!!!
****************************************************
## New Concept: Tuples
---
But before we get started, I need to introduce a new concept to you
which will be used in the lesson: tuples.
****************************************************
## Definition: Tuple

An immutable (cannot be changed) ordered sequence of values.

---
A tuple in Python is a an immutable - meaning cannot be changed -
ordered sequence of values. It is commonly used to group a set of related
values. It is similar to lists with the main difference that it is immutable.
****************************************************
## Tuples

```python
(1, 2)
```

---
This is a tuple in Python. It is written as a comma-separated list of
values, surrounded by parenthesis. Very much like the argument list
of a function call:

```python
print(1, 2)
```

Except that there is no function name to the left of the parenthesis.
****************************************************
## Tuples

```python
my_tuple = [[(1, 2)]][[A tuple expression]]
```

---
A tuple is an expression and you can assign it to a variable just like
any other expression.
****************************************************
## Tuples

```python
a_2_tuple = (1, 2)
a_3_tuple = (3, 4, 6)

a_4_tuple_of_strings = ("apple", "orange", "pear", "kiwi")
a_2_tuple_of_lists = ([1, 2, 3], [4, 5, 6])
```

---

A tuple can contain any number of values. A tuple that contains 2 values is
called a 2-tuple. One that contains 3 values is called a 3-tuple, and so on.

A tuple can also contain any kind of values, including numbers, strings, lists,
and more.
****************************************************
## Tuples

```python
apples = ("apple", 2)
oranges = ("orange", 5)
```

---
A tuple can also contain mixed types of things, such as strings and numbers.
****************************************************
## Tuples vs Lists

```python
tuple_of_numbers = (4, 3, 8, 1)
list_of_numbers = [5, 2, 7, 9]
```
---
Tuples are very much like lists, in that both of them are a sequence of
values.
****************************************************
## Tuples vs Lists

```python
tuple_of_numbers = (4, 3, 8, 1)

four = tuple_of_numbers[0]
three = tuple_of_numbers[1]
eight = tuple_of_numbers[2]
one = tuple_of_numbers[3]
```
---
You can use the subscript notation to access an element of a tuple by its
index, in the same way you can with a list.
****************************************************
## Tuples vs Lists

```python
tuple_of_numbers = (4, 3, 8, 1)

the_length = len(tuple_of_numbers)
```
---
You can also get the length of a tuple using the `len` function, like a list.
****************************************************
## Tuples vs Lists

```python
tuple_of_numbers = (4, 3, 8, 1)

for number in tuple_of_numbers:
  print(number)
```
---
And you can use a for loop to iterate through its values just like a list.
****************************************************
## Tuples vs Lists

```python
tuple_of_numbers = (4, 3, 8, 1)
```
---
They are different from lists in that they are *immutable* - which means
that they cannot be modified.
****************************************************
## Tuples vs Lists

```python
tuple_of_numbers[1] = 5
```

`TypeError: 'tuple' object does not support item assignment`
---
If you tried to change the value within one of the slots of a tuple,
you would get this error - that a tuple does not support the item
assignment operation.
****************************************************
## Tuples vs Lists

```python
tuple_of_numbers.append(7)
```

`AttributeError: 'tuple' object has no attribute 'append'`
---
Like-wise, if you tried to append a new value to a tuple, you
would get this error, that a tuple object doesn't not have
an attribute append - which a list object does.
****************************************************
## Tuples

```python
a_position = (50, 100)
a_dimension = (800, 600)
a_color = (255, 0, 0)
```

---
In the context of Pygame, we'll often be using tuples to represent
positions, dimensions and colors.

A position in 2D is represented as a tuple
of two numbers - an x coordinate and a y coordinate.

A screen dimension is represented as a tuple of two numbers as well,
a width and a height.

A color in RGB (Red Green and Blue) is represented as three numbers
between 0 and 255. The first number being the intensity of the red,
the second being the intensity of the green, and the third being
the intensity of the blue.
****************************************************
## Installing Pygame

```
pip3 install pygame
```
---
Okay. Now we are ready to start Pygame...

First things first. You have to install Pygame before you can use it. Run
this command in your terminal, and then hit Enter, then you should have Pygame
installed. If you run into permission issues, try putting `sudo` in front of
the command, as in:

```
sudo pip3 install pygame
```

Then the system will ask you to enter your password before it proceeds.
***************************************************
## Your First Pygame Program

```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```
---
This is your first Pygame program. Please type it into a new `.py` file,
you may name it what you want, and then run the program.

Unfortunately, Python Tutor does not support Pygame, and therefore, you'll
not be able to use it to debug your program. More on this later.
***************************************************
![First Pygame Program](./lessons/python/lesson-6/images/first-program.png)

---
This is what you should see.
***************************************************
## Quitting the Program

1. Switch back to terminal
2. `Control-C`
---
To quit the program, you'd have to first switch back to your terminal, and then
use the key combination `Control-C` - which means press the `Control` and `C`
keys on your keyboard simultaneously.
***************************************************
```python
[[import pygame]][[Import statement that imports pygame]]

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```
---
Now let's walk through this program line by line.

The first line is called an *import statement*. It "brings in" the pygame
library and makes it available to this program.

The word "import" is a Python
keyword, while the word "pygame" is the name by which the Pygame library
is referenced. If you hadn't install Pygame properly, the program would fail
on this line.
***************************************************
```python
import pygame

[[pygame.init()]][[Initialize the Pygame engine]]
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```
---
The second line calls the `init` function that's provided by the `pygame`
module. What it does is initializes the Pygame engine. All Pygame programs need this
line.
***************************************************
```python
import pygame

pygame.init()
[[pygame.display.set_caption('A Red Circle')]][[Sets the title]]
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```
---
The next line calls the `set_caption` function on `pygame.display` - which
is Pygame's display module - a submodule of Pygame.

`set_caption` sets the caption on the title bar of the window
that's going to launch when we run this program --- exciting!!!
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
[[screen = pygame.display.set_mode((600, 400))]][[Sets display mode and creates screen]]

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```
---
The next line gets even *more* exciting! It creates the screen/window that
we are going to draw on.

The `set_mode` function on the `pygame.display` module takes in a dimension
(height and width) represented as a tuple, and
creates a window of that size as well as sets its display mode. Then,
it returns a screen object, which will be used to draw on in subsequent
commands. Now it is really not the entire screen, but the part of the
screen within that's within the window that pops up.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

[[screen.fill((0, 0, 0))]][[Fills the window with black]]
pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```

---
Now we have a screen (or window) to draw on, and the first thing we do
is paint the entire background in black! This is done with the `fill`
function on the `screen` object - if you called this the `fill` method,
you would also be correct.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
[[pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, 0)]][[BAM!!! Circle]]

pygame.display.update()

while True:
    pass
```

---
The next part may be the most exciting part of all!!! Actually drawing
a circle on the screen. This is done using the `circle` function of the
`pygame.draw` module. The `circle` function takes this list of arguments:

* a screen object
* a 3-tuple representing a color
* a 2-tuple representing
* the radius of the circle
* a number representing the thickness of the circle border; if the thickness is
0, it fills the entire circle

So with this particular set of arguments...
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle([[screen]][[Our screen object]], (255, 0, 0), (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```

---
First we pass to it the screen object we created in the 4th line of the program.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, [[(255, 0, 0)]][[The color red]], (300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```

---
Then we pass in a 3-tuple `(255, 0, 0)` - representing the color red, given
that the intensity for red - the first value has been set to 255 - the maximum
value, while the intensities for green and blue have been set to 0 - the minimum
value.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), [[(300, 200)]][[x coordinate 300, y coordinate 200]], 100, 0)

pygame.display.update()

while True:
    pass
```

---
Then we pass in a 2-tuple `(300, 200)` - 300 for the x coordinate, 200 for the
y coordinate.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (300, 200), [[100]][[100 pixel radius]], 0)

pygame.display.update()

while True:
    pass
```

---
Then we pass in a single number 100 to be the radius of the circle.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), (300, 200), 100, [[0]][[0 thickness means fill]])

pygame.display.update()

while True:
    pass
```
---
Finally, for the thickness argument, we pass in the value 0, which means
rather than stroke the border of the circle, we want the `circle` function
to fill the entire circle with red instead.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), [(300, 200), 100, 0)

[[pygame.display.update()]][[Updates the display to what we just drew]]

while True:
    pass
```
---
Next, we have to call the `update` function of the `pygame.display` module
in order to actually display the circle that we just drew.
***************************************************
## Double buffering

![Flip over whiteboard](./lessons/python/lesson-6/images/flip-over.jpg)

---
Why is this? For performance reasons, Pygame uses a technique called *double
buffering*. This means that whenever you are drawing on the screen, instead
of drawing directly on the screen, you are actually drawing on a secondary
invisible screen, called the *buffer*. When you are done drawing on the buffer,
you will tell Pygame to update the screen with the contents of the buffer,
and it will do so.

Image you are drawing for an audience. But instead of drawing
right in front of the audience, you are drawing on the back side of a flipover
whiteboard. Whenever you are
done with the next drawing, you call `pygame.display.update()` and that flips
the white board over so that the audience can see your new drawing, and then
you draw on the back side again. That's double buffering.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), [(300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```
---
Back to this...
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), [(300, 200), 100, 0)

pygame.display.update()

[[while True:
    pass]][[An infinite loop to keep the game going]]
```
---
Finally, we have a while loop at the end of the program that loops infinitely.
Why? Because we don't want the game to end. If we didn't have this loop here,
the window would display only for a moment, and then the program would end,
causing the window to close.

This infinite loop is called the game loop, and once you start writing games,
you'll put logic inside of it to update and display game objects.
***************************************************
```python
import pygame

pygame.init()
pygame.display.set_caption('A Red Circle')
screen = pygame.display.set_mode((600, 400))

screen.fill((0, 0, 0))
pygame.draw.circle(screen, (255, 0, 0), [(300, 200), 100, 0)

pygame.display.update()

while True:
    pass
```
---
Now, can you modify this program...
***************************************************
![Mickey](./lessons/python/lesson-6/images/mickey.png)

---
to draw a silhouette of Mickey Mouse?
***************************************************
## Drawing Functions

| Function            |      Use         |
|---------------------|------------------|
| pygame.draw.circle  | Draw a circle    |
| pygame.draw.rect    | Draw a rectangle |
| pygame.draw.line    | Draw a line      |
| pygame.draw.polygon | Draw a polygon   |

---
To give you more abilities with this canvas, here is a list of some basic
things you can draw within Pygame. We'll go over each one.
***************************************************
## pygame.draw.circle

```python
pygame.draw.circle(screen, color, coords, radius, thickness)
```


| Argument  |                                 What it is                                 |
|-----------|----------------------------------------------------------------------------|
| screen    | a screen object created using pygame.display.set_mode                      |
| color     | a 3-tuple representing the Red, Green and Blue intensities                 |
| coords    | a 2-tuple representing x and y coordinates                                 |
| radius    | radius of the circle                                                       |
| thickness | a number - thickness of border, if the thickness is 0, it fills the circle |

---
As we've covered before, to draw a circle in Pygame, you need to supply these
arguments.
***************************************************
## pygame.draw.rect

```python
pygame.draw.rect(screen, color, rect, thickness)
```


| Argument  |                                 What it is                                 |
|-----------|----------------------------------------------------------------------------|
| screen    | a screen object created using pygame.display.set_mode                      |
| color     | a 3-tuple representing the Red, Green and Blue intensities                 |
| rect      | a 4-tuple representing the x and y coordinates, and then the width and height of the rectangle |
| thickness | a number - thickness of border, if the thickness is 0, it fills the rectangle |

---
This is the function you'd use to draw a rectangle on the screen and the
arguments you need to pass to it.
***************************************************
## pygame.draw.line

```python
pygame.draw.line(screen, color, start_pos, end_pos, thickness)
```


| Argument  |                                 What it is                                 |
|-----------|----------------------------------------------------------------------------|
| screen    | a screen object created using pygame.display.set_mode                      |
| color     | a 3-tuple representing the Red, Green and Blue intensities                 |
| start_pos | a 2-tuple representing the start x and y coordinates - where to start drawing the line |
| end_pos   | a 2-tuple representing the end x and y coordinates - where to start drawing the line |
| thickness | a number - thickness of the line                                           |

---
This is the function you'd use to draw a line on the screen and the
arguments you need to pass to it.
***************************************************
## pygame.draw.polygon

```python
pygame.draw.polygon(screen, color, point_list, thickness)
```


| Argument   |                                 What it is                                 |
|------------|----------------------------------------------------------------------------|
| screen     | a screen object created using pygame.display.set_mode                      |
| color      | a 3-tuple representing the Red, Green and Blue intensities                 |
| point_list | a list of 2-tuples representing the start x and y coordinates of each vertex (corner) of the polygon |
| thickness | a number - thickness of border, if the thickness is 0, it fills the polygon |

---
This is the function you'd use to draw a polygon - which lets you draw
any shape that can be draw with a series of straight lines on the screen and the
arguments you need to pass to it.
***************************************************
## Draw This

![Simple House](./lessons/python/lesson-6/images/house-simple.png)

---
Now armed with these weapons, I'd like you to write a program to draw this
house.
***************************************************
## Copying Images

```python
an_image = pygame.image.load('images/LOLCat.jpg')

screen.blit(an_image, (0, 0))
```

---
I want to give you one more ability: to be able to take an image you have,
and copy it onto the canvas. It takes two steps to do this...
***************************************************
## Copying Images

```python
an_image = [[pygame.image.load('images/LOLCat.jpg')]][[Loads an image file]]

screen.blit(an_image, (0, 0))
```

---
First, to load an image file into an image object using the `load` function
of the `pygame.image` module. This function returns an image object.
***************************************************
## Copying Images

```python
[[an_image]][[An image object]] = pygame.image.load('images/LOLCat.jpg')

screen.blit(an_image, (0, 0))
```

---
After this line is executed, the `an_image` variable will contain an image
object.
***************************************************
## Copying Images

```python
an_image = pygame.image.load('images/LOLCat.jpg')

[[screen.blit(an_image, (0, 0))]][[Copies image to the screen]]
```

---
Now to draw the image onto the screen, we will use the `blit` function
of the screen object. `BLIT` stands for block image transfer, and it performs a
copy from the image of the image file to the screen.
***************************************************
## Copying Images

```python
an_image = pygame.image.load('images/LOLCat.jpg')

screen.blit([[an_image]][[The image object]], (0, 0))
```

---
Blit takes two arguments: the image object.
***************************************************
## Copying Images

```python
an_image = pygame.image.load('images/LOLCat.jpg')

screen.blit(an_image, [[(0, 0)]][[Coordinates to copy to]])
```

---
And the coordinates to copy the image to, as a 2-tuple.
***************************************************
## Summary

* Tuples
* Pygame
* Drawing
  * circles
  * rectangles
  * lines
  * polygons
  * images
---
This is a summary of what you learned.
***************************************************
## Homework

[Homework](https://gist.github.com/airportyh/a32858f149d25ccd07d3bc04993ee9eb)

---
Here is your homework. Good luck! Ask questions if you get stuck.
