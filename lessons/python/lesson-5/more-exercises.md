# Lesson 5 More Exercises

## Terminal Colors

To write colored text in the terminal, you'd use special *control sequence*.
For example, to print a red HELLO on the screen you would write:

```python
print("\033[31mHELLO\033[0m")
```

If you are familiar with HTML, you can think of `\033[31m` as the open tag
(like `<h1>`) - let's call this the open sequence. You can think of `\033[0m`
as the close tag (like `</h1>`) - let's call this the close sequence.
The text `HELLO` is like the content text inside those two tags.
You might notice that the open sequence and the close sequence have everything
in common except for the number to the left of the last `m` character:

```
\033[Xm
```

`X` is the *control code* of the sequence. The code for the close sequence
is always 0. The code for the open sequence determines how the text appears:

| Code |     Appearance      |
|------|---------------------|
|  1   |        Bold         |
|  2   |        Dim          |
|  4   |     Underlined      |
|  5   |        Blink        |
|  7   |    Color Inverse    |
|  30  |        Black        |
|  31  |         Red         |
|  32  |        Green        |
|  33  |        Yellow       |
|  34  |        Blue         |
|  35  |       Magenta       |
|  36  |        Cyan         |

If you want more, you can get [the full list of codes](https://misc.flogisoft.com/bash/tip_colors_and_formatting).

If you have a code number in a variable called `code`, you can use the `%d`
string formatter to substitute it into a string like so:

```python
code = 31
print("\033[%dmHELLO\033[0m" % code)
```

Then maybe next time you change the code and use the exact same code to print
it again:

```python
code = 33
print("\033[%dmHELLO\033[0m" % code)
```

Or better yet! You have a list of codes:

```python
codes = [31, 35, 33, 34, 32]
```

And you use a loop to print "HELLO" in all of those different colors.

## Exercise 1

Ask the user for a code, and then print "Hello world" with that code as the
control code.

## Exercise 2

Ask the user for a code, and the text message, to print. Print that message
using that control code.

## Exercise 3

Ask the user for a text message with optional asterisks (\*) in them to surround
phrases or words. Convert the part inside the asterisk to red. So:
`Pass me the *french fries*!` should convert to `Pass me the \033[31mfrench fries\033[0m`

## Exercise 4

Extend the above exercise to convert text surrounded by understores (\_) to
yellow. So `This Sunday the _Browns_ are playing vs the *Reds*.` should
convert to `This Sunday the \033[33mBrowns\033[0m are playing vs the \033[31mreds\033[0m`.

## Exercise 5

You will implement basic HTML-like tags!!!

The user can input tags like `This <magenta>Sunday</magenta>, the <yellow>Browns</yellow> are playing vs the <red>Reds</red>.` and those parts in
the tags are printed in those respective colors in the terminal.
