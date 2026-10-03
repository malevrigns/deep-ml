import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    res = []
    sum = 0
    max_score = max(scores)
    for item in scores:
        temp = math.exp(item-max_score)
        sum += temp
    for item in scores:
        temp = math.exp(item-max_score)
        res.append(round(temp/sum, 4))
    return res