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

You will first build the 3 sub-functions, test each one in isolation,
and then build the top-level function and test that. Below is
more detail about what each function looks like.

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
