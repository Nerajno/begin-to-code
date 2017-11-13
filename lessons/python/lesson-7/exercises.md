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

## Super Draw

Make a "super draw" program for drawing your master piece! Tip: print out
`event.key` for keyboard events and then press the keys you want to figure
out what each key's key code is.

1. Will draw lines when you click your mouse button and drag. Stops drawing
when you release the mouse.
2. The user can change colors by pressing keys on the keyboard - you decide
what key means what color(numbers `1`, `2`, `3`, etc or specific letters
  `a`, `b`, `c`, etc).
3. The user can change thickness of the line by pressing keys on the keyboard -
you decide what key means what thickness(numbers or specific letters).
Or could chose to use only 2 keys
for this: one key to increase the thickness (`+`?) and another to decrease
the thickness (`-`?).
4. Challenge 1: eraser - the eraser is activated by holding down the spacebar
and moving the mouse around. When you release the spacebar, it stops erasing.
The eraser also uses the same thickness as the strokes and so you can
change its thickness using the method you implemented in \#3.
5. Challenge 2: LOL Cat Stamp - have a specific key (`l`?) on the keyboard (your
  choice) activate the LOL Cat Stamp tool. It will print a LOL cat image on the
  canvas every time you click - at the location of the click. Press the same key
  again to deactivate the LOL Cat Stamp.
6. Challenge 3: rectangle tool - have a specific key (`r`?) on the keyboard activate
the rectangle tool. Instead of drawing a line between the last mouse position
and the current `event.pos`, when the rectangle tool is activated, it will
fill a rectangle using the last position as one corner and the `event.pos`
as the opposite corner. Press the same key again to deactivate the rectangle
tool.
7. Draw your master piece drawing, take a screenshot of it and send it to me :)
