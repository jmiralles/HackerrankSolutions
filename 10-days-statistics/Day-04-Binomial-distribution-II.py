# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

“”””
Task
A manufacturer of metal pistons finds that, on average,
12% of the pistons they manufacture are rejected because they are incorrectly sized.
What is the probability that a batch of 10 pistons will contain:

1. No more than  rejects?
2. At least  rejects?
“””

p = 0.12
n = 10
result = 0


def binomial(n, x, p):
    if p < 0 or p > 1 or n < 0 or x < 0 or x > n:
        return None
    return combinations(n, x) * pow(p, x) * pow(1 - p, n - x)

def combinations(n, x):
    if n < 0 or x < 0 or x > n:
        return None
    return factorial(n) / (factorial(x) * factorial(n - x))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

for i in range(0, 3):
    result = result + binomial(n, i, p)

print "%.3f" % result

result = 1 - binomial(n, 0, p) - binomial(n, 1, p);

print "%.3f" % result
