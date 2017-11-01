# Lesson 7 Exercises

## Clicking dots

Make a Pygame program within which whenever you click on the window, it will
draw a dot where you clicked.

## Clicking boxes

Make a Pygame program within which whenever you click on the window, it will
draw a box (a blue square) where you clicked.

## Drawing Dots

Make a Pygame program within which you can draw dots on the screen just by
moving your mouse around - it will draw a dot under whereever your mouse
has been - without event having to click. *Hint: use `pygame.MOUSEMOTION`.*

## Drawing and Erasing

Extend the previous program, but add the eraser. You can click to erase:
whenever you click on the screen, it will erase the area within a 50 pixel
radius from where you clicked.

*Hint: draw a circle that is the same color as the background.*

## Switching colors

Extend the previous program, but add the ability to switch colors.

The user can switch to one of a number of preset colors by pressing a number
key. If they press:

* 1 - red
* 2 - yellow
* 3 - blue
* 4 - green
* 5 - pink
* 6 - orange
* 7 - purple
* 8 - black

*Hint: create a variable for the color 3-tuple that gets passed as the second
argument into the `pygame.draw.circle` function.*

## Clicking Lines

Write a new Pygame program within which you can draw any number of lines.
You'd draw a line by clicking on the screen twice. The first click defines
the start point of the line, the second click defines the end point of the line.
The next click after that starts a second line.

How would you keep track of whether you are currently beginning a line or
ending a line? The *state machine pattern*.

You will use the `pygame.draw.line` function to draw a line. You can refer
to the previous lesson for the parameters you'll need.

## The Draw Program

Make another version of the drawing program you made a couple of exercises ago.
This time, instead of drawing dots everywhere your mouse moves:

1. It will draw lines. It will do this by remembering where your mouse lasts
was and then draw a line from there to where your mouse currently is.
2. It will only draw while you are dragging your mouse - meaning that you
have your primary mouse button held down.
