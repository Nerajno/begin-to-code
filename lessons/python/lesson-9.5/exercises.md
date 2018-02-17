# Lesson 9.5 Exercises

## Gymnastics Scores

In a gymnastics competition, the judges have given their scores for a
particular performance, and they have supplied the scores in a list like so:

```python
scores = [7, 8, 9, 10, 5, 6, 7, 3, 4]
```

Your job is to calculate the average score. But, due to the very real
possibility of the judges' favoritism, you are instructed to discard the
highest and lowest scores from the list before calculating the average.

Therefore, the final score can be calculated as:

```
total score = highest score - lowest score / (number of judges - 2)
```

You will break this problem into a number of smaller sub-problems, solve each
one, and then solve the larger problem as a whole utilizing the sub-functions
(functions for the sub-problems) you've built.

The top-level function will be `final_score(scores)`, it will be aided by
3 sub functions:

* `lowest_score(scores)`
* `highest_score(scores)`
* `total_score(scores)`

You will write a list of steps for solving the top-level function, and
write a list of steps for solving each sub-function.

You will first build the 3 sub-functions, test each one in isolation,
and then build the top-level function and test that.

Below is more detail about what each function looks like.

### `lowest_score(scores)`

The `lowest_score` function takes a list of scores, and returns the lowest one.
You may assumed that any score given is 0 or greater.

Inputs:

* `scores` - a list of numbers representing all the scores from the judges

Output:

* a number representing the lowest score from the list

*Write some extra code to test this function in isolation before you move on
to the next one.*

### `highest_score(scores)`

The `highest_score` function takes a list of scores, and returns the highest one.
You may assumed that any score given is 10 or less.

Inputs:

* `scores` - a list of numbers representing all the scores from the judges

Output:

* a number representing the highest score from the list

*Write some extra code to test this function in isolation before you move on
to the next one.*

### `total_score(scores)`

The `total_score` function takes a list of scores, and returns the total of
the scores.

Inputs:

* `scores` - a list of numbers representing all the scores from the judges

Output:

* a number representing the sum of all the scores within the list

*Write some extra code to test this function in isolation before you move on
to the next one.*

### `final_score(scores)`

The `final_score` function takes the list of scores, and returns the final
score. *Hint: within this function, you will need to call each of the other
functions you've built thus far.*

Inputs:

* `scores` - a list of numbers representing all the scores from the judges

Output:

* a number representing the final score

*Write some extra code to test this function.*

## Pig Latin

### Problem Decomposition

To solve the problem below, you will:

1. Write a list of steps for solving the top-level problem.
2. Give a name to the function that will solve the top-level problem, it
should be a phrase that starts with a verb.
3. List the input parameter(s) of the top-level function, give them names,
and describe what they are.
4. Describe what the output value of the top-level function is.
5. Break up the problem into a number of smaller sub-problems.
6. For each sub-problem you identified:
    a. Write a list of steps for solving the sub-problem
    b. Give a name to this sub-function. It
    should be a phrase that starts with a verb.
    c. List the input parameter(s) of the sub-function and describe what they are.
    d. Describe what the output value of the sub-function is.

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
