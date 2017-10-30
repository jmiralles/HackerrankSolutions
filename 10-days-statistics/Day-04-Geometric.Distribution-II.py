# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

“”””
Task
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the first 5 inspections?

“””

a = raw_input().split()
n = int(raw_input())

numerator = float(a[0])
denominator = float(a[1])

def geometric(n, p):
    return pow(1 - p, n - 1) * p

p = numerator / denominator

result = 0
for i in range(1, n +1):
    result += geometric(i, p)

print "%.3f" % result
