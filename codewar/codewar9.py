# https://www.codewars.com/kata/beginner-series-number-3-sum-of-numbers/train/python


def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2


print(get_sum(2, 5))
