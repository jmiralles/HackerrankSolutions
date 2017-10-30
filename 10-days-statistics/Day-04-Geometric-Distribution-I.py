# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

“”””
Task
The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the 5th inspection?
“””

a = raw_input().split()
n = float(raw_input())

numerator = float(a[0])
denominator = float(a[1])

def geometric(n, p):
    return pow(1 - p, n - 1) * p

p = numerator / denominator

print "%.3f" % geometric(n, p)
