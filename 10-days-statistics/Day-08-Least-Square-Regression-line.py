# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

“”””
Task

A group of five students enrolls in Statistics immediately after taking a Math aptitude test.
Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of (x, y) points:

1. (95, 85)
2. (85, 95)
3. (80, 70)
4. (70, 65)
5. (60, 70)

If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics?
Determine the equation of the best-fit line using the least squares method, then compute and print the value of when x = 80.
“””

X = [95, 85, 80, 70, 60]
Y = [85, 95, 70, 65, 70]

global mean_X
global mean_Y

def mean(array):
    length = len(array)
    _sum = sum(array)
    return _sum/length

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def stddev(data, ddof=0):
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/(n-ddof)
    return pvar**0.5


mean_X = mean(X)

mean_Y = mean(Y)

def pearson_rho(X, Y):
    num = 0
    for i in range(len(X)):
        num += (X[i] - mean_X) * (Y[i] - mean_Y)
    denom = len(X) * stddev(X) * stddev(Y)

    return (num / denom)


def linreg(X, Y):
    """ Returns a tuple of (a,b) for the parameters of regression line: Y = a + b*X """

    b = pearson_rho(X, Y) * (stddev(Y) / stddev(X))

    a = mean_Y - (b * mean_X)

    return (a, b)


x = 80

y = linreg(X, Y)[0] + linreg(X, Y)[1] * x

print(round(y, 3))
