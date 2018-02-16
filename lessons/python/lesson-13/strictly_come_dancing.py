# This implements a simplified version of the Strictly Come Dancing
# scoring system. For more info:
# http://tv.bt.com/tv/strictly-come-dancing/voting-11364202272549
# https://www.youtube.com/watch?v=ZoA0u66wcSs

from functools import reduce

class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

contestants = [
    Record(name = "Mack", judge_scores = [9, 8, 6], audience_votes = 3481),
    Record(name = "Jane", judge_scores = [10, 9, 10], audience_votes = 9456),
    Record(name = "Amjad", judge_scores = [10, 8, 10], audience_votes = 1204),
    Record(name = "Manoush", judge_scores = [9, 8, 7], audience_votes = 4967),
    Record(name = "Anushka", judge_scores = [9, 8, 9], audience_votes = 2252),
    Record(name = "Jamal", judge_scores = [9, 8, 8], audience_votes = 12356),
    Record(name = "Karen", judge_scores = [6, 8, 5], audience_votes = 443),
    Record(name = "Lamar", judge_scores = [4, 5, 8], audience_votes = 4683)
]

numbers = {
    0: "first",
    1: "second",
    2: "third"
}

def judge_score(contestant):
    return reduce(lambda a, b: a + b, contestant.judge_scores, 0) / len(contestant.judge_scores)

judge_rank = sorted(contestants, key=judge_score, reverse=True)
audience_rank = sorted(contestants, key=lambda c: c.audience_votes, reverse=True)

for i in range(len(judge_rank)):
    contestant = judge_rank[i]
    contestant.judge_score = len(judge_rank) - i

for i in range(len(audience_rank)):
    contestant = audience_rank[i]
    contestant.audience_score = len(audience_rank) - i

final_rank = sorted(contestants, key=lambda c: c.judge_score + c.audience_score, reverse=True)

for i in range(3):
    print("The %s place winner is %s." % (numbers[i], final_rank[i].name))
