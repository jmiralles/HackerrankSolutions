# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

“”””
Task
The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the first 5 inspections?

“””

number_e = 2.7182818284590451
_lambda = float(raw_input())
k = int(raw_input())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def poisson(k, _lambda):
    return (pow(_lambda, k) * pow(number_e, -1 * _lambda)) / factorial(k)

print poisson(k, _lambda)
