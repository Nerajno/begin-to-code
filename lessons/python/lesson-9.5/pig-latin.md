## Pig Latin: Function Decomposition

To solve the problem below, you will first break up the problem into a
number of smaller subproblems.

1. What are the subproblems?
2. Structure each subproblem as a function. For each subproblem, write
the name of the function that would solve the subproblem, its inputs, and
its output.
3. What is the function that implements the entire problem? What are its inputs
and output?

**Important**: Answer the above questions and send them to your mentor/teacher
to get their feedback before starting work on implementing the functions.

### Problem Description

Pig Latin is a made up language. It is based on English and sometimes used
by parents to obfuscate their words from their children. To translate an
English word to Pig Latin:

* Move the first consonant or consonant cluster
(such as ch, tr, or dr) to the end of the word, then add "ay" to the end of the word.
* If the word starts with a vowel, add "yay" to the end of the word instead.

Examples:

```
happy day -> appyhay ayday
chicken nuggets -> ickenchay uggetsnay
apple pie -> appleway iepay
fantastic orange -> antasticfay orangeway
what the heck -> atwhay ethay eckhay
```

Write a program to ask the user to enter an English phrase, and then print
the Pig Latin version of that phrase.

### Bonus Challenge

Preserve uppercases: Preserve the uppercasing of uppercased words. For example
the phrase:

```
Dennis the Menace
```

should be translated to:

```
Ennisday ethay Enacemay
```

Would you benefit from having additional function(s) to your disposal? If so,
what are they? Write out their name, inputs and outputs.
