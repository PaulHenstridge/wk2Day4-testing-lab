def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    length = len(scores)
    index = 3
    if length < 3:
        index = length
    scores.sort(reverse=True)
    return scores[0:index]


def highest_to_lowest(scores):
    scores.sort(reverse=True)
    return scores


# print(highest_to_lowest([1, 2, 3, 4, 5]))
