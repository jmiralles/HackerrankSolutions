# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

“”””
Task
The ratio of boys to girls for babies born in Russia 1.0.9 : 1 is . If there 1 is  child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

“””

r = 1.09
p = r/(1+r)
q = 1 - p
n = 6
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

for i in range(3, n+1):
    result = result + binomial(n, i, p)

print "%.3f" % result
