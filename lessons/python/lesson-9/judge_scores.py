def lowest_score(scores):
    lowest = 10
    for score in scores:
        if score < lowest:
            lowest = score
    return lowest

def highest_score(scores):
    highest = 10
    for score in scores:
        if score > highest:
            highest = score
    return highest

def total_score(scores):
    total = 0
    for score in scores:
        total += score
    return total

def final_score(scores):
    total = total_score(scores)
    highest = highest_score(scores)
    lowest = lowest_score(scores)
    total -= highest
    total -= lowest
    return total / (len(scores) - 2)

if __name__ == '__main__':
    judges = ["William", "Ann", "Justin", "Manoush", "Jake", "Candice", "Keyur"]
    scores = []

    for judge in judges:
        score = int(input("Score from %s (0-10): " % judge))
        scores.append(score)

    print("The scores were: %r" % scores)
    print("The final score is %.2f" % final_score(scores))
