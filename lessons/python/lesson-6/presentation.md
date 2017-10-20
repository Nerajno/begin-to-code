# Pygame

---
This lesson you'll learn the basics of Pygame - a game creation framework
in Python. In a few lessons, you'll not only learn key fundamental concepts
in programming, but you'll get to make your very own video game!!!
****************************************************
## Installing Pygame

```
pip3 install pygame
```
---
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
***************************************************
![First Pygame Program](./lessons/python/lesson-6/images/first-program.png)

---
This is what you should see.
***************************************************
## Quitting the Program

To quit:

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
The second line initializes the Pygame engine. All Pygame programs need this
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
`pygame.display.set_caption` sets the caption on the title bar of the window
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
`pygame.display.set_mode` - sets the display mode of the program - which requires
its dimensions (height and width), which in this case is 600 wide by 400
high. `set_mode` also returns a screen object, which we'll need in order to
draw.
