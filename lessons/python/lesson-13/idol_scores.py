from functools import reduce

class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

contestant = Record(
        name = "Jelly Blockton",
        judge_scores = [9, 4, 7, 8, 10, 5],
        popular_score = 10)

# The final score is the average of the judge's scores combined
# with the popular_score. But the judge's scores has a 70% weight
# while the popular score only has a 30% weight.
def final_score(contestant):
    result = reduce(lambda a, b: a + b, contestant.judge_scores, 0) / len(contestant.judge_scores) * 0.7 + contestant.popular_score * 0.3
    return result

print("%s's final score is %.2f." % (contestant.name, final_score(contestant)))
