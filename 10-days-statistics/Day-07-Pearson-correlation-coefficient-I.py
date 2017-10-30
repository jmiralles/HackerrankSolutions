# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem


“”””
Task

Given two -element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

“””

import math

def pearson(xs, ys):
    if xs == None or ys == None or len(xs) != len(ys):
        return None

    xMean = getMean(xs)
    yMean = getMean(xs)

    n = len(xs)

    numerator = 0
    for i in range(n):
        numerator += (xs[i] - xMean) * (ys[i] - yMean)

    return numerator / (n * standardDeviation(xs) * standardDeviation(ys))


def getMean(array):
    if array == None:
        return None

    total = 0

    for num in array:
        total += num

    return total / len(array)


def standardDeviation(array):
    if array == None:
        return None

    mean = getMean(array)
    sum = 0
    for x in array:
        sum += math.pow(x - mean, 2)

    variance = sum / len(array)
    return math.sqrt(variance)

size = int(raw_input())


xs = map(float, raw_input().split())
xy = map(float, raw_input().split())


print("%.3f" % pearson(xs, xy))
