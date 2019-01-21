from collections import OrderedDict
from pprint import pprint as pp

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):
    score_keys = list(HONORS.keys())
    for i in range(len(score_keys)):
        last_key = score_keys.pop()
        if user_score >= last_key:
            return HONORS[last_key]
    return None



if __name__ == "__main__":
    test_scores = [5,13,52,101,175,499,601,900,1001,303]
    for i in test_scores:
        print(get_belt(i))
