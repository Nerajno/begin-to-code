# JS Lesson 2 Exercises

You may print out this [cheatsheet](https://gist.github.com/airportyh/09edebba39e59b79d5aa8bf264e8904d) and use it while doing these problems.

## Section 1: Functions and forEach

Translate the following code from Python to JS. Use the
`forEach` method instead of a for loop in JS. Write some
extra code to test the functions.

*Tip: if you want to loop through the letters of a string,
split it into an array of one-character strings first by
using split with an empty string as the separator:
`string.split("")`. Then, you can use `forEach` to loop
through each character.*

### Tip Calculator

```python
def calculate_tip(amount, service):
  if service == "good":
    return amount * 0.2
  elif service == "fair":
    return amount * 0.15
  elif service == "poor":
    return amount * 0.1
```

### Average

```python
def average(numbers):
  total = 0
  for num in numbers:
    total += num
  return total / len(numbers)
```

### Reverse the words Redux

```python
def reverse_word(word):
  result = ""
  for letter in word:
    result = letter + result
  return result

def reverse_all_words(phrase):
  words = phrase.split(" ")
  reversed_words = []
  for word in words:
    reversed = reverse_word(word)
    reversed_words.append(reversed)
  result = " ".join(reversed_words)
  return result
```

## Section 2: Objects

Translate the following functions from Python to JS. Write some
extra code to test the functions.

### Word Histogram

```python
def word_histogram(phrase):
  histogram = {}
  words = phrase.split(" ")
  for word in words:
    if word not in histogram:
      histogram[word] = 0
    histogram[word] += 1
  return histogram
```

### Dream Team

Tip: convert the following code a bit at a time, not all at once. Test
your code after each bit.

```python
class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record %r" % self.__dict__

barkley  = Record(name="Charles Barkley",    gp=6, pts=98, fgm=34, fga=58)
bird     = Record(name="Larry Bird",         gp=2, pts=19, fgm=8,  fga=11)
clyde    = Record(name="Clyde Drexler",      gp=5, pts=69, fgm=27, fga=39)
ewing    = Record(name="Patrick Ewing",      gp=5, pts=59, fgm=27, fga=43)
magic    = Record(name="Magic Johnson",      gp=6, pts=58, fgm=19, fga=34)
jordan   = Record(name="Michael Jordan",     gp=6, pts=76, fgm=29, fga=53)
laettner = Record(name="Christian Laettner", gp=6, pts=44, fgm=18, fga=31)
malone   = Record(name="Carl Malone",        gp=6, pts=89, fgm=33, fga=53)
mullin   = Record(name="Chris Mullin",       gp=6, pts=86, fgm=31, fga=49)
pippen   = Record(name="Scottie Pippen",     gp=6, pts=48, fgm=20, fga=30)
robinson = Record(name="David Robinson",     gp=6, pts=71, fgm=32, fga=42)
stockton = Record(name="John Stockton",      gp=2, pts=10, fgm=5,  fga=6 )

dream_team = [
    barkley, bird, clyde, ewing, magic, jordan, laettner,
    malone, mullin, pippen, robinson, stockton
]

def most_points(players):
    highest_pts = 0
    highest_player = None
    for player in players:
        if player.pts > highest_pts:
            highest_pts = player.pts
            highest_player = player
    return highest_player

def print_fg_avg(players):
  for player in players:
      fg_avg = 100 * player.fgm / player.fga
      print("%s's field goal percentage is %.2f%%" % (player.name, fg_avg))

def scoring_histogram(players):
  score_bracket_dict = {
    0: "0-4",
    5: "5-9",
    10: "10-14",
    15: "15-19",
    20: "20-24"
  }
  histogram = {}
  for player in players:
    pts_per_game = player.pts / player.gp
    score_bracket = (pts_per_game // 5) * 5
    key = score_bracket_dict[score_bracket]
    if key not in histogram:
      histogram[key] = []
    histogram[key].append(player)
  return histogram

print_fg_avg(dream_team)
print()

high_scorer = most_points(dream_team)
print("%s is the highest scorer with %d points." % (high_scorer.name, high_scorer.pts))
print()

histogram = scoring_histogram(dream_team)
for key, players in histogram.items():
  print("Players who scored %s points:" % key)
  for player in players:
    print("  %s" % player.name)
```

### Final Project Rewrite

If applicable, take your Python final project and rewrite it
in JavaScript.

### Code Challenges

* Go on Code Wars or similar code challenge sites and challenge yourself
even more!
